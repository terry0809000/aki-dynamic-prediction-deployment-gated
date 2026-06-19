# Monitoring and Drift Plan

DRAFT_NOT_APPROVED_FOR_CLINICAL_USE

## Silent-Mode Monitoring Before Go-Live
Monitor case mix, variable missingness, urine-output coverage, baseline creatinine source, serum creatinine measurement frequency, treatment/documentation features, calibration, discrimination, threshold operating characteristics, subgroup performance, and alert burden. The prespecified primary horizon is 72 hours.

## Prospective Performance Guardrails
The local review should require sensitivity >= 0.70, alert rate <= 0.25, ECE <= 0.05, and clinically acceptable calibration slope/intercept at the locked threshold. These are minimum guardrails, not automatic approval rules.

## Drift Triggers
Pause or investigate if baseline-source mix changes materially, urine-output capture deteriorates, serum creatinine ordering frequency shifts, any subgroup shows clinically meaningful calibration drift, alert burden exceeds the locked threshold plan, the EHR mapping changes, RRT documentation changes, or observed event prevalence moves outside the validation envelope.

## Cadence
Daily technical feed checks during shadow validation; weekly clinical safety review during the first 8 weeks of any controlled deployment; monthly calibration and subgroup review thereafter; immediate review after EHR upgrades, ICU workflow changes, laboratory interface changes, or safety events.
