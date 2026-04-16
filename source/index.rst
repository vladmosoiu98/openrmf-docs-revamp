.. OpenRMF OSS documentation master file

=======================================
OpenRMF OSS Documentation
=======================================

OpenRMF\ :sup:`®` OSS is an open-source, web-based platform for managing DoD STIG
checklists, DISA/OpenSCAP/Nessus SCAP scans, and Nessus/ACAS patch data. It
generates NIST compliance reports, Plans of Action and Milestones (POA&M), Risk
Assessment Reports (RAR), and Test Plan summaries from a single browser-based
interface.

The project is built on a microservices architecture using .NET Core, MongoDB,
NATS messaging, NGINX, and Keycloak, deployed through Docker Compose or
Kubernetes.

.. note::

   This documentation targets developers and contributors working with the
   OpenRMF OSS codebase. It covers architecture, API surface, deployment,
   development workflows, security, and observability.

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   overview
   minimum-requirements
   glossary

.. toctree::
   :maxdepth: 3
   :caption: Architecture

   architecture/index

.. toctree::
   :maxdepth: 3
   :caption: API Reference

   api/index
   api/read-api
   api/save-api
   api/upload-api
   api/template-api
   api/scoring-api
   api/controls-api
   api/compliance-api
   api/audit-api
   api/reports-api
   api/external-score-api

.. toctree::
   :maxdepth: 3
   :caption: Deployment

   deployment/index

.. toctree::
   :maxdepth: 3
   :caption: Developer Guide

   developer/index

.. toctree::
   :maxdepth: 3
   :caption: User Guide

   user-guide/index

.. toctree::
   :maxdepth: 3
   :caption: Security

   security/index

.. toctree::
   :maxdepth: 3
   :caption: Observability

   observability/index

.. toctree::
   :maxdepth: 2
   :caption: Reference

   reference/software-bom
   reference/nats-subjects
   reference/environment-variables
   reference/changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
