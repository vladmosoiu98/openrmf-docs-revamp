=====================
Security Hardening
=====================

After initial deployment, several hardening steps should be performed to secure the
OpenRMF OSS stack for production use.

.. warning::

   Make a backup of your configuration before performing any of these changes.

Change Default Keycloak Admin Credentials
==========================================

1. Log in to the Keycloak admin console.
2. Change the admin password.
3. Remove the ``KEYCLOAK_ADMIN`` and ``KEYCLOAK_ADMIN_PASSWORD`` environment
   variables from ``docker-compose.yml``. Keycloak persists the credentials
   internally after first use.

Change Default MongoDB Credentials
=====================================

1. Connect to the MongoDB instance and change the root user password.
2. Store the new credentials securely.
3. Remove ``MONGO_INITDB_ROOT_USERNAME`` and ``MONGO_INITDB_ROOT_PASSWORD`` from
   ``docker-compose.yml``.
4. Update the ``DBCONNECTION`` environment variable in all API and messaging service
   definitions to use the new credentials.

Change Default Grafana Credentials
====================================

1. Log in to Grafana and change the admin password.
2. Remove ``GF_SECURITY_ADMIN_PASSWORD`` from the ``.grafana`` configuration file.
   Grafana persists the password internally.

Change Default PostgreSQL Credentials
========================================

1. Update the PostgreSQL password for the Keycloak database.
2. Update the corresponding environment variables in the Keycloak and PostgreSQL
   service definitions in ``docker-compose.yml``.

Enable HTTPS
=============

For production deployments, enable TLS as described in
:doc:`/deployment/https`. This encrypts all traffic between browsers
and the NGINX reverse proxy, including authentication tokens and checklist data.

Network Segmentation
====================

In the default Docker Compose configuration, all services communicate on a single
Docker bridge network. For enhanced security:

- Do not expose MongoDB, PostgreSQL, or NATS ports to the host (they only need to be
  accessible within the Docker network).
- Only expose the NGINX proxy port (8080 or 8443) to the host network.
- Use firewall rules to restrict access to the host port.

Container Image Verification
=============================

OpenRMF container images are published to Docker Hub under the ``cingulara``
organization. Verify image integrity by checking the image digests against published
release notes.

Log Monitoring
==============

Monitor container logs for security-relevant events:

- Failed authentication attempts (Keycloak logs)
- Unauthorized API access (401/403 responses in API logs)
- Unusual data access patterns (audit log entries)

Use ``docker compose logs -f <service-name>`` to stream logs from specific services.
