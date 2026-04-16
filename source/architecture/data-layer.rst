===========
Data Layer
===========

OpenRMF OSS uses MongoDB as its primary data store, with separate logical databases
for different bounded contexts. Keycloak uses PostgreSQL for identity data. All
databases run as containers with persistent volumes.

MongoDB Databases
=================

OpenRMF deploys multiple MongoDB instances (or databases within a shared instance)
to maintain separation between services in accordance with the microservices
architecture.

Artifacts Database
------------------

:Used By: openrmf-api-read, openrmf-api-save, openrmf-api-upload
:Collection: ``Artifacts``

Stores checklist records including:

- Raw CKL or XCCDF XML content
- Metadata: title, description, STIG type, hostname, host IP
- System Group ID (foreign key to the System Package)
- Created and updated timestamps
- User information (creator, last modifier)

This is the source of truth for all checklist data in the system.

Scores Database
---------------

:Used By: openrmf-msg-score, openrmf-api-scoring
:Collection: ``Scores``

Stores pre-computed scoring results for each checklist artifact. Each score record
contains:

- Artifact ID reference
- Counts by status: Open, Not a Finding, Not Applicable, Not Reviewed
- Counts by category: CAT I, CAT II, CAT III
- System Group ID for system-level score aggregation

Scores are written by the ``openrmf-msg-score`` messaging service whenever a
checklist is created, updated, or has a vulnerability edited.

Reports Database
----------------

:Used By: openrmf-msg-reports, openrmf-api-reports
:Collections: Nessus patch data, vulnerability data

Stores denormalized, query-optimized copies of checklist and scan data for
reporting. This database is populated through eventual consistency — the
``openrmf-msg-reports`` service subscribes to checklist and system events,
parses raw data, and inserts structured records.

Report data includes:

- Host-level vulnerability records parsed from CKL data
- Nessus plugin-level patch data parsed from ``.nessus`` files
- Aggregated vulnerability counts by status and severity

Administrators can trigger a full refresh of all report data through the
``openrmf.report.refresh.nessuspatchdata`` and
``openrmf.report.refresh.vulnerabilitydata`` NATS subjects.

Templates Database
------------------

:Used By: openrmf-api-template, openrmf-msg-template
:Collection: ``Templates``

Stores CKL checklist templates uploaded by administrators. Templates serve as the
structural skeleton that SCAP XCCDF scan results are matched against during import.
Each template includes:

- Template title (used for matching)
- Raw CKL XML content
- STIG type and version metadata

Audit Database
--------------

:Used By: openrmf-msg-audit, openrmf-api-audit
:Collection: ``Audits``

Write-once log of auditable events across the system. Records include:

- Event type (create, update, delete, login)
- Affected entity type and ID
- User who performed the action
- Timestamp
- Summary of the change

Default Credentials
===================

.. warning::

   The default MongoDB credentials are intended for initial setup only. Change them
   immediately in production deployments. See :doc:`/security/hardening`.

The default MongoDB user configured in the Docker Compose files:

- **Username**: ``openrmf``
- **Password**: ``openrmf1234!``
- **Permissions**: ``readWriteAnyDatabase``
- **Auth Source**: ``admin``

Connection string pattern::

   mongodb://openrmf:openrmf1234!@<hostname>/openrmf?authSource=admin

PostgreSQL (Keycloak)
=====================

Keycloak uses a PostgreSQL 16 database for storing realm configuration, user
accounts, roles, sessions, and client registrations. This database is managed
entirely by Keycloak and should not be modified directly.

The PostgreSQL container is configured in the Docker Compose file with default
credentials that should be changed after initial setup.

Persistent Volumes
==================

All databases use Docker named volumes for data persistence. On Linux systems, these
volumes reside under ``/var/lib/docker/volumes/`` (Docker) or the equivalent Podman
storage path.

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Volume
     - Service
     - Contents
   * - MongoDB data volume
     - openrmf-mongo
     - All checklist, score, report, template, and audit data
   * - PostgreSQL data volume
     - openrmf-postgres
     - Keycloak identity data
   * - Prometheus data volume
     - openrmf-prometheus
     - Metrics time-series data
   * - Grafana data volume
     - openrmf-grafana
     - Dashboard definitions and user preferences

Backup and Restore
==================

To back up MongoDB data, use ``mongodump`` against the running container::

   docker exec openrmf-mongo mongodump --archive=/tmp/backup.archive --gzip \
       -u openrmf -p 'openrmf1234!' --authenticationDatabase admin

   docker cp openrmf-mongo:/tmp/backup.archive ./openrmf-backup.archive

To restore::

   docker cp ./openrmf-backup.archive openrmf-mongo:/tmp/backup.archive

   docker exec openrmf-mongo mongorestore --archive=/tmp/backup.archive --gzip \
       -u openrmf -p 'openrmf1234!' --authenticationDatabase admin
