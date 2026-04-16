==========
Upload API
==========

:Repository: `Cingulara/openrmf-api-upload <https://github.com/Cingulara/openrmf-api-upload>`_
:Container: ``cingulara/openrmf-api-upload``
:Internal Port: 8080

The Upload API processes incoming CKL checklist files and SCAP XCCDF XML result
files. When a file is uploaded, the service parses it, stores the artifact record,
and publishes NATS events that trigger scoring and reporting workflows.

Supported File Formats
======================

- **CKL files**: DISA STIG Viewer checklist format. Uploaded directly and stored as
  artifact records.
- **SCAP XCCDF XML files**: Result files from DISA SCC or OpenSCAP scans. During
  processing, the Upload API uses the ``openrmf.template.read`` NATS subject to
  match the scan results against a stored template, then merges the findings into
  a checklist artifact.

NATS Events Published
=====================

- ``openrmf.checklist.save.new`` — a new checklist was uploaded (triggers scoring
  and report generation)
- ``openrmf.checklist.save.update`` — an existing checklist was re-uploaded with
  new data
- ``openrmf.upload.new`` — new upload event for audit tracking
- ``openrmf.upload.update`` — upload update event
- ``openrmf.system.count.>`` — increments the checklist count for the target system

NATS Requests Made
==================

- ``openrmf.template.read`` — requests a template checklist by title from
  ``openrmf-msg-template`` for XCCDF import matching
