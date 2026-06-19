# Local Data Mapping Specification

DRAFT_NOT_APPROVED_FOR_CLINICAL_USE

## Required Mappings
Map local EHR data to the notebook variable ontology before prospective validation: serum creatinine, urine output, RRT, weight, ICU admission/discharge times, death time, creatinine baseline source, vasopressors, diuretics, nephrotoxins, antibiotics, mechanical ventilation, vitals, blood gases, chemistry, hematology, comorbidities, ICU type, and demographics needed for audit.

## Unit and Timing Checks
Verify units for creatinine, urine output, weight, temperature, blood gases, and medication timestamps. All predictors must be available before the prediction landmark plus actionability-gap logic. Outcome labels must not leak post-landmark information into features.

## Measurement Bias Checks
Before validation, summarize serum creatinine ordering frequency, urine-output coverage, missingness, medication documentation, and RRT documentation by service line and ICU type. These summaries must be reviewed as possible measurement-process bias, not merely data quality noise.
