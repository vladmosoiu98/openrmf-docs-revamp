==========================
NATS Subject Reference
==========================

This page provides a complete reference of all NATS subjects used in OpenRMF OSS.
For architectural context, see :doc:`/architecture/messaging`.

Request/Reply Subjects
======================

.. list-table::
   :header-rows: 1
   :widths: 35 20 20 25

   * - Subject
     - Requester(s)
     - Responder
     - Payload
   * - ``openrmf.checklist.read``
     - Score API, Compliance API
     - msg-system
     - Full artifact record by ID
   * - ``openrmf.system.checklists.read``
     - Compliance API, Read API
     - msg-system
     - All checklists for a system
   * - ``openrmf.compliance.cci``
     - Compliance API
     - msg-compliance
     - Full CCI-to-NIST mapping
   * - ``openrmf.compliance.cci.control``
     - Read API, Compliance API
     - msg-compliance
     - CCI items for a control
   * - ``openrmf.compliance.cci.references``
     - Compliance API
     - msg-compliance
     - CCI titles + NIST refs
   * - ``openrmf.controls``
     - Various APIs
     - msg-controls
     - Full control list
   * - ``openrmf.controls.search``
     - Various APIs
     - msg-controls
     - Single control by ID
   * - ``openrmf.template.read``
     - Upload API
     - msg-template
     - Template by title
   * - ``openrmf.score.read``
     - Read API
     - msg-score
     - Score data for export

Publish/Subscribe Subjects
===========================

Checklist Events
----------------

.. list-table::
   :header-rows: 1
   :widths: 40 20 40

   * - Subject
     - Publisher
     - Subscriber(s)
   * - ``openrmf.checklist.save.new``
     - Upload API
     - msg-score, msg-reports
   * - ``openrmf.checklist.save.update``
     - Upload API
     - msg-score, msg-reports
   * - ``openrmf.checklist.delete``
     - Save API
     - msg-score
   * - ``openrmf.checklist.save.vulnerability.update``
     - Save API
     - msg-reports, msg-score

System Events
-------------

.. list-table::
   :header-rows: 1
   :widths: 40 20 40

   * - Subject
     - Publisher
     - Subscriber(s)
   * - ``openrmf.system.update.{Id}``
     - Save API
     - msg-system
   * - ``openrmf.system.count.>``
     - Upload API, Save API
     - msg-system
   * - ``openrmf.system.compliance``
     - Compliance API
     - msg-system
   * - ``openrmf.system.delete``
     - Save API
     - msg-reports
   * - ``openrmf.system.patchscan``
     - Save API
     - msg-reports

Administrative Commands
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 45 20 35

   * - Subject
     - Publisher
     - Subscriber(s)
   * - ``openrmf.report.refresh.nessuspatchdata``
     - Admin action
     - msg-reports
   * - ``openrmf.report.refresh.vulnerabilitydata``
     - Admin action
     - msg-reports

Other Events
------------

.. list-table::
   :header-rows: 1
   :widths: 40 20 40

   * - Subject
     - Publisher
     - Subscriber(s)
   * - ``openrmf.save.new``
     - Save API
     - (audit tracking)
   * - ``openrmf.save.update``
     - Save API
     - (audit tracking)
   * - ``openrmf.upload.new``
     - Upload API
     - (audit tracking)
   * - ``openrmf.upload.update``
     - Upload API
     - (audit tracking)
