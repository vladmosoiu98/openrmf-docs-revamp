==============
Compliance API
==============

:Repository: `Cingulara/openrmf-api-compliance <https://github.com/Cingulara/openrmf-api-compliance>`_
:Container: ``cingulara/openrmf-api-compliance``
:Internal Port: 8080

The Compliance API evaluates checklists against NIST 800-53 major controls and
reports the implementation status of each control. It bridges the gap between
individual STIG vulnerability findings and the RMF control framework.

How Compliance Mapping Works
============================

1. The API retrieves all checklists for a System Package via the
   ``openrmf.system.checklists.read`` NATS subject.
2. For each vulnerability in each checklist, the CCI (Control Correlation Identifier)
   is extracted and mapped to its parent NIST 800-53 control using the
   ``openrmf.compliance.cci`` and ``openrmf.compliance.cci.control`` NATS subjects.
3. The status of each vulnerability (Open, Not a Finding, Not Applicable, Not
   Reviewed) is aggregated at the control level.
4. Controls are filtered by the requested baseline (low, moderate, or high) with an
   optional PII overlay.

The result is a control-by-control compliance summary showing how many findings are
open, closed, or unreviewed for each NIST control applicable to the selected
baseline.

NATS Subjects
=============

**Requests Made:**

- ``openrmf.system.checklists.read`` — fetches all checklists for a system
- ``openrmf.compliance.cci`` — full CCI-to-control mapping
- ``openrmf.compliance.cci.control`` — CCI items for a specific control

**Events Published:**

- ``openrmf.system.compliance`` — records the timestamp of the compliance check on
  the system record
