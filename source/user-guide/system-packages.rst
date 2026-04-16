===============
System Packages
===============

A **System Package** is the primary organizational unit in OpenRMF OSS. It represents
an Authority to Operate (ATO) boundary or accreditation scope — a logical grouping
of all checklists, SCAP scans, and Nessus patch scans for a single system under
assessment.

Creating a System Package
=========================

1. Log in to OpenRMF.
2. Navigate to the System Packages area from the main dashboard.
3. Click **Create New System Package**.
4. Enter a title and optional description.
5. Click **Save**.

The System Package dashboard becomes available immediately after creation.

System Package Dashboard
=========================

The dashboard shows an overview of all assessment data within the package:

- Total number of checklists uploaded
- Aggregate scoring across all checklists (Open, Not a Finding, Not Applicable, Not
  Reviewed counts)
- CAT I / CAT II / CAT III breakdown
- Compliance status (if a compliance check has been run)
- Last compliance check timestamp
- Nessus patch scan summary (if patch scans have been uploaded)

Managing System Packages
=========================

**Renaming**: Edit the system title from the dashboard. When renamed, the
``openrmf.system.update.{Id}`` NATS event propagates the change to all checklist
references.

**Deleting**: Deleting a System Package removes it and all associated checklists,
scores, and report data. This action publishes the ``openrmf.system.delete`` event.

.. warning::

   Deleting a System Package is irreversible. All associated data (checklists,
   scores, reports) is permanently removed.
