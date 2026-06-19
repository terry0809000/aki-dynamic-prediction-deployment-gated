# Human Factors Signoff

DRAFT_NOT_APPROVED_FOR_CLINICAL_USE

## Required Testing
Before any clinician-facing use, complete simulated ICU workflow testing with intended users. Include cases with missing urine output, admission-fallback baseline creatinine, CKD, sepsis, diuretic exposure, nephrotoxin exposure, RRT documentation edge cases, and repeated landmark predictions from the same stay.

## Comprehension Requirements
Users must understand that the score is a risk estimate, not a diagnosis or treatment instruction; repeated landmarks are correlated; retrospective external validation does not prove local transportability; and SHAP/PSM outputs are non-causal exploratory diagnostics.

## Alert-Burden Review
The local locked threshold must be reviewed against predicted daily alert volume, ICU staffing, escalation capacity, false-positive burden, and potential automation bias. If users cannot explain the action pathway and limitations, the model must remain silent.

## Signoff Fields
Simulation date: TBD.
Number and roles of participants: TBD.
Observed workflow failures: TBD.
Training materials approved: TBD.
Decision: not approved.
