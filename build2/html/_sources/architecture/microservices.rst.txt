=======================
Microservices Reference
=======================

OpenRMF OSS comprises 22 repositories under the ``Cingulara`` GitHub organization.
This page catalogs each service, its purpose, tech stack, and role in the overall
architecture.

API Services
============

These services expose RESTful HTTP endpoints consumed by the web frontend through
the NGINX reverse proxy. All API services are built with C# / .NET Core and expose
Swagger documentation at their ``/swagger/`` path.

openrmf-api-read
----------------

:Repository: `Cingulara/openrmf-api-read <https://github.com/Cingulara/openrmf-api-read>`_
:Language: C# (.NET Core)
:Database: MongoDB (``Artifacts`` collection)
:Purpose: Primary read-side API for checklist data retrieval and export.

As of version 1.8, this service also handles CKL/XML uploads, checklist saving, and
system package management (consolidating functionality that was previously split
across the upload and save APIs).

**Key Endpoints:**

.. list-table::
   :header-rows: 1
   :widths: 15 35 50

   * - Method
     - Path
     - Description
   * - GET
     - ``/``
     - List all checklist artifact records
   * - GET
     - ``/artifact/{id}``
     - Retrieve a single checklist by ID
   * - GET
     - ``/download/{id}``
     - Download a checklist in CKL format
   * - GET
     - ``/export/{id}``
     - Export a checklist as color-coded XLSX
   * - GET
     - ``/{id}/control/{control}``
     - Get vulnerability IDs mapped to a NIST control
   * - GET
     - ``/systems``
     - List all System Packages
   * - GET
     - ``/system/{systemGroupId}``
     - Get details for a specific System Package
   * - GET
     - ``/systems/{systemGroupId}``
     - List all checklists within a System Package
   * - GET
     - ``/system/{systemGroupId}/downloadnessus``
     - Download Nessus results for a system
   * - GET
     - ``/system/{systemGroupId}/exportnessus``
     - Export Nessus data
   * - GET
     - ``/system/{systemGroupId}/nessuspatchsummary``
     - Generate Nessus patch summary
   * - GET
     - ``/system/{systemGroupId}/testplanexport``
     - Export Test Plan summary
   * - GET
     - ``/system/{systemGroupId}/poamexport``
     - Export POA&M document
   * - GET
     - ``/system/{systemGroupId}/rarexport``
     - Export Risk Assessment Report
   * - GET
     - ``/count/artifacts``
     - Count total checklist artifacts
   * - GET
     - ``/count/systems``
     - Count total System Packages

**NATS Subjects Used (Request/Reply):**

- ``openrmf.score.read`` — retrieve scores for XLSX downloads
- ``openrmf.compliance.cci.control`` — control-based vulnerability mapping
- ``openrmf.scores.system`` — multi-checklist system scores
- ``openrmf.compliance.cci`` — CCI item enumeration

openrmf-api-save
-----------------

:Repository: `Cingulara/openrmf-api-save <https://github.com/Cingulara/openrmf-api-save>`_
:Language: C# (.NET Core)
:Database: MongoDB (``Artifacts`` collection)
:Purpose: Write-side API for creating, updating, and deleting artifacts and systems.

**Key Endpoints:**

.. list-table::
   :header-rows: 1
   :widths: 15 45 40

   * - Method
     - Path
     - Description
   * - POST
     - ``/``
     - Create a new artifact record
   * - PUT
     - ``/artifact/{id}``
     - Update an existing artifact
   * - PUT
     - ``/artifact/{artifactId}/vulnid/{vulnid}``
     - Update a specific vulnerability within a checklist
   * - POST
     - ``/upgradechecklist/system/{systemGroupId}/artifact/{artifactId}``
     - Upgrade a checklist to a newer STIG version
   * - DELETE
     - ``/artifact/{id}``
     - Delete an artifact
   * - DELETE
     - ``/system/{id}``
     - Delete a system and all its artifacts
   * - DELETE
     - ``/system/{id}/artifacts``
     - Delete selected artifacts within a system
   * - POST
     - ``/system``
     - Create a new System Package
   * - PUT
     - ``/system/{systemGroupId}``
     - Update a System Package

**NATS Subjects Published:**

- ``openrmf.save.new`` — new artifact created
- ``openrmf.save.update`` — artifact updated
- ``openrmf.checklist.delete`` — artifact deleted
- ``openrmf.system.update.{Id}`` — system title changed
- ``openrmf.system.count.>`` — system checklist count changed
- ``openrmf.system.delete`` — system deleted
- ``openrmf.system.patchscan`` — patch scan data uploaded
- ``openrmf.checklist.save.vulnerability.update`` — individual vulnerability edited

openrmf-api-upload
------------------

:Repository: `Cingulara/openrmf-api-upload <https://github.com/Cingulara/openrmf-api-upload>`_
:Language: C# (.NET Core)
:Purpose: Handles CKL file uploads to initiate or append to STIG records.

**NATS Subjects Published:**

- ``openrmf.upload.new`` — new upload processed
- ``openrmf.upload.update`` — upload updated
- ``openrmf.checklist.save.new`` — triggers scoring and reporting
- ``openrmf.system.count.>`` — increments system checklist count

openrmf-api-template
--------------------

:Repository: `Cingulara/openrmf-api-template <https://github.com/Cingulara/openrmf-api-template>`_
:Language: C# (.NET Core)
:Database: MongoDB
:Purpose: Manages checklist file templates. Templates are used during SCAP XCCDF
   import to match scan results against the correct STIG checklist structure.

**Key Operations:**

- Upload a CKL file as a reusable template with metadata
- List all available templates
- Retrieve a specific template by ID or title

openrmf-api-scoring
--------------------

:Repository: `Cingulara/openrmf-api-scoring <https://github.com/Cingulara/openrmf-api-scoring>`_
:Language: C# (.NET Core)
:Database: MongoDB
:Purpose: Provides STIG vulnerability scoring. Can read stored scores from MongoDB
   or calculate scores on the fly from an uploaded checklist file.

Scores include counts of Open, Not a Finding, Not Applicable, and Not Reviewed
statuses, grouped by severity category (CAT I, CAT II, CAT III).

openrmf-api-controls
--------------------

:Repository: `Cingulara/openrmf-api-controls <https://github.com/Cingulara/openrmf-api-controls>`_
:Language: C# (.NET Core)
:Purpose: Read-only lookup service for NIST 800-53 security controls. Returns
   control family, title, and description. Used by the compliance APIs to map CCI
   items to their parent controls.

openrmf-api-compliance
----------------------

:Repository: `Cingulara/openrmf-api-compliance <https://github.com/Cingulara/openrmf-api-compliance>`_
:Language: C# (.NET Core)
:Purpose: Evaluates checklists against NIST 800-53 major controls and reports
   implementation status. Supports filtering by baseline (low, moderate, high) and
   PII overlay.

openrmf-api-audit
------------------

:Repository: `Cingulara/openrmf-api-audit <https://github.com/Cingulara/openrmf-api-audit>`_
:Language: C# (.NET Core)
:Database: MongoDB
:Purpose: Read-only query interface for audit records. Restricted to administrator
   users. Records are written by the ``openrmf-msg-audit`` messaging service.

openrmf-api-reports
-------------------

:Repository: `Cingulara/openrmf-api-reports <https://github.com/Cingulara/openrmf-api-reports>`_
:Language: C# (.NET Core)
:Database: MongoDB (eventually consistent report database)
:Purpose: Read-only API serving pre-computed report data including Nessus Patch
   Reports and Host Vulnerability reports. Data is populated by the
   ``openrmf-msg-reports`` messaging service through eventual consistency.


Messaging Services
==================

These services are NATS clients that subscribe to published messages or respond to
request/reply patterns. They handle asynchronous processing such as scoring,
compliance mapping, reporting, and audit logging.

openrmf-msg-score
------------------

:Repository: `Cingulara/openrmf-msg-score <https://github.com/Cingulara/openrmf-msg-score>`_
:Language: C# (.NET Core)
:Database: MongoDB
:Subscribes To: ``openrmf.checklist.save.new``, ``openrmf.checklist.save.update``,
   ``openrmf.checklist.delete``, ``openrmf.checklist.save.vulnerability.update``

Scores each checklist on save/update and persists the result to MongoDB. Removes
score records when checklists are deleted.

openrmf-msg-reports
-------------------

:Repository: `Cingulara/openrmf-msg-reports <https://github.com/Cingulara/openrmf-msg-reports>`_
:Language: C# (.NET Core)
:Database: MongoDB (report database)
:Subscribes To: ``openrmf.checklist.save.new``, ``openrmf.checklist.save.update``,
   ``openrmf.system.delete``, ``openrmf.system.patchscan``,
   ``openrmf.report.refresh.nessuspatchdata``,
   ``openrmf.report.refresh.vulnerabilitydata``,
   ``openrmf.checklist.save.vulnerability.update``

Parses raw checklist and Nessus data into denormalized structures optimized for
report queries. Supports administrator-triggered full refreshes of all report data.

openrmf-msg-system
-------------------

:Repository: `Cingulara/openrmf-msg-system <https://github.com/Cingulara/openrmf-msg-system>`_
:Language: C# (.NET Core)
:Database: MongoDB
:Subscribes To: ``openrmf.system.update.{Id}``, ``openrmf.system.count.>``,
   ``openrmf.system.compliance``
:Responds To: ``openrmf.checklist.read``, ``openrmf.system.checklists.read``

Maintains system-level metadata: updates checklist references when system titles
change, increments/decrements checklist counts, and records the timestamp of the
last compliance check.

openrmf-msg-compliance
-----------------------

:Repository: `Cingulara/openrmf-msg-compliance <https://github.com/Cingulara/openrmf-msg-compliance>`_
:Language: C# (.NET Core)
:Responds To: ``openrmf.compliance.cci``, ``openrmf.compliance.cci.control``,
   ``openrmf.compliance.cci.references``

Provides CCI-to-NIST-control mapping data on request. Supports queries for full CCI
listings, CCI items for a specific control, and CCI titles with NIST references.

openrmf-msg-controls
---------------------

:Repository: `Cingulara/openrmf-msg-controls <https://github.com/Cingulara/openrmf-msg-controls>`_
:Language: C# (.NET Core)
:Responds To: ``openrmf.controls``, ``openrmf.controls.search``

Returns the full list of RMF controls or looks up a specific control by identifier
(e.g., ``AC-1``).

openrmf-msg-template
---------------------

:Repository: `Cingulara/openrmf-msg-template <https://github.com/Cingulara/openrmf-msg-template>`_
:Language: C# (.NET Core)
:Database: MongoDB
:Responds To: ``openrmf.template.read``

Returns template checklist data by title. Used during SCAP XCCDF import to match
scan results to the appropriate STIG checklist structure.

openrmf-msg-audit
------------------

:Repository: `Cingulara/openrmf-msg-audit <https://github.com/Cingulara/openrmf-msg-audit>`_
:Language: C# (.NET Core)
:Database: MongoDB
:Subscribes To: All ``openrmf.audit.*`` subjects

Records auditable events (checklist uploads, edits, deletes, system changes) into
the audit database. Data is queried through the ``openrmf-api-audit`` service.

openrmf-msg-checklist
---------------------

:Repository: `Cingulara/openrmf-msg-checklist <https://github.com/Cingulara/openrmf-msg-checklist>`_
:Language: C# (.NET Core)
:Responds To: Checklist/artifact information requests via NATS

Returns checklist and artifact information to other services that need it for
processing.


Web Frontend
============

openrmf-web
------------

:Repository: `Cingulara/openrmf-web <https://github.com/Cingulara/openrmf-web>`_
:Languages: JavaScript (84.8%), HTML (9.0%), CSS (5.7%), SCSS (0.4%)
:Purpose: Browser-based UI for all OpenRMF functionality.

Built on the Pike Admin Bootstrap 4 theme, the frontend is served as static files
by NGINX. All API calls are routed through the NGINX reverse proxy to the backend
microservices. The web application integrates with Keycloak for OpenID Connect
authentication.

The ``/help/`` section of the site is generated using Jekyll (``bundle exec jekyll
build`` from the ``./help/`` directory) and bundled into the NGINX container.


Supporting Repositories
=======================

openrmf-docs
-------------

:Repository: `Cingulara/openrmf-docs <https://github.com/Cingulara/openrmf-docs>`_
:Purpose: Documentation, deployment scripts (Docker Compose, Kubernetes Helm),
   database initialization, and Keycloak configuration files.

openrmf-at-aws
--------------

:Repository: `Cingulara/openrmf-at-aws <https://github.com/Cingulara/openrmf-at-aws>`_
:Language: Shell
:Purpose: Terraform and Ansible scripts for provisioning OpenRMF on AWS
   infrastructure.

openrmf-ext-api-score
---------------------

:Repository: `Cingulara/openrmf-ext-api-score <https://github.com/Cingulara/openrmf-ext-api-score>`_
:Language: C# (.NET Core)
:Purpose: External-facing scoring API that accepts STIG checklists via HTTP POST
   and returns scores without requiring a full OpenRMF deployment.

openrmf-io
-----------

:Repository: `Cingulara/openrmf-io <https://github.com/Cingulara/openrmf-io>`_
:Language: JavaScript
:Purpose: Source code for the openrmf.io website.
