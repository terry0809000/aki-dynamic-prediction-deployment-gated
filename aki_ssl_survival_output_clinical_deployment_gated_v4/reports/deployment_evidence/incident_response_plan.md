# Incident Response Plan

DRAFT_NOT_APPROVED_FOR_CLINICAL_USE

## Scope
This plan covers silent-mode data failures, erroneous predictions, suspected patient-safety events, excessive alert burden, calibration drift, EHR feed interruptions, and any clinician-facing misunderstanding if the model later enters controlled deployment.

## Immediate Actions
1. Disable clinician-facing alerts or hold go-live if patient safety may be affected.
2. Preserve model inputs, prediction logs, threshold version, mapping version, and relevant EHR audit logs.
3. Notify the clinical owner, technical owner, patient-safety owner, and governance chair.
4. Triage whether the issue is data mapping, model drift, threshold misuse, interface design, or clinical workflow mismatch.

## Review and Rollback
A rollback decision must be available at all times. Reinstatement requires documented root-cause analysis, regression testing on recent local data, calibration/threshold review, and governance signoff. Serious events require institutional patient-safety reporting according to local policy.
