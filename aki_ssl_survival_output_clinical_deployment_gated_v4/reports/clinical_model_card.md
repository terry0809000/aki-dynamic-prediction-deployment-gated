# Severe AKI Dynamic Prediction - Clinical Research Model Card

Pipeline version: `2026-06-19-d-drive-publication-gated-v4`

## Intended Use
Retrospective research workflow for dynamic prediction of KDIGO stage 2/3 AKI or RRT after ICU admission using MIMIC-IV and eICU data. This notebook produces a deployment-gated research artifact. It must not be used for clinical care unless the deployment gate passes with institution-specific prospective shadow validation, locked thresholds, monitoring, incident response, regulatory review, and local governance approval.

## Outcome Definition
The notebook targets severe AKI/RRT after a 6-hour landmark and 6-hour actionability gap. KDIGO-compatible severe AKI is operationalized as creatinine >=2x baseline, creatinine >=4.0 mg/dL with acute rise when configured, urine output <0.5 mL/kg/h over 12h, urine output <0.3 mL/kg/h over 24h, or RRT initiation. Death and ICU discharge are handled as competing events.

## Major Limitations
- Retrospective EHR data can encode measurement frequency, treatment decisions, documentation practice, and site effects rather than kidney biology alone.
- Baseline creatinine is imperfect; admission fallback is flagged and audited.
- Race/ethnicity is coarse, inconsistently captured, and included only for audit/subgroup summaries, not as a predictor.
- Repeated landmark rows are correlated; reported CIs use cluster bootstrap but remain approximate.
- SHAP and PSM outputs are exploratory and must not be interpreted causally.

## Required Review Before Any Clinical Translation
1. TRIPOD+AI-complete manuscript/reporting package.
2. PROBAST+AI risk-of-bias assessment by independent reviewers.
3. External validation on the target institution with frozen preprocessing and thresholds.
4. Calibration-in-the-large, calibration slope, decision-curve and threshold utility review.
5. Subgroup review across age, sex, CKD, sepsis, ICU type, baseline-source, and race/ethnicity where available.
6. Prospective silent deployment with alert burden, workflow impact, and harm monitoring.

## Reference Anchors
- KDIGO 2012 AKI guideline: https://kdigo.org/guidelines/acute-kidney-injury/
- TRIPOD+AI: https://www.tripod-statement.org/
- EQUATOR TRIPOD+AI record: https://www.equator-network.org/reporting-guidelines/tripod-statement/
- PROBAST+AI publication: https://www.bmj.com/content/388/bmj-2024-082505
