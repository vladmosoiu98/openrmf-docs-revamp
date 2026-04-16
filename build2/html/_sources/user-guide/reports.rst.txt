=======
Reports
=======

OpenRMF OSS provides several reporting capabilities, from interactive dashboards to
downloadable compliance documents.

Interactive Reports
===================

**Vulnerability Report**
   Displays all vulnerabilities across checklists in a System Package, filterable by
   status (Open, Not a Finding, Not Applicable, Not Reviewed) and severity (CAT I,
   CAT II, CAT III).

**Nessus Patch Report**
   Shows patch vulnerability data from uploaded Nessus ``.nessus`` files, organized
   by host and plugin. Indicates severity levels and patch availability.

**Compliance Dashboard**
   After running a compliance check, displays the implementation status of NIST
   800-53 controls across the selected baseline (low, moderate, high).

Generated Documents
===================

These documents are generated on demand and downloaded as files:

**POA&M (Plan of Action and Milestones)**
   Lists all Open findings with their severity, affected hosts, and NIST control
   mapping. Exported via the Read API's ``/system/{id}/poamexport`` endpoint.

**Test Plan Summary**
   Summarizes the assessment activities and results. Exported via
   ``/system/{id}/testplanexport``.

**Risk Assessment Report (RAR)**
   Documents identified risks and their severity relative to the system. Exported via
   ``/system/{id}/rarexport``.

**Excel Exports**
   Individual checklists can be exported as color-coded XLSX files with vulnerability
   statuses highlighted by severity.

**CKL Downloads**
   Checklists can be downloaded in the standard DISA CKL format for use in STIG
   Viewer or other tools.

Nessus Patch Summary
====================

For System Packages with uploaded Nessus scan data, the patch summary provides:

- Total number of hosts scanned
- Patch vulnerability counts by severity
- Host-by-host breakdown of missing patches

Data Freshness
==============

Report data is populated through eventual consistency. There may be a brief delay
(typically sub-second) between uploading or editing data and seeing updated reports.
Administrators can force a full report refresh through the NATS administrative
commands described in :doc:`/architecture/messaging`.
