=========
Changelog
=========

This page tracks significant changes across OpenRMF OSS releases. For detailed
release notes, see the
`GitHub Releases <https://github.com/Cingulara/openrmf-docs/releases>`_ page.

Version 1.9
============

- Migrated to Docker Compose v2 plugin syntax (``docker compose`` instead of
  ``docker-compose``)
- Upgraded Keycloak to 26.1.0
- Upgraded PostgreSQL to 16
- Unified service configuration under a single ``docker-compose.yml``
- All services accessible on a single port (8080)
- Podman and podman-compose fully supported with script conversion

Version 1.8
============

- Consolidated upload and save functionality into the Read API
- Added Nessus patch scan upload and reporting
- Added Risk Assessment Report (RAR) generation
- Introduced NATS client metrics exporter
- Architecture stabilized to the current microservices design

Earlier Versions
================

- **January 2019**: Architecture redesigned from monolith to microservices using
  .NET Core Web APIs, MongoDB, and NATS messaging with CQRS and eventual consistency.
- **2018**: Initial project creation as an RMF compliance management tool.

For the complete release history, visit the
`Releases page <https://github.com/Cingulara/openrmf-docs/releases>`_ on GitHub.
