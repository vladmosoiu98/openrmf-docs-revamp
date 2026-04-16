============
Template API
============

:Repository: `Cingulara/openrmf-api-template <https://github.com/Cingulara/openrmf-api-template>`_
:Container: ``cingulara/openrmf-api-template``
:Internal Port: 8080
:Database: MongoDB (``Templates`` collection)

The Template API manages STIG checklist templates. Templates provide the structural
skeleton that SCAP XCCDF scan results are matched against during import. Without a
matching template, SCAP scan results cannot be processed into checklists.

Endpoints
=========

.. list-table::
   :header-rows: 1
   :widths: 10 30 60

   * - Method
     - Path
     - Description
   * - GET
     - ``/``
     - Lists all available checklist templates with metadata.
   * - GET
     - ``/template/{id}``
     - Retrieves a specific template by ID.
   * - POST
     - ``/``
     - Uploads a CKL file as a new template. The file is parsed and stored with
       its title, STIG type, and version metadata.

Template Matching
=================

When SCAP XCCDF results are uploaded through the Upload API, the system extracts the
benchmark title from the XML and uses the ``openrmf.template.read`` NATS subject to
request a matching template from ``openrmf-msg-template``. If a match is found, the
template's checklist structure is used as the base, and scan results are merged into
the vulnerability entries. If no match is found, the upload may fail or produce an
incomplete checklist.

Administrators should upload templates for every STIG type that will be scanned via
SCAP before importing scan results.
