========
Save API
========

:Repository: `Cingulara/openrmf-api-save <https://github.com/Cingulara/openrmf-api-save>`_
:Container: ``cingulara/openrmf-api-save``
:Internal Port: 8080
:Database: MongoDB (``Artifacts`` collection)

The Save API handles all write operations for artifacts and System Packages. It is
responsible for creating, updating, and deleting checklist records, managing system
metadata, and publishing NATS events that trigger downstream processing (scoring,
reporting, auditing).

Endpoints
=========

Artifact CRUD
-------------

.. list-table::
   :header-rows: 1
   :widths: 10 50 40

   * - Method
     - Path
     - Description
   * - POST
     - ``/``
     - Creates a new artifact record from submitted form data.
   * - PUT
     - ``/artifact/{id}``
     - Updates an existing artifact record.
   * - PUT
     - ``/artifact/{artifactId}/vulnid/{vulnid}``
     - Updates a specific vulnerability within a checklist. Publishes the
       ``openrmf.checklist.save.vulnerability.update`` event.
   * - DELETE
     - ``/artifact/{id}``
     - Deletes a single artifact. Publishes ``openrmf.checklist.delete`` and
       decrements the system checklist count.
   * - DELETE
     - ``/system/{id}/artifacts``
     - Deletes one or more artifacts within a system by ID list.

Checklist Upgrade
-----------------

.. list-table::
   :header-rows: 1
   :widths: 10 55 35

   * - Method
     - Path
     - Description
   * - POST
     - ``/upgradechecklist/system/{systemGroupId}/artifact/{artifactId}``
     - Upgrades a checklist to a newer STIG version. The existing vulnerability
       statuses are preserved and mapped to the new version where applicable.

System Package CRUD
-------------------

.. list-table::
   :header-rows: 1
   :widths: 10 35 55

   * - Method
     - Path
     - Description
   * - POST
     - ``/system``
     - Creates a new System Package.
   * - PUT
     - ``/system/{systemGroupId}``
     - Updates system metadata (title, description). Publishes
       ``openrmf.system.update.{Id}`` to propagate the change.
   * - DELETE
     - ``/system/{id}``
     - Deletes a system and all its artifacts. Publishes ``openrmf.system.delete``.

NATS Events Published
=====================

The Save API is one of the primary event publishers in the system:

- ``openrmf.save.new`` — a new artifact was created
- ``openrmf.save.update`` — an artifact was updated
- ``openrmf.checklist.delete`` — an artifact was deleted
- ``openrmf.system.update.{Id}`` — a system's title was changed
- ``openrmf.system.count.>`` — a system's checklist count changed
- ``openrmf.system.delete`` — a system was deleted
- ``openrmf.system.patchscan`` — Nessus patch scan data was uploaded
- ``openrmf.checklist.save.vulnerability.update`` — an individual vulnerability was
  edited
