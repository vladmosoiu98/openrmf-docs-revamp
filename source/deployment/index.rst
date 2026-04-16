==========
Deployment
==========

OpenRMF OSS runs entirely in OCI-compliant containers and supports several
deployment methods:

- **Docker Compose** (recommended for development and small-scale deployments)
- **Podman with podman-compose** (rootless alternative to Docker)
- **Kubernetes with Helm** (for production and scaled deployments)
- **Air-gapped installations** (for disconnected environments)

All deployment methods use the same container images published to Docker Hub under
the ``cingulara`` organization.

Before deploying, review the :doc:`/minimum-requirements` page to ensure your host
meets the hardware and software prerequisites.

.. toctree::
   :maxdepth: 1

   docker-compose
   kubernetes
   airgapped
   https
   upgrading
