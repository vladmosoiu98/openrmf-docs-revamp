====================
Minimum Requirements
====================

OpenRMF OSS runs entirely in containers, so the primary requirement is a compatible
container runtime. This page details the hardware and software prerequisites for a
successful deployment.

Software Requirements
=====================

Container Runtime
-----------------

One of the following container runtimes is required:

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Runtime
     - Minimum Version
     - Notes
   * - Docker
     - 20.10.7
     - Must include the ``docker-compose-plugin`` (v2 syntax)
   * - Podman
     - 4.2.0
     - Requires ``podman-compose`` 1.0.3 or later

On Linux systems, ensure the ``docker-compose-plugin`` is included when installing or
updating Docker through ``apt-get`` or ``yum``.

On Windows 10 and macOS, Docker Desktop bundles all required executables. WSL
(Windows Subsystem for Linux) is supported, with CPU and memory constraints
configured at the host level.

Operating System
----------------

Any OS capable of running Docker or Podman containers is supported. This includes
Linux distributions (Ubuntu, RHEL, CentOS, Fedora), Windows 10+ with Docker
Desktop or WSL, and macOS with Docker Desktop.

.. warning::

   ARM-based chipsets (Apple Silicon, Raspberry Pi) may not run the OpenRMF stack
   correctly due to how the container images are built. AMD/Intel x86_64
   architectures are recommended.

Hardware Requirements
=====================

.. list-table::
   :header-rows: 1
   :widths: 25 25 50

   * - Resource
     - Minimum
     - Notes
   * - CPU
     - 6 cores
     - Dedicated to the container runtime
   * - RAM
     - 8 GB
     - Allocated to the container runtime
   * - Swap
     - 1 GB
     - Recommended for Docker Desktop configurations
   * - Disk
     - 40 GB
     - Accommodates container images and data growth over time

Storage Considerations
----------------------

On Linux systems, persistent volumes for MongoDB, Keycloak (PostgreSQL), Prometheus,
and Grafana are stored under the ``/var`` partition. With a minimum of 20 GB
allocated to ``/var``, expect approximately 60% usage with a baseline OpenRMF OSS
deployment before significant data ingestion.

Network Requirements
====================

OpenRMF OSS exposes its services on a single port:

- **HTTP**: port ``8080`` (default)
- **HTTPS**: port ``8443`` (when TLS is configured)

This port must be available on the host, not occupied by another service, and not
blocked by a firewall if external access is required. All microservices communicate
internally through Docker networking; only the NGINX reverse proxy port is exposed to
the host.

Browser Requirements
====================

OpenRMF OSS is tested against modern evergreen browsers:

- Google Chrome (recommended)
- Microsoft Edge
- Mozilla Firefox
- Safari
- Internet Explorer 11 (limited support)
