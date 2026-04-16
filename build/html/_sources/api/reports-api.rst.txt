===========
Reports API
===========

:Repository: `Cingulara/openrmf-api-reports <https://github.com/Cingulara/openrmf-api-reports>`_
:Container: ``cingulara/openrmf-api-reports``
:Internal Port: 8080
:Database: MongoDB (report database, eventually consistent)

The Reports API serves pre-computed report data that has been denormalized and
optimized for query performance. Data is populated by the ``openrmf-msg-reports``
messaging service through eventual consistency — when checklists or scans are
uploaded or modified, the messaging service processes the raw data and inserts
structured records into the report database.

Available Reports
=================

**Nessus Patch Report**
   Plugin-level patch vulnerability data parsed from uploaded ``.nessus`` files.
   Shows which hosts are affected by which vulnerabilities, severity levels, and
   patch availability.

**Host Vulnerability Report**
   Host-by-host breakdown of vulnerability findings across all checklists in a
   System Package.

**Vulnerability Summary**
   Aggregated counts of Open, Not a Finding, Not Applicable, and Not Reviewed
   findings by severity category and checklist type.

Data Freshness
==============

Because the Reports API uses eventually consistent data, there may be a brief delay
between when a checklist is uploaded/modified and when the updated data appears in
reports. The delay depends on NATS message processing time and MongoDB write
performance, but is typically sub-second under normal load.

Administrators can force a full refresh of all report data by publishing to:

- ``openrmf.report.refresh.nessuspatchdata`` — rebuilds all Nessus patch reports
- ``openrmf.report.refresh.vulnerabilitydata`` — rebuilds all vulnerability reports
