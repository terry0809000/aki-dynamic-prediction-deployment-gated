# Threshold Locking Protocol

DRAFT_NOT_APPROVED_FOR_CLINICAL_USE

## Current Position
No clinical threshold is locked. The retrospective 72-hour external model did not meet the aspirational AUROC >= 0.80 guardrail, and the evaluated retrospective thresholds did not establish a deployable alert policy.

## Locking Process
Threshold selection must occur after local prospective shadow validation. The lock decision should consider sensitivity, PPV, alert rate, calibration, subgroup performance, staffing capacity, intended action pathway, and patient-safety review. The selected threshold must be entered in locked_thresholds.csv with review_status=approved only after governance approval.

## Change Control
Any threshold change after approval requires versioning, justification, retrospective replay on recent local data, prospective silent recheck if material, and governance signoff.
