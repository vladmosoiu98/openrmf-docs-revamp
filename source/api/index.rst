=============
API Reference
=============

OpenRMF OSS exposes nine RESTful API services, each running as an independent
container. All APIs are built with C# / .NET Core and follow consistent patterns
for authentication, error handling, and documentation.

Accessing API Documentation
===========================

Every API service exposes a Swagger/OpenAPI specification at its ``/swagger/``
endpoint. In a running deployment, these are accessible through the NGINX reverse
proxy at paths like::

   http://<host>:8080/api/read/swagger/
   http://<host>:8080/api/save/swagger/
   http://<host>:8080/api/template/swagger/
   ...

Authentication
==============

All API calls (except Swagger endpoints) require a valid JWT bearer token issued by
Keycloak. The token must be included in the ``Authorization`` header::

   Authorization: Bearer <jwt-token>

Tokens are obtained through the OpenID Connect flow managed by Keycloak. The web
frontend handles this automatically. For direct API testing, obtain a token from
Keycloak's token endpoint::

   POST http://<host>:8080/auth/realms/openrmf/protocol/openid-connect/token
   Content-Type: application/x-www-form-urlencoded

   grant_type=password&client_id=openrmf&username=<user>&password=<pass>

Role-based authorization is enforced at the API level. See :doc:`/security/rbac` for
role definitions.

API Service Summary
===================

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Service
     - Operations
     - Description
   * - :doc:`read-api`
     - Read
     - Checklist retrieval, export, system listing, document generation
   * - :doc:`save-api`
     - Write
     - Artifact and system CRUD operations, vulnerability editing
   * - :doc:`upload-api`
     - Write
     - CKL and SCAP file upload processing
   * - :doc:`template-api`
     - Read/Write
     - Checklist template management
   * - :doc:`scoring-api`
     - Read
     - STIG checklist scoring (stored and on-the-fly)
   * - :doc:`controls-api`
     - Read
     - NIST 800-53 control lookups
   * - :doc:`compliance-api`
     - Read
     - Compliance assessment against NIST baselines
   * - :doc:`audit-api`
     - Read
     - Audit log queries (admin only)
   * - :doc:`reports-api`
     - Read
     - Pre-computed report data (Nessus, vulnerability)

Common Response Codes
=====================

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - Code
     - Meaning
   * - 200
     - Success. Response body contains the requested data.
   * - 400
     - Bad request. The request body or parameters are invalid.
   * - 401
     - Unauthorized. The JWT token is missing or expired.
   * - 403
     - Forbidden. The authenticated user lacks the required role.
   * - 404
     - Not found. The requested resource does not exist.
   * - 500
     - Internal server error. Check service logs for details.
