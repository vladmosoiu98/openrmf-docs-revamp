========
Overview
========

What is OpenRMF OSS?
====================

OpenRMF\ :sup:`®` OSS (Open Risk Management Framework, Open Source Software) is a
web-based application for managing, viewing, and reporting on DoD STIG checklists,
SCAP scans, and Nessus patch scans. It provides a centralized interface that replaces
the traditionally manual and fragmented processes involved in Risk Management
Framework (RMF) compliance workflows.

The tool was created by Cingulara (now Soteria Software) and is released under the
GPL-3.0 license. It is free to use, deploy, and redistribute, though it may not be
sold commercially.

Core Capabilities
=================

OpenRMF OSS provides the following capabilities through a 100% browser-based
interface (Chrome, Edge, Firefox, Safari):

**Checklist Management**
   Upload, view, edit, and download DISA CKL checklist files directly in the browser.
   Checklists can be upgraded to newer STIG versions released by DISA.

**SCAP Scan Processing**
   Import SCAP XCCDF-format scan results from DISA SCC or OpenSCAP tools. Results
   are matched against checklist templates and merged into the compliance picture.

**Nessus/ACAS Patch Scanning**
   Upload Nessus ``.nessus`` scan files for patch vulnerability tracking. The system
   parses raw scan data and structures it for host-level and plugin-level reporting.

**Compliance Generation**
   Map STIG vulnerability IDs to NIST 800-53 controls and generate compliance status
   across low, moderate, and high baselines with PII overlay considerations.

**Document Generation**
   Automatically produce POA&M (Plan of Action and Milestones), Test Plan summaries,
   and Risk Assessment Reports (RAR) from the uploaded assessment data.

**Bulk Vulnerability Editing**
   Edit vulnerability statuses across multiple checklists of the same type
   simultaneously.

**Role-Based Access Control**
   UI features and API calls are gated by Keycloak-managed roles using OpenID
   Connect.

**Reporting**
   Interactive vulnerability reports, Nessus patch reports, compliance dashboards,
   and Excel exports for offline analysis.

How It Works
============

OpenRMF OSS organizes compliance artifacts around the concept of a **System
Package**, which represents an Authority to Operate (ATO) boundary or accreditation
scope. Within a System Package, users upload CKL checklists, SCAP scan results, and
Nessus patch scans. The platform aggregates this data and produces a unified view of
the system's security posture.

The application is deployed as a set of containerized microservices communicating
through NATS messaging and backed by MongoDB databases. NGINX serves the web
frontend, and Keycloak provides authentication and authorization.

Project History
===============

OpenRMF was initially conceived in 2018 as a tool to automate RMF compliance
tracking. In January 2019, the architecture was redesigned from a monolith to a
microservices-based system using web APIs, CQRS (Command Query Responsibility
Segregation), eventual consistency, MongoDB, and NATS messaging. This architecture
has remained stable from version 1.8 onward.

The project is maintained by the Cingulara / Tutela team and has an active community
communicating through GitHub issues and a Slack channel.

License
=======

OpenRMF OSS is released under the `GNU General Public License v3.0
<https://www.gnu.org/licenses/gpl-3.0.en.html>`_. You are free to use, modify, and
distribute the software, but you may not charge others to install or use it.

Related Projects
================

**OpenRMF Professional** is a commercial offering from Soteria Software that extends
the OSS edition with additional features including custom checklist templates, CIS
scan support, historical trending, enhanced POAM workflows, SSP/SAR/RAR/CCRI
document generation, and advanced vulnerability tracking.
