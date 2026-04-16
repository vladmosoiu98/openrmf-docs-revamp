========
Glossary
========

.. glossary::
   :sorted:

   ATO
      Authority to Operate. A formal authorization granted by a senior official to
      operate an information system at an acceptable level of risk.

   ACAS
      Assured Compliance Assessment Solution. The DoD-mandated implementation of
      Nessus for vulnerability scanning.

   CCI
      Control Correlation Identifier. DISA-maintained identifiers that provide a
      bridge between NIST 800-53 controls and specific STIG requirements.

   CKL
      Checklist file format used by DISA STIG Viewer. OpenRMF imports and exports
      checklists in this XML-based format.

   CQRS
      Command Query Responsibility Segregation. An architectural pattern where read
      and write operations use separate models. OpenRMF applies this by using
      dedicated read APIs backed by eventually consistent report databases.

   DISA
      Defense Information Systems Agency. The DoD agency responsible for publishing
      STIGs and SCAP benchmarks.

   NATS
      A lightweight, high-performance messaging system used by OpenRMF for
      inter-service communication, supporting both publish/subscribe and
      request/reply patterns.

   NIST 800-53
      A catalog of security and privacy controls published by the National Institute
      of Standards and Technology. OpenRMF maps STIG findings to these controls for
      compliance reporting.

   OpenID Connect
      An identity layer on top of OAuth 2.0 used by Keycloak to provide
      authentication to OpenRMF.

   POA&M
      Plan of Action and Milestones. A document identifying security weaknesses,
      resources required to mitigate them, and milestones for completing corrective
      actions.

   RAR
      Risk Assessment Report. A document describing identified risks and their
      severity relative to the system.

   RBAC
      Role-Based Access Control. OpenRMF uses Keycloak roles to restrict UI features
      and API endpoints based on user assignments.

   RMF
      Risk Management Framework. The structured process used by the DoD and federal
      agencies to manage information security risk, defined in NIST SP 800-37.

   SCAP
      Security Content Automation Protocol. A suite of specifications for automating
      vulnerability management and compliance checking. OpenRMF processes SCAP XCCDF
      result files.

   SCC
      SCAP Compliance Checker. A DISA tool that performs automated SCAP scans against
      systems and produces XCCDF result files.

   STIG
      Security Technical Implementation Guide. Configuration standards published by
      DISA for securing information systems and software.

   System Package
      An OpenRMF organizational unit representing an ATO boundary. System Packages
      group checklists, SCAP scans, and patch scans for a single accreditation scope.

   XCCDF
      Extensible Configuration Checklist Description Format. An XML-based
      specification for writing security checklists and benchmarks. OpenRMF imports
      XCCDF result files from SCAP scans.
