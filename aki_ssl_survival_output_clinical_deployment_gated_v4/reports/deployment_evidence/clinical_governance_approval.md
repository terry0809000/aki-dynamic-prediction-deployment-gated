# Clinical Governance Approval

DRAFT_NOT_APPROVED_FOR_CLINICAL_USE

## Required Decision
A local clinical AI, patient-safety, ICU, nephrology, informatics, privacy, and quality-governance body must make an explicit go/no-go decision before any non-silent use. Retrospective MIMIC/eICU performance does not satisfy this approval.

## Minimum Evidence for Review
- Prospective silent-mode validation at the target hospital with at least 1000 eligible prediction rows and enough outcome events for stable calibration review.
- Locked threshold row for the 72-hour horizon.
- Calibration-in-the-large, calibration slope, ECE, Brier score, AUROC, AUPRC, PPV, sensitivity, specificity, NPV, and alert burden.
- Subgroup review by age, sex, CKD, sepsis, ICU type, baseline creatinine source, race/ethnicity where legally and ethically available, and missingness/measurement-frequency strata.
- Human-factors simulation showing that clinicians understand that SHAP/PSM outputs are exploratory and non-causal.

## Local Signoff Fields
Committee name: TBD.
Clinical owner: TBD.
Technical owner: TBD.
Patient-safety owner: TBD.
Decision date: TBD.
Decision: not approved.
Review cadence: TBD.
