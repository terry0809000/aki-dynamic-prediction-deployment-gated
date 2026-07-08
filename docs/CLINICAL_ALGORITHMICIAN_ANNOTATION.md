# Senior Clinical Algorithmician Annotation

## Clinical Algorithmic Frame

Repository: [Deployment-gated severe AKI dynamic prediction workflow](https://github.com/terry0809000/aki-dynamic-prediction-deployment-gated)

Domain: severe AKI/RRT dynamic prediction.

Intended research use: retrospective deployment-gated model selection, calibration review, and prospective-shadow-validation planning.

Explicit non-use: renal replacement therapy initiation, nephrology consult triggers, medication dosing, fluid orders, or bedside alerting.

Primary analytic signal: dynamic ICU landmarks, severe AKI/RRT endpoints, no-treatment feature sets, calibration, subgroup audit, and deployment evidence reports.

Primary validation claim: 72-hour strict external validation with leakage-aware model selection and blocked deployment gate.

Deployment gate: BLOCKED_NOT_CLINICALLY_DEPLOYABLE; the package is designed to expose that gate rather than bypass it.

## Algorithmic Interpretation

This repository should be read as a clinical algorithm research package, not
as a deployable medical device. The model outputs are risk estimates or text
labels conditioned on the data-generating process used in the study. They are
not causal effects, treatment rules, or substitutes for clinician judgement.

The clinically important question is not only whether discrimination is high.
A senior review must ask whether the cohort definition is stable, whether the
outcome is observable before downstream care changes it, whether features are
available at the stated decision time, whether missingness reflects illness or
documentation practice, and whether calibration survives source shift.

## Minimum Evidence Standard

- Cohort construction must be locked before model selection.
- Feature availability must be anchored to the stated prediction time.
- Patient, stay, site, or state-week clustering must be respected in splits
  and uncertainty estimates.
- AUROC must be interpreted with AUPRC, Brier score, calibration-in-the-large,
  calibration slope/intercept, expected/observed ratios, and threshold burden.
- External or temporal validation must be labelled according to the actual
  data source and split design.
- Recalibration must be distinguished from frozen external validation.
- Explanation methods are diagnostic descriptions of the fitted model, not
  biological or clinical causality.

## Operational Guardrails

A real-world implementation would require a local feature map, data-refresh
checks, locked thresholds, subgroup and drift monitoring, incident response,
audit logs, model versioning, clinical owner signoff, and a prospective
silent-trial period. The package is therefore intentionally conservative:
where evidence is retrospective, sparse, poorly calibrated, or source-shifted,
the correct algorithmic state is blocked or research-only.

## Reviewer Checklist

- Does the README identify the intended use and the non-use cases?
- Can a reviewer run repository validation without credentialed data?
- Are raw datasets and patient-level derivatives absent from Git?
- Are local workstation paths removed from public files?
- Is Zenodo metadata present for citable public release?
- Are deployment claims separated from retrospective modelling results?
