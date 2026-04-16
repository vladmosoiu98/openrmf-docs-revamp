============
Controls API
============

:Repository: `Cingulara/openrmf-api-controls <https://github.com/Cingulara/openrmf-api-controls>`_
:Container: ``cingulara/openrmf-api-controls``
:Internal Port: 8080

The Controls API is a read-only lookup service for NIST 800-53 security controls. It
provides control family, title, description, and supplemental guidance for each
control identifier.

This service is used by the Compliance API and the web frontend to resolve control
identifiers into human-readable information. It does not use a database — control
data is embedded in the service.

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
     - Returns the full list of NIST 800-53 controls.
   * - GET
     - ``/{controlId}``
     - Returns details for a specific control (e.g., ``AC-1``, ``IA-2``).

NATS Integration
================

The service also responds to NATS request/reply on:

- ``openrmf.controls`` — returns the full control list
- ``openrmf.controls.search`` — returns a single control by identifier
