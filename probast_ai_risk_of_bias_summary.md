# PROBAST+AI-Oriented Risk-of-Bias Summary

This is a pragmatic self-audit to support peer review. It is not a substitute for independent PROBAST+AI assessment.

## Participants
Risk: moderate to high. Public ICU databases differ in time, geography, coding, hospital mix, and documentation. Adult ICU eligibility and exclusions were explicit, but prospective local representativeness is unproven.

Mitigation: strict cross-database validation, subgroup audit, baseline-source audit, and deployment gate requiring local prospective validation.

## Predictors
Risk: moderate to high. EHR measurements encode observation intensity, clinician concern, treatment decisions, and documentation workflows.

Mitigation: actionability gap, pre-landmark feature timing, treatment/documentation ablations, measurement-process ablations, and exclusion of race/ethnicity from model predictors.

## Outcome
Risk: moderate. Severe AKI/RRT is clinically meaningful but baseline creatinine and urine-output documentation are imperfect.

Mitigation: KDIGO-compatible phenotype, baseline-source indicators, urine-output observability requirement, early severe AKI/RRT exclusion, and baseline-source subgroup reporting.

## Analysis
Risk: moderate. Row-level dynamic landmarks produce correlated observations and may inflate apparent precision.

Mitigation: cluster-bootstrap confidence intervals, first-landmark-per-stay sensitivity, external validation, calibration reporting, and explicit claim guardrails.

## Overall Judgment
The retrospective research workflow is publication-ready as a transportability and governance study. It is not clinically deployable until local prospective shadow validation, threshold approval, monitoring, incident response, regulatory review, governance approval, and human-factors signoff are completed.
