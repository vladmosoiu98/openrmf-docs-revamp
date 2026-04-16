==========
Kubernetes
==========

OpenRMF OSS can be deployed on Kubernetes using Helm charts provided in the
``openrmf-docs`` repository under the ``deployments/`` directory.

Prerequisites
=============

- A running Kubernetes cluster (1.19+)
- ``kubectl`` configured to communicate with the cluster
- Helm 3 installed
- Persistent volume provisioner available in the cluster

Deployment Overview
===================

The Kubernetes deployment creates the same set of services as the Docker Compose
deployment but as Kubernetes Deployments, Services, and ConfigMaps. Key
considerations for Kubernetes:

- Each microservice runs as a separate Deployment with its own Pod specification
- MongoDB, PostgreSQL, NATS, Prometheus, and Grafana use StatefulSets or Deployments
  with PersistentVolumeClaims
- An Ingress resource exposes the NGINX frontend (replacing the Docker host port
  mapping)
- Keycloak configuration is managed through ConfigMaps and environment variables

Helm Chart Structure
====================

The Helm chart is located in the ``deployments/chart/`` directory of the
``openrmf-docs`` repository. It includes:

- ``values.yaml`` — configurable parameters (image tags, resource limits, Keycloak
  settings, storage sizes)
- Templates for Deployments, Services, ConfigMaps, PersistentVolumeClaims, and
  Ingress resources

Configuration
=============

Edit ``values.yaml`` to set:

- **Image tags**: pin specific versions of each service
- **Resource limits**: CPU and memory requests/limits per service
- **Storage**: persistent volume sizes for MongoDB, PostgreSQL, Prometheus, Grafana
- **Keycloak**: realm URL, client ID, admin credentials
- **Ingress**: hostname, TLS certificate, annotations for your ingress controller
- **NATS**: connection URL and cluster configuration

.. note::

   Prometheus and Grafana configuration for Kubernetes differs from the Docker
   Compose deployment. The Docker Compose stack bundles Prometheus and Grafana
   behind the ``/metrics/`` path on the NGINX proxy. In Kubernetes, you may prefer
   to use your cluster's existing monitoring stack (e.g., kube-prometheus-stack).

Post-Deployment
===============

After deploying the Helm chart:

1. Configure Keycloak following the same steps as the Docker Compose deployment
   (:doc:`docker-compose`, Steps 4-6), using the Kubernetes service URL for
   Keycloak.
2. Create users and assign roles.
3. Access OpenRMF through the configured Ingress hostname.
