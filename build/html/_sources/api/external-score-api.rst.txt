===================
External Score API
===================

:Repository: `Cingulara/openrmf-ext-api-score <https://github.com/Cingulara/openrmf-ext-api-score>`_
:Container: ``cingulara/openrmf-ext-api-score``
:Language: C# (.NET Core)

The External Score API is a standalone scoring service that accepts STIG checklists
via HTTP POST and returns scoring results. Unlike the internal Scoring API, this
service does not require a full OpenRMF deployment — it operates independently
without MongoDB, NATS, or Keycloak dependencies.

Use Cases
=========

- CI/CD pipeline integration: score checklists as part of an automated build process
- External tooling: integrate STIG scoring into third-party applications
- Quick validation: score a checklist without importing it into OpenRMF

Usage
=====

Submit a CKL file as the request body via HTTP POST to the service endpoint. The
response contains the score breakdown by status and severity category.
