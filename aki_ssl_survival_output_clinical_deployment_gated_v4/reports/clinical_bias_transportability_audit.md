# Clinical Risk, Bias, and Transportability Audit

Pipeline version: `2026-06-19-d-drive-publication-gated-v4`  
Generated from: `aki_ssl_survival_sectioned_workflow_clinical_deployment_gated_v4_d_drive_publication.ipynb`  
Primary horizon: 72 hours  
Deployment gate: **BLOCKED_NOT_CLINICALLY_DEPLOYABLE**

## Bottom Line

The best verified 72-hour external result was `cpu_xgb_eicu_to_mimic_no_treatment_external` with AUROC 0.763 (95% cluster bootstrap CI 0.758-0.773), AUPRC 0.333, Brier score 0.112, ECE 0.032, calibration intercept -0.409, and calibration slope 0.893. This does not meet the aspirational AUROC >=0.80 guardrail. The strongest short-horizon result was 0.803 at 12 hours for cpu_xgb_mimic_to_eicu_full_external, but this is not the prespecified primary horizon.

The deployment gate remains **BLOCKED_NOT_CLINICALLY_DEPLOYABLE** because local prospective shadow-mode metrics, locked thresholds, governance approval, monitoring, incident response, regulatory assessment, workflow documentation, and human-factors signoff were not supplied.

## Cohort and Landmark Construction

| Database | Base ICU stays | Baseline sCr available | Final cohort stays | Landmarks | Stays with landmarks | Missing UO exclusions | Severe AKI/RRT by 6h exclusions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MIMIC-IV | 50066 | 49611 | 49611 | 354387 | 42012 | 713 | 872 |
| eICU | 93830 | 81322 | 81322 | 581356 | 58427 | 17207 | 1105 |

## Primary External Model Selection at 72 Hours

| Candidate | AUROC | AUROC CI low | AUROC CI high | AUPRC | Brier | ECE | Events | Landmarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cpu_xgb_eicu_to_mimic_no_treatment_external | 0.763 | 0.758 | 0.773 | 0.333 | 0.112 | 0.032 | 51270 | 354387 |
| cpu_hgb_eicu_to_mimic_full_external | 0.763 | 0.758 | 0.773 | 0.329 | 0.111 | 0.032 | 51270 | 354387 |
| cpu_xgb_eicu_to_mimic_full_external | 0.762 | 0.758 | 0.772 | 0.326 | 0.113 | 0.040 | 51270 | 354387 |
| cpu_hgb_eicu_to_mimic_no_treatment_external | 0.762 | 0.758 | 0.773 | 0.326 | 0.112 | 0.026 | 51270 | 354387 |
| cpu_hgb_mimic_to_eicu_full_external | 0.752 | 0.747 | 0.765 | 0.240 | 0.068 | 0.007 | 47109 | 581356 |
| cpu_xgb_mimic_to_eicu_full_external | 0.752 | 0.745 | 0.763 | 0.236 | 0.069 | 0.006 | 47109 | 581356 |
| cpu_xgb_eicu_to_mimic_conservative_external | 0.749 | 0.743 | 0.759 | 0.322 | 0.112 | 0.023 | 51270 | 354387 |
| cpu_hgb_mimic_to_eicu_no_treatment_external | 0.749 | 0.745 | 0.762 | 0.231 | 0.069 | 0.007 | 47109 | 581356 |

## Repeated Correlated Landmark Risk

The selected model's landmark-row AUROC at 72 hours was 0.763, but first-eligible-landmark-per-stay AUROC was 0.712. This gap is clinically important and should prevent overinterpretation of row-level discrimination.

| Horizon h | Stays | Events | AUROC | AUPRC | Brier | ECE | Cal intercept | Cal slope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 42012 | 6813 | 0.724 | 0.309 | 0.126 | 0.032 | 0.046 | 0.855 |
| 24 | 42012 | 9380 | 0.715 | 0.389 | 0.158 | 0.037 | -0.047 | 0.808 |
| 48 | 42012 | 11438 | 0.712 | 0.447 | 0.179 | 0.039 | -0.052 | 0.804 |
| 72 | 42012 | 12212 | 0.712 | 0.474 | 0.185 | 0.036 | -0.058 | 0.813 |
| 168 | 42012 | 13030 | 0.715 | 0.501 | 0.190 | 0.033 | -0.019 | 0.863 |

## Treatment and Measurement-Process Confounding

Treatment/documentation ablation produced small AUROC changes at 72 hours, while removing measurement-process features produced larger drops. This suggests the model is not dominated by treatment variables, but surveillance/documentation intensity still contributes meaningful signal and remains a retrospective EHR bias risk.

| Direction | Full AUROC | No-treatment AUROC | No-measurement AUROC | Conservative AUROC | Full minus no-treatment | Full minus no-measurement |
| --- | --- | --- | --- | --- | --- | --- |
| mimic to eicu | 0.752 | 0.749 | 0.730 | 0.722 | 0.003 | 0.022 |
| eicu to mimic | 0.763 | 0.762 | 0.743 | 0.747 | 0.001 | 0.020 |

## Baseline Creatinine Sensitivity

Baseline-source performance differed. The selected model had AUROC 0.765 for prior baselines and AUROC 0.748 for early-admission fallback baselines at 72 hours.

| Baseline source | Landmarks | Events | AUROC | AUPRC | Brier | ECE | Cal intercept | Cal slope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| early_min_0_6h | 39160 | 7229 | 0.748 | 0.388 | 0.133 | 0.018 | -0.178 | 0.880 |
| prior | 315227 | 44041 | 0.765 | 0.325 | 0.110 | 0.036 | -0.443 | 0.895 |

## Threshold Operating Characteristics at 72 Hours

None of the evaluated thresholds simultaneously met sensitivity >=0.70 and alert rate <=0.25. A 0.20 threshold gave sensitivity 0.665 with alert rate 0.334; a 0.30 threshold reduced alert rate to 0.197 but sensitivity fell to 0.457.

| Threshold | Alert rate | Sensitivity | Specificity | PPV | NPV | Alerts |
| --- | --- | --- | --- | --- | --- | --- |
| 0.05 | 0.789 | 0.970 | 0.242 | 0.178 | 0.979 | 279626 |
| 0.10 | 0.576 | 0.884 | 0.476 | 0.222 | 0.960 | 204257 |
| 0.20 | 0.334 | 0.665 | 0.722 | 0.288 | 0.927 | 118197 |
| 0.30 | 0.197 | 0.457 | 0.847 | 0.336 | 0.902 | 69799 |

## Subgroup Audit at 72 Hours

Subgroup results are audit evidence only; they are not proof of fairness or local clinical safety. Several smaller race/ethnicity groups have unstable estimates and require local review before any clinical use.

| Subgroup | Level | Landmarks | Events | AUROC | AUPRC | ECE |
| --- | --- | --- | --- | --- | --- | --- |
| age_band | 65-79 | 113931 | 18297 | 0.737 | 0.327 | 0.042 |
| age_band | <65 | 182063 | 22109 | 0.781 | 0.324 | 0.033 |
| age_band | >=80 | 58393 | 10864 | 0.745 | 0.368 | 0.021 |
| ckd | no | 325853 | 46409 | 0.765 | 0.330 | 0.032 |
| ckd | yes | 28534 | 4861 | 0.747 | 0.360 | 0.034 |
| diabetes | no | 267192 | 36153 | 0.768 | 0.323 | 0.032 |
| diabetes | yes | 87195 | 15117 | 0.745 | 0.357 | 0.032 |
| sepsis_dx | no | 301186 | 40063 | 0.768 | 0.314 | 0.037 |
| sepsis_dx | yes | 53201 | 11207 | 0.726 | 0.407 | 0.020 |
| sex | female | 153495 | 21492 | 0.783 | 0.355 | 0.022 |
| sex | male | 200892 | 29778 | 0.749 | 0.321 | 0.040 |

| Race/ethnicity audit level | Landmarks | Events | AUROC | AUPRC | ECE |
| --- | --- | --- | --- | --- | --- |
| white | 221417 | 33458 | 0.753 | 0.330 | 0.032 |
| unknown | 55556 | 8818 | 0.778 | 0.375 | 0.022 |
| black | 31257 | 3984 | 0.793 | 0.352 | 0.029 |
| other | 17926 | 2210 | 0.760 | 0.286 | 0.043 |
| hispanic_latino | 13789 | 1551 | 0.770 | 0.291 | 0.042 |
| asian | 13032 | 1087 | 0.761 | 0.248 | 0.062 |
| american_indian_alaska_native | 676 | 83 | 0.797 | 0.260 | 0.091 |
| native_hawaiian_pacific_islander | 541 | 54 | 0.656 | 0.297 | 0.084 |

## Clinical Interpretation Boundaries

- Retrospective AUROC is not deployment evidence.
- SHAP and PSM outputs, when generated, are exploratory and must not be interpreted causally.
- External transport remained modest; best 72-hour external AUROC was below 0.80.
- The selected model does not satisfy a bedside alerting operating point without further threshold development.
- Local prospective shadow-mode validation and governance evidence are mandatory before any clinical use.

