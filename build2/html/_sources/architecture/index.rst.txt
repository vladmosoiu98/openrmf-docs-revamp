========================
Architecture Overview
========================

OpenRMF OSS follows a microservices architecture that was introduced in January 2019
(version 1.0) and has remained structurally stable through version 1.9. The system
uses RESTful APIs built on .NET Core, asynchronous messaging through NATS, MongoDB
for persistence, NGINX as a reverse proxy, and Keycloak for identity management.

Design Principles
=================

The architecture is guided by several key principles:

**Microservices Decomposition**
   Each bounded context (checklists, scoring, compliance, templates, auditing,
   reporting) is implemented as an independent service with its own codebase and
   container image. Services can be scaled, deployed, and updated independently.

**CQRS (Command Query Responsibility Segregation)**
   Write operations (uploads, edits, deletes) and read operations (listings, exports,
   reports) are handled by separate services. This allows the read path to be
   optimized for query performance with denormalized data while the write path
   maintains data integrity.

**Eventual Consistency**
   When a checklist is uploaded or modified, the write-side API publishes a NATS
   message. Subscriber services (scoring, reporting) process the message
   asynchronously and update their own data stores. This means report data may lag
   slightly behind the source of truth, but the system scales better under load.

**Containerized Deployment**
   Every service is packaged as an OCI-compliant container image. The full stack is
   orchestrated through Docker Compose or Kubernetes, making deployments reproducible
   across development, staging, and production environments.

High-Level Component Diagram
=============================

The following diagram shows the major components and their interactions::

   ┌─────────────────────────────────────────────────────────────┐
   │                        Browser                              │
   └──────────────────────────┬──────────────────────────────────┘
                              │ HTTPS/HTTP :8080 or :8443
                              ▼
   ┌─────────────────────────────────────────────────────────────┐
   │                    NGINX (openrmf-web)                      │
   │              Reverse Proxy + Static Frontend                │
   └──┬───────┬───────┬───────┬───────┬───────┬───────┬─────────┘
      │       │       │       │       │       │       │
      ▼       ▼       ▼       ▼       ▼       ▼       ▼
   ┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
   │ Read ││ Save ││Upload││Templ.││Score ││Ctrl. ││Compl.│  ... APIs
   │ API  ││ API  ││ API  ││ API  ││ API  ││ API  ││ API  │
   └──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘
      │       │       │       │       │       │       │
      ▼       ▼       ▼       ▼       ▼       ▼       ▼
   ┌─────────────────────────────────────────────────────────────┐
   │                      NATS Message Bus                       │
   │           (Publish/Subscribe + Request/Reply)               │
   └──┬───────┬───────┬───────┬───────┬───────┬─────────────────┘
      │       │       │       │       │       │
      ▼       ▼       ▼       ▼       ▼       ▼
   ┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
   │ msg- ││ msg- ││ msg- ││ msg- ││ msg- ││ msg- │  Messaging
   │score ││report││system││audit ││compl.││ctrl. │  Services
   └──┬───┘└──┬───┘└──┬───┘└──┬───┘└──────┘└──────┘
      │       │       │       │
      ▼       ▼       ▼       ▼
   ┌─────────────────────────────────────────────────────────────┐
   │                   MongoDB Databases                         │
   │  (Artifacts, Scores, Reports, Audit, Templates)             │
   └─────────────────────────────────────────────────────────────┘

   ┌───────────────┐  ┌───────────────────┐  ┌──────────────────┐
   │   Keycloak     │  │   Prometheus      │  │    Grafana       │
   │ (PostgreSQL)   │  │   (Metrics)       │  │  (Dashboards)    │
   └───────────────┘  └───────────────────┘  └──────────────────┘

Component Categories
====================

The system is divided into four categories of components:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Category
     - Description
   * - **Web Frontend**
     - NGINX serving static HTML/JS/CSS built on the Pike Admin Bootstrap 4 theme.
       All API calls are made from the browser to backend services through the NGINX
       reverse proxy.
   * - **API Services**
     - Nine .NET Core Web APIs handling RESTful requests. Each API has its own
       Swagger documentation endpoint at ``/swagger/``.
   * - **Messaging Services**
     - Seven NATS client services implementing the asynchronous processing layer.
       These handle scoring, reporting, compliance mapping, system updates, auditing,
       and template lookups.
   * - **Infrastructure**
     - MongoDB (data), NATS (messaging), Keycloak + PostgreSQL (auth), Prometheus
       (metrics), Grafana (dashboards), and NGINX (reverse proxy).

.. toctree::
   :maxdepth: 1

   microservices
   messaging
   data-layer
