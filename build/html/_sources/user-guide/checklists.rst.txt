==========
Checklists
==========

Checklists are the core data objects in OpenRMF OSS. Each checklist represents a DISA
STIG assessment for a specific technology on a specific host.

Uploading Checklists
====================

1. Open a System Package dashboard.
2. Click **Upload Checklist**.
3. Select one or more ``.ckl`` files from your file system.
4. Click **Upload**.

The uploaded checklists are parsed, stored in MongoDB, and trigger NATS events for
scoring and report generation. The system dashboard updates to reflect the new data.

Viewing Checklists
==================

Click on any checklist in the System Package to view its contents:

- **Checklist metadata**: STIG type, version, hostname, host IP, host MAC
- **Vulnerability listing**: each STIG rule with its ID, title, severity (CAT I/II/III),
  and current status (Open, Not a Finding, Not Applicable, Not Reviewed)
- **Finding details**: for each vulnerability, view the discussion, check content, fix
  text, and any comments or finding details entered by the assessor

Editing Checklists
==================

OpenRMF allows live editing of checklist data in the browser:

1. Open a checklist.
2. Click on a vulnerability entry.
3. Update the status, finding details, or comments.
4. Click **Save**.

Each edit publishes the ``openrmf.checklist.save.vulnerability.update`` event,
which triggers re-scoring and report updates.

Bulk Vulnerability Editing
==========================

For checklists of the same STIG type, OpenRMF supports bulk editing:

1. Select multiple checklists of the same type within a System Package.
2. Choose the vulnerability to update.
3. Set the new status and finding details.
4. Apply the change across all selected checklists.

This is useful when a finding applies uniformly across multiple hosts running the
same technology.

Downloading Checklists
======================

Checklists can be downloaded in two formats:

- **CKL format**: the standard DISA STIG Viewer format, suitable for import into
  STIG Viewer or other tools.
- **XLSX format**: a color-coded Excel export with vulnerabilities highlighted by
  severity and status.

Upgrading Checklists
====================

When DISA releases a new version of a STIG, existing checklists can be upgraded:

1. Open the checklist to upgrade.
2. Click **Upgrade Checklist**.
3. Select the target STIG version.
4. The system maps existing vulnerability statuses and finding details to the new
   version where the rules match. New rules added in the STIG update appear as
   Not Reviewed.

Vulnerability Delta Detection
===============================

OpenRMF can detect differences in vulnerability findings across checklists within
a System Package. This helps identify inconsistencies where the same rule has
different statuses on different hosts.
