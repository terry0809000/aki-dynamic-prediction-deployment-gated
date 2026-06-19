# Model Selection and Claims Report

Pipeline version: `2026-06-19-d-drive-publication-gated-v4`
Experiment setting: `reports_only`
Primary horizon: `72` hours
Status: **NO_AUROC_0_80_EXTERNAL_CANDIDATE_FOUND**

## Selected Best External Row
- `prefix`: cpu_xgb_eicu_to_mimic_no_treatment_external
- `metric_family`: landmark_row
- `source_file`: cpu_xgb_eicu_to_mimic_no_treatment_external_metrics.csv
- `horizon_hours`: 72
- `n`: 354387
- `events`: 51270
- `auc`: 0.7634218798070919
- `auc_ci_low`: 0.7584045532944561
- `auc_ci_high`: 0.7734970569105212
- `auprc`: 0.3330339383747896
- `brier`: 0.112353715976316
- `ece`: 0.0323251905764347
- `calibration_intercept`: -0.4086782226638267
- `calibration_slope`: 0.8934144845613792

## Claim Guardrails
- Best external AUROC at 72h is 0.763, below the aspirational 0.80 threshold.
- Selected AUROC is landmark-row based; pair it with stay-level metrics because repeated landmarks are correlated.

## Files
- All candidate metrics: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\all_candidate_metrics_for_selection.csv`
- External ranking: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\external_metric_ranking_primary_horizon.csv`

