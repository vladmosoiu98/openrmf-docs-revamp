===========================
Local Development Setup
===========================

This page describes how to set up a local development environment for working on
OpenRMF OSS microservices.

Prerequisites
=============

- **.NET SDK 8.0** (or the version matching the current OpenRMF release)
- **Docker** or **Podman** (for running infrastructure services)
- **MongoDB** client tools (optional, for database inspection)
- **Git**
- A code editor (Visual Studio, VS Code with C# extension, or JetBrains Rider)

Running Infrastructure Locally
================================

Even when developing a single microservice, you need the shared infrastructure
running: MongoDB, NATS, and optionally Keycloak. The easiest approach is to use
the Docker Compose file from the ``openrmf-docs`` repository, but only start the
infrastructure services::

   cd openrmf-docs/scripts

   # Start only infrastructure
   docker compose up -d openrmf-mongo nats openrmf-keycloak openrmf-postgres

This gives you:

- MongoDB on ``localhost:27017``
- NATS on ``localhost:4222``
- Keycloak on ``localhost:8080/auth/``
- PostgreSQL on ``localhost:5432``

Cloning a Service Repository
=============================

Each service is an independent repository::

   git clone https://github.com/Cingulara/openrmf-api-read.git
   cd openrmf-api-read/src

Running a Service Locally
==========================

From the ``src/`` directory of any API service::

   dotnet restore
   dotnet run

The service starts on ``http://localhost:8080`` by default. Environment variables
for MongoDB connection strings, NATS URLs, and JWT configuration can be set in a
``launchSettings.json`` file or passed directly::

   DBCONNECTION="mongodb://openrmf:openrmf1234!@localhost/openrmf?authSource=admin" \
   NATSSERVERURL="nats://localhost:4222" \
   JWTAUTHORITY="http://localhost:8080/auth/realms/openrmf" \
   JWTCLIENT="openrmf" \
   dotnet run

Environment Variables
=====================

Each service uses a common set of environment variables:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``DBCONNECTION``
     - MongoDB connection string
   * - ``DBTYPE``
     - Database type identifier
   * - ``NATSSERVERURL``
     - NATS server connection URL
   * - ``JWTAUTHORITY``
     - Keycloak realm URL for JWT validation
   * - ``JWTCLIENT``
     - Keycloak client ID (typically ``openrmf``)
   * - ``JAABORHOST``
     - Jaeger tracing endpoint (optional)

Developing the Web Frontend
============================

The ``openrmf-web`` repository contains the static frontend. To develop locally:

1. Clone the repository::

      git clone https://github.com/Cingulara/openrmf-web.git

2. The frontend is plain HTML/JavaScript/CSS (no build step required for the main
   app). Files are in the ``wwwroot/`` directory.

3. For the help documentation, Jekyll is used::

      cd help/
      bundle install
      bundle exec jekyll build

4. To test locally, serve the ``wwwroot/`` directory with any static file server or
   configure NGINX to proxy API requests to your locally running services.
