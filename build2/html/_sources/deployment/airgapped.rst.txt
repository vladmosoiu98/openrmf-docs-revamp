========================
Air-Gapped Installation
========================

OpenRMF OSS can be installed in disconnected (air-gapped) environments where the
host has no access to Docker Hub or the public internet.

Overview
========

The process involves:

1. Downloading all container images on a connected machine
2. Saving them to a portable medium (USB drive, DVD, network share)
3. Loading the images into the container runtime on the air-gapped host
4. Running the standard deployment scripts

Step 1: Pull Images on a Connected Machine
============================================

On a machine with internet access and Docker installed, pull all OpenRMF images::

   docker pull cingulara/openrmf-web:<version>
   docker pull cingulara/openrmf-api-read:<version>
   docker pull cingulara/openrmf-api-save:<version>
   docker pull cingulara/openrmf-api-upload:<version>
   docker pull cingulara/openrmf-api-template:<version>
   docker pull cingulara/openrmf-api-scoring:<version>
   docker pull cingulara/openrmf-api-controls:<version>
   docker pull cingulara/openrmf-api-compliance:<version>
   docker pull cingulara/openrmf-api-audit:<version>
   docker pull cingulara/openrmf-api-reports:<version>
   docker pull cingulara/openrmf-msg-score:<version>
   docker pull cingulara/openrmf-msg-reports:<version>
   docker pull cingulara/openrmf-msg-system:<version>
   docker pull cingulara/openrmf-msg-audit:<version>
   docker pull cingulara/openrmf-msg-compliance:<version>
   docker pull cingulara/openrmf-msg-controls:<version>
   docker pull cingulara/openrmf-msg-template:<version>
   docker pull cingulara/openrmf-msg-checklist:<version>
   docker pull nats:2
   docker pull mongo:6
   docker pull postgres:16
   docker pull quay.io/keycloak/keycloak:26.1.0
   docker pull prom/prometheus:v2.55.0
   docker pull grafana/grafana:10.0.0

Replace ``<version>`` with the target OpenRMF release tag (e.g., ``1.9.02``).

Step 2: Save Images to Archive
================================

::

   docker save -o openrmf-images.tar \
       cingulara/openrmf-web:<version> \
       cingulara/openrmf-api-read:<version> \
       ... (all images listed above)

Step 3: Transfer to Air-Gapped Host
=====================================

Copy ``openrmf-images.tar`` and the ``openrmf-docs`` repository to the air-gapped
host via USB drive, DVD, or approved transfer mechanism.

Step 4: Load Images
====================

On the air-gapped host::

   docker load -i openrmf-images.tar

For Podman::

   podman load -i openrmf-images.tar

Step 5: Deploy
===============

Follow the standard :doc:`docker-compose` deployment steps starting from Step 2
(Configure the Environment). The ``start.sh`` script will use the locally loaded
images instead of pulling from Docker Hub.
