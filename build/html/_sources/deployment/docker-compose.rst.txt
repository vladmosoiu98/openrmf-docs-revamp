==============
Docker Compose
==============

This is the primary deployment method for OpenRMF OSS. The ``openrmf-docs``
repository contains the Docker Compose files, environment configuration, and
startup scripts.

Prerequisites
=============

- Docker 20.10.7 or later with the ``docker-compose-plugin`` (v2 syntax)
- Or Podman 4.2.0+ with ``podman-compose`` 1.0.3+
- 6 CPU cores, 8 GB RAM, 40 GB disk allocated to the container runtime
- Port 8080 available and not blocked by firewall
- File Sharing enabled (Docker Desktop users)

.. warning::

   Do **not** use ``localhost`` or ``127.0.0.1`` in configuration files. In
   container networking, these addresses refer to the container itself, not the
   host machine. Use your machine's actual IP address or DNS name.

Step 1: Clone the Repository
=============================

::

   git clone https://github.com/Cingulara/openrmf-docs.git
   cd openrmf-docs/scripts

Step 2: Configure the Environment
==================================

Edit the ``.env`` file and replace ``xxx.xxx.xxx.xxx`` with your machine's IP
address or DNS name::

   # .env
   JWTAUTHORITY=http://192.168.1.100:8080/auth/realms/openrmf
   JWTCLIENT=openrmf
   ...

Edit the ``.grafana`` file with the same IP address or DNS name.

Step 3: Start the Stack
========================

**Docker:**

::

   ./start.sh

**Podman:** Convert the scripts first, then start:

::

   sed -i "s|docker compose|podman-compose|g" *.sh
   ./start.sh

The script pulls all container images from Docker Hub and starts the services
defined in ``docker-compose.yml``. First-time startup may take several minutes
while images are downloaded.

Step 4: Configure Keycloak
===========================

Keycloak manages authentication and must be configured before users can log in.

**Run the realm setup script:**

::

   cd keycloak

   # For Podman, convert scripts first:
   # sed -i "s|docker |podman |g" *.sh

   ./setup-realm-linux.sh

The script prompts for:

1. Your machine's IP address or DNS name
2. An initial administrator username

It automatically configures the ``openrmf`` realm, roles, client settings, protocols,
and password policies.

Step 5: Configure Keycloak Redirect URIs
=========================================

1. Open ``http://<your-ip>:8080/auth/`` in a browser.
2. Click **Administration Console** and log in with the default admin credentials
   (found in the ``docker-compose.yml`` ``KEYCLOAK_ADMIN`` and
   ``KEYCLOAK_ADMIN_PASSWORD`` variables).
3. Switch from the ``master`` realm to the ``openrmf`` realm (dropdown in the upper
   left).
4. Navigate to **Clients** → **openrmf**.
5. In **Valid redirect URIs**, add: ``http://<your-ip>:8080/*``
6. In **Valid post logout redirect URIs**, add: ``http://<your-ip>:8080/*``
7. Click **Save**.

Step 6: Create and Configure Users
====================================

1. In the Keycloak admin console, navigate to **Users**.
2. Select the user created during the realm setup (Step 4).
3. Fill in the **Email**, **First Name**, and **Last Name** fields.
4. Go to the **Credentials** tab.
5. Set a password. Ensure the **Temporary** toggle is **OFF**.
6. Password requirements: minimum 12 characters with at least 2 uppercase, 2
   lowercase, 2 digits, and 2 special characters.

Step 7: Log In
===============

Navigate to ``http://<your-ip>:8080/`` and authenticate with the credentials
configured in Step 6.

Step 8: Begin Using OpenRMF
============================

1. Create a **System Package** (represents an ATO boundary).
2. Open the System Package dashboard.
3. Upload CKL checklist files or SCAP XCCDF XML result files.
4. View aggregated assessment results, scores, and compliance status.

Stopping and Restarting
========================

::

   # Stop all services
   ./stop.sh

   # Start all services
   ./start.sh

Data persists in Docker named volumes between restarts.

Service Composition
===================

The ``docker-compose.yml`` defines the following services:

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Service
     - Port
     - Description
   * - openrmf-web
     - 8080 (host)
     - NGINX reverse proxy + static frontend
   * - openrmf-api-read
     - 8080 (internal)
     - Read API
   * - openrmf-api-save
     - 8080 (internal)
     - Save API
   * - openrmf-api-upload
     - 8080 (internal)
     - Upload API
   * - openrmf-api-template
     - 8080 (internal)
     - Template API
   * - openrmf-api-scoring
     - 8080 (internal)
     - Scoring API
   * - openrmf-api-controls
     - 8080 (internal)
     - Controls API
   * - openrmf-api-compliance
     - 8080 (internal)
     - Compliance API
   * - openrmf-api-audit
     - 8080 (internal)
     - Audit API
   * - openrmf-api-reports
     - 8080 (internal)
     - Reports API
   * - openrmf-mongo
     - 27017 (internal)
     - MongoDB database
   * - nats
     - 4222 (internal)
     - NATS messaging server
   * - openrmf-keycloak
     - (via NGINX)
     - Keycloak identity provider
   * - openrmf-postgres
     - 5432 (internal)
     - PostgreSQL for Keycloak
   * - openrmf-prometheus
     - 9090 (internal)
     - Prometheus metrics
   * - openrmf-grafana
     - (via NGINX)
     - Grafana dashboards
   * - nats-client-metrics
     - 7778 (internal)
     - NATS client metrics exporter
   * - openrmf-msg-score
     - —
     - Score messaging service
   * - openrmf-msg-reports
     - —
     - Reports messaging service
   * - openrmf-msg-system
     - —
     - System messaging service
   * - openrmf-msg-audit
     - —
     - Audit messaging service
   * - openrmf-msg-compliance
     - —
     - Compliance messaging service
   * - openrmf-msg-controls
     - —
     - Controls messaging service
   * - openrmf-msg-template
     - —
     - Template messaging service
   * - openrmf-msg-checklist
     - —
     - Checklist messaging service
