========
Read API
========

:Repository: `Cingulara/openrmf-api-read <https://github.com/Cingulara/openrmf-api-read>`_
:Container: ``cingulara/openrmf-api-read``
:Internal Port: 8080
:Database: MongoDB (``Artifacts`` collection)

The Read API is the primary data retrieval service in OpenRMF. It serves checklist
listings, individual checklist data, CKL downloads, Excel exports, system package
information, Nessus data, and generated compliance documents (POA&M, Test Plan,
RAR).

As of version 1.8, this service also handles CKL/XML uploads, checklist and system
package persistence, and compliance generation — consolidating functionality that was
previously distributed across the upload and save APIs.

Endpoints
=========

Artifact Operations
-------------------

.. list-table::
   :header-rows: 1
   :widths: 10 30 60

   * - Method
     - Path
     - Description
   * - GET
     - ``/``
     - Returns a list of all checklist artifact records with metadata. Does not
       include raw CKL/XML content.
   * - GET
     - ``/artifact/{id}``
     - Returns the full artifact record for a specific checklist, including its raw
       CKL/XML content and all metadata fields.
   * - GET
     - ``/download/{id}``
     - Returns the raw CKL file as a downloadable attachment with
       ``Content-Disposition: attachment``.
   * - GET
     - ``/export/{id}``
     - Generates and returns a color-coded Excel (XLSX) export of the checklist with
       vulnerability statuses highlighted by severity.
   * - GET
     - ``/{id}/control/{control}``
     - Returns vulnerability IDs within a checklist that map to the specified NIST
       800-53 control identifier.

System Operations
-----------------

.. list-table::
   :header-rows: 1
   :widths: 10 40 50

   * - Method
     - Path
     - Description
   * - GET
     - ``/systems``
     - Lists all System Packages with summary metadata.
   * - GET
     - ``/system/{systemGroupId}``
     - Returns details for a specific System Package.
   * - GET
     - ``/systems/{systemGroupId}``
     - Lists all checklist artifacts within a System Package.

Nessus Operations
-----------------

.. list-table::
   :header-rows: 1
   :widths: 10 50 40

   * - Method
     - Path
     - Description
   * - GET
     - ``/system/{systemGroupId}/downloadnessus``
     - Downloads raw Nessus results for a system.
   * - GET
     - ``/system/{systemGroupId}/exportnessus``
     - Exports Nessus data in a structured format.
   * - GET
     - ``/system/{systemGroupId}/nessuspatchsummary``
     - Generates a patch summary report from Nessus data.

Document Generation
-------------------

.. list-table::
   :header-rows: 1
   :widths: 10 50 40

   * - Method
     - Path
     - Description
   * - GET
     - ``/system/{systemGroupId}/testplanexport``
     - Generates and downloads a Test Plan summary document.
   * - GET
     - ``/system/{systemGroupId}/poamexport``
     - Generates and downloads a POA&M (Plan of Action & Milestones).
   * - GET
     - ``/system/{systemGroupId}/rarexport``
     - Generates and downloads a Risk Assessment Report.

Counts
------

.. list-table::
   :header-rows: 1
   :widths: 10 30 60

   * - Method
     - Path
     - Description
   * - GET
     - ``/count/artifacts``
     - Returns the total count of checklist artifacts across all systems.
   * - GET
     - ``/count/systems``
     - Returns the total count of System Packages.

NATS Integration
================

The Read API uses NATS request/reply to fetch data from messaging services:

- ``openrmf.score.read`` — Retrieves scoring data for XLSX export generation
- ``openrmf.compliance.cci.control`` — Maps NIST controls to CCI items for
  vulnerability filtering
- ``openrmf.scores.system`` — Fetches aggregated scores for all checklists in a
  system
- ``openrmf.compliance.cci`` — Enumerates CCI items for compliance document
  generation
