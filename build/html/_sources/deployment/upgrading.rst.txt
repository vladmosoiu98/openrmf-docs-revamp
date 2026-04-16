=========
Upgrading
=========

This page covers upgrading between OpenRMF OSS versions.

General Upgrade Process
=======================

1. **Back up your data**: Use ``mongodump`` to back up MongoDB data and snapshot
   your ``docker-compose.yml``, ``.env``, and Keycloak configuration.

2. **Stop the stack**::

      ./stop.sh

3. **Pull the latest repository**::

      cd openrmf-docs
      git pull origin master

4. **Pull updated container images**: The ``start.sh`` script automatically pulls
   the latest images specified in ``docker-compose.yml``.

5. **Start the stack**::

      ./start.sh

6. **Clear browser cache**: After upgrading, clear your browser cache to ensure the
   web frontend loads the latest JavaScript and CSS assets.

Upgrading from v1.8.x to v1.9+
================================

Version 1.9 introduced several breaking changes:

**Docker Compose v2 Syntax**
   The ``docker-compose`` standalone command was replaced with the ``docker compose``
   plugin syntax. All scripts in v1.9+ use ``docker compose`` (space, not hyphen).
   Ensure you have the ``docker-compose-plugin`` installed.

**Keycloak Reconfiguration**
   Keycloak was upgraded to version 26.1.0. After upgrading, re-run the realm setup
   script and reconfigure redirect URIs as described in :doc:`docker-compose` Steps
   4-5.

**PostgreSQL 16**
   Keycloak's backing database was upgraded to PostgreSQL 16. If upgrading from an
   older PostgreSQL version, follow the PostgreSQL migration steps in the
   ``postgres-16-upgrade.md`` file in the ``openrmf-docs`` repository.

**Unified YML Configuration**
   All services now operate on a single port (8080) with a unified
   ``docker-compose.yml`` configuration.

Rollback
========

If an upgrade fails:

1. Stop the stack: ``./stop.sh``
2. Check out the previous version of ``openrmf-docs``:
   ``git checkout <previous-tag>``
3. Restore the MongoDB backup if data was migrated
4. Start the stack: ``./start.sh``
