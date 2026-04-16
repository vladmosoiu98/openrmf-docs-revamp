==============
Keycloak Setup
==============

Keycloak provides identity and access management for OpenRMF OSS using OpenID
Connect. This page covers user management, role assignment, and realm configuration.

Accessing the Admin Console
===========================

1. Navigate to ``http://<your-ip>:8080/auth/`` (or ``https://...:8443/auth/`` if TLS
   is configured).
2. Click **Administration Console**.
3. Log in with the Keycloak admin credentials (initially set in ``docker-compose.yml``
   as ``KEYCLOAK_ADMIN`` and ``KEYCLOAK_ADMIN_PASSWORD``).
4. Switch to the **openrmf** realm using the dropdown in the upper left corner.

Creating Users
==============

1. Navigate to **Users** in the left sidebar.
2. Click **Add user**.
3. Fill in the required fields: username, email, first name, last name.
4. Click **Create**.
5. Go to the **Credentials** tab.
6. Set a password. Toggle **Temporary** to **OFF** to prevent a forced password change
   on first login.

Password Policy
===============

The ``openrmf`` realm enforces a password policy configured by the realm setup
script:

- Minimum length: 12 characters
- At least 2 uppercase letters
- At least 2 lowercase letters
- At least 2 digits
- At least 2 special characters

Assigning Roles
===============

Roles control access to UI features and API endpoints. To assign roles:

1. Navigate to **Users** → select a user.
2. Go to the **Role mappings** tab.
3. Select the ``openrmf`` client from the client roles dropdown.
4. Assign the appropriate roles from the available list.

Available roles are defined by the realm setup script and correspond to the
RBAC model described in :doc:`/security/rbac`.

Creating Users Manually
========================

If the realm setup script is not used, users can be created entirely through the
Keycloak admin console. The ``create-users-by-hand.md`` file in the ``openrmf-docs``
repository provides step-by-step instructions for manual user creation with proper
role assignments.
