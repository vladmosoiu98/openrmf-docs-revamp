==============
Repository Map
==============

OpenRMF OSS is a multi-repository project hosted under the
`Cingulara <https://github.com/Cingulara>`_ GitHub organization. This page provides
a quick reference of all 22 repositories.

API Services
============

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Repository
     - Description
   * - `openrmf-api-read <https://github.com/Cingulara/openrmf-api-read>`_
     - Checklist retrieval, export, system listing, document generation (POA&M, RAR,
       Test Plan). Also handles uploads and saves as of v1.8.
   * - `openrmf-api-save <https://github.com/Cingulara/openrmf-api-save>`_
     - Artifact and system CRUD operations, vulnerability editing.
   * - `openrmf-api-upload <https://github.com/Cingulara/openrmf-api-upload>`_
     - CKL and SCAP XCCDF file upload processing.
   * - `openrmf-api-template <https://github.com/Cingulara/openrmf-api-template>`_
     - Checklist template management for SCAP scan matching.
   * - `openrmf-api-scoring <https://github.com/Cingulara/openrmf-api-scoring>`_
     - STIG vulnerability scoring (stored and on-the-fly).
   * - `openrmf-api-controls <https://github.com/Cingulara/openrmf-api-controls>`_
     - NIST 800-53 control lookups.
   * - `openrmf-api-compliance <https://github.com/Cingulara/openrmf-api-compliance>`_
     - Compliance assessment against NIST baselines.
   * - `openrmf-api-audit <https://github.com/Cingulara/openrmf-api-audit>`_
     - Audit log query interface (admin only).
   * - `openrmf-api-reports <https://github.com/Cingulara/openrmf-api-reports>`_
     - Pre-computed report data (Nessus, vulnerability).

Messaging Services
==================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Repository
     - Description
   * - `openrmf-msg-score <https://github.com/Cingulara/openrmf-msg-score>`_
     - Scores checklists on save/update, persists to MongoDB.
   * - `openrmf-msg-reports <https://github.com/Cingulara/openrmf-msg-reports>`_
     - Parses raw data into denormalized report structures.
   * - `openrmf-msg-system <https://github.com/Cingulara/openrmf-msg-system>`_
     - Maintains system-level metadata and checklist counts.
   * - `openrmf-msg-audit <https://github.com/Cingulara/openrmf-msg-audit>`_
     - Records auditable events.
   * - `openrmf-msg-compliance <https://github.com/Cingulara/openrmf-msg-compliance>`_
     - CCI-to-NIST control mapping via request/reply.
   * - `openrmf-msg-controls <https://github.com/Cingulara/openrmf-msg-controls>`_
     - RMF control lookups via request/reply.
   * - `openrmf-msg-template <https://github.com/Cingulara/openrmf-msg-template>`_
     - Template retrieval via request/reply.
   * - `openrmf-msg-checklist <https://github.com/Cingulara/openrmf-msg-checklist>`_
     - Checklist/artifact information via request/reply.

Frontend
========

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Repository
     - Description
   * - `openrmf-web <https://github.com/Cingulara/openrmf-web>`_
     - Browser-based UI (JavaScript, HTML, CSS on Pike Admin Bootstrap 4).

Documentation and Infrastructure
=================================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Repository
     - Description
   * - `openrmf-docs <https://github.com/Cingulara/openrmf-docs>`_
     - Documentation, Docker Compose files, Kubernetes Helm charts, scripts.
   * - `openrmf-at-aws <https://github.com/Cingulara/openrmf-at-aws>`_
     - Terraform + Ansible provisioning for AWS.
   * - `openrmf-ext-api-score <https://github.com/Cingulara/openrmf-ext-api-score>`_
     - Standalone external scoring API.
   * - `openrmf-io <https://github.com/Cingulara/openrmf-io>`_
     - Source for the openrmf.io website.

Standard Repository Structure
==============================

Most C# service repositories follow this layout::

   openrmf-api-<name>/
   ├── .github/           # GitHub Actions workflows
   ├── src/               # Application source code
   │   ├── Controllers/   # API endpoint definitions
   │   ├── Models/        # Data models
   │   ├── Data/          # Database context and repositories
   │   ├── Classes/       # Business logic and utilities
   │   └── Program.cs     # Application entry point
   ├── tests/             # Unit tests
   ├── Dockerfile         # Container build definition
   ├── Makefile           # Build automation
   ├── LICENSE            # GPL-3.0
   └── README.md
