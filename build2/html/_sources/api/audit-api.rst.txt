=========
Audit API
=========

:Repository: `Cingulara/openrmf-api-audit <https://github.com/Cingulara/openrmf-api-audit>`_
:Container: ``cingulara/openrmf-api-audit``
:Internal Port: 8080
:Database: MongoDB (``Audits`` collection)

The Audit API provides a read-only query interface for audit records. Access is
restricted to users with the administrator role in Keycloak.

Audit records are written by the ``openrmf-msg-audit`` messaging service, which
subscribes to auditable events across the system. The Audit API simply queries and
returns these records — it does not write to the database.

Typical Audit Events
====================

- Checklist uploaded, updated, or deleted
- System Package created, renamed, or deleted
- Vulnerability status changed
- SCAP scan results imported
- Nessus patch scan uploaded
- User login events (via Keycloak integration)
