# Prospective Shadow Validation Protocol

DRAFT_NOT_APPROVED_FOR_CLINICAL_USE

## Objective
Estimate local, prospective, silent-mode performance before any clinical use. The model must run with frozen preprocessing, frozen feature definitions, no clinician-visible alerts, and no retraining on the target hospital data during the evaluation window.

## Primary Endpoint
Severe AKI/RRT within 72 hours after an eligible landmark, with the configured actionability gap and exclusion rules. Death and ICU discharge should be reported as competing outcomes rather than ignored.

## Required Analyses
Report AUROC, AUPRC, Brier score, ECE, calibration intercept, calibration slope, threshold sensitivity/specificity/PPV/NPV, alert rate, decision-curve or net-benefit analysis if possible, first-landmark-per-stay sensitivity, and subgroup performance. Use patient/stay-level clustered confidence intervals because repeated landmark rows are correlated.

## Pass/Review Criteria
Minimum statistical review requires n >= 1000, sensitivity >= 0.70, alert rate <= 0.25, ECE <= 0.05, no unacceptable subgroup failure, and governance acceptance. These criteria do not replace clinician judgment or regulatory review.
