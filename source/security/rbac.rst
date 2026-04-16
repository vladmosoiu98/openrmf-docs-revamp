==========================
Role-Based Access Control
==========================

OpenRMF OSS uses Keycloak to implement role-based access control (RBAC) through
OpenID Connect. Both the web frontend and API services enforce role checks.

How RBAC Works
==============

1. Users authenticate through Keycloak and receive a JWT (JSON Web Token).
2. The JWT contains the user's assigned roles as claims.
3. The web frontend reads the JWT to show or hide UI elements based on roles.
4. API services validate the JWT on every request and check the role claims before
   processing the request.

Keycloak Realm and Client
=========================

OpenRMF uses the ``openrmf`` realm in Keycloak with an ``openrmf`` client. The realm
setup script (``setup-realm-linux.sh``) automatically configures:

- The client with the correct redirect URIs and protocol mappers
- Role definitions
- Token mappers to include roles in the JWT
- Password policies

Role Definitions
================

The following roles are configured by the realm setup script. Each role maps to
specific permissions within the application:

**Administrator**
   Full access to all features including audit logs, system management, user
   management, and the ability to trigger report refreshes.

**Assessor**
   Can upload, edit, and manage checklists and SCAP scans within assigned System
   Packages. Can view reports and download documents.

**Reader / Viewer**
   Read-only access to checklists, scores, and reports. Cannot modify data.

.. note::

   The exact role names and granularity are defined by the Keycloak realm setup
   script. Review the script in the ``openrmf-docs/keycloak/`` directory for the
   authoritative list of roles and their mappings.

API-Level Enforcement
=====================

Each API service validates the JWT bearer token on incoming requests. If the token
is missing, expired, or does not contain the required role, the API returns:

- **401 Unauthorized**: missing or invalid token
- **403 Forbidden**: valid token but insufficient role

The JWT validation configuration is set through environment variables:

- ``JWTAUTHORITY``: the Keycloak realm URL (e.g.,
  ``http://<host>:8080/auth/realms/openrmf``)
- ``JWTCLIENT``: the Keycloak client ID (``openrmf``)
