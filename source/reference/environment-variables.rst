=====================
Environment Variables
=====================

This page documents the environment variables used to configure OpenRMF OSS services.
These are typically set in the ``docker-compose.yml`` file or in Kubernetes ConfigMaps.

Common Variables (All Services)
================================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``JWTAUTHORITY``
     - Keycloak realm URL for JWT token validation. Example:
       ``http://192.168.1.100:8080/auth/realms/openrmf``
   * - ``JWTCLIENT``
     - Keycloak client identifier. Typically ``openrmf``.
   * - ``NATSSERVERURL``
     - NATS server connection URL. Example: ``nats://natsserver:4222``

API Service Variables
=====================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``DBCONNECTION``
     - MongoDB connection string. Example:
       ``mongodb://openrmf:openrmf1234!@openrmf-mongo/openrmf?authSource=admin``
   * - ``DBTYPE``
     - Database type identifier used by the service.
   * - ``JAABORHOST``
     - Jaeger tracing agent host (optional). Example: ``jaeger:6831``

Keycloak Variables
==================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``KEYCLOAK_ADMIN``
     - Initial Keycloak administrator username. Remove after setup.
   * - ``KEYCLOAK_ADMIN_PASSWORD``
     - Initial Keycloak administrator password. Remove after setup.

MongoDB Variables
=================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``MONGO_INITDB_ROOT_USERNAME``
     - MongoDB root username for initial setup. Remove after setup.
   * - ``MONGO_INITDB_ROOT_PASSWORD``
     - MongoDB root password for initial setup. Remove after setup.

Grafana Variables
=================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``GF_SECURITY_ADMIN_PASSWORD``
     - Initial Grafana admin password. Stored in the ``.grafana`` file. Remove
       after changing the password through the Grafana UI.

NGINX / Web Frontend Variables
===============================

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Variable
     - Description
   * - ``SSL_VERIFY``
     - Set to ``false`` for self-signed certificates on the nginx-metrics container.

.env File
=========

The ``.env`` file in the ``scripts/`` directory is loaded by Docker Compose and
provides variables to the ``docker-compose.yml`` file. The primary variable to
configure is ``JWTAUTHORITY``, which must contain your host's IP address or DNS name.

.grafana File
=============

The ``.grafana`` file contains Grafana-specific environment variables, primarily the
admin password and the host URL for dashboard links.
