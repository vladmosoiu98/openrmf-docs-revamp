==========
SCAP Scans
==========

OpenRMF OSS can import SCAP (Security Content Automation Protocol) scan results in
XCCDF format, merging automated scan findings into STIG checklists.

What is SCAP Scanning?
======================

SCAP scanning automates the evaluation of system configurations against STIG
requirements. Tools like DISA's SCC (SCAP Compliance Checker) or OpenSCAP run
benchmarks against target systems and produce XCCDF result XML files containing
pass/fail results for each STIG rule.

OpenRMF processes these result files and merges the findings into checklist
artifacts, reducing the manual effort required to populate checklists.

Prerequisites
=============

Before importing SCAP results, you must upload the corresponding checklist
**template** for the STIG being scanned. The system uses the template to match scan
results to the correct checklist structure. See :doc:`/api/template-api` for details
on template management.

Without a matching template, SCAP imports may fail or produce incomplete results.

Importing SCAP Results
======================

1. Open a System Package dashboard.
2. Click **Upload SCAP Scan**.
3. Select one or more XCCDF ``.xml`` result files.
4. Click **Upload**.

The Upload API parses the XCCDF file, extracts the benchmark title, requests the
matching template via NATS (``openrmf.template.read``), and creates a checklist
artifact with the automated findings merged in.

Supported Formats
=================

- **DISA SCC XCCDF results**: XML files produced by the DISA SCAP Compliance Checker
- **OpenSCAP XCCDF results**: XML files produced by the OpenSCAP tool suite

Both produce standard XCCDF format results that OpenRMF can process.

After Import
============

Once imported, SCAP scan results appear as checklist artifacts in the System Package.
They can be viewed, edited, and exported like any other checklist. The automated
findings (pass/fail) populate the vulnerability statuses, while rules not covered by
the scan remain as Not Reviewed for manual assessment.
