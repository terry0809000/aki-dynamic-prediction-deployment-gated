# TRIPOD+AI-Oriented Readiness Checklist

Status: draft self-audit for submission support. This is not an official completed EQUATOR form.

| Domain | Manuscript/package coverage | Status |
| --- | --- | --- |
| Title/abstract identify prediction model and AI/ML nature | Title and abstract describe dynamic prediction, AKI/RRT, ICU, MIMIC-IV/eICU, and deployment gate | covered |
| Background and intended use | Introduction and deployment-gate sections define retrospective research purpose and blocked clinical use | covered |
| Data source and eligibility | Methods and cohort table report MIMIC-IV/eICU sources, exclusions, baseline sCr, landmarks, and urine-output exclusions | covered |
| Outcome definition | Severe AKI/RRT and KDIGO-compatible criteria described | covered |
| Predictor definition and timing | Landmarking, actionability gap, feature families, and audit-only metadata described | covered |
| Missingness/measurement process | Urine-output coverage, measurement-process ablation, baseline-source audit, and documentation bias described | covered |
| Sample size and events | Cohort and external metric tables report stays, landmarks, and events | covered |
| Model development | CPU HGB/XGBoost models and optional SSL survival branch described | covered |
| Validation | Strict MIMIC-to-eICU and eICU-to-MIMIC external validation reported | covered |
| Performance measures | AUROC, AUPRC, Brier, ECE, calibration intercept/slope, thresholds, subgroup audit, and cluster bootstrap included | covered |
| Clinical utility | Threshold operating characteristics reported; no deployable threshold claimed | covered |
| Interpretability | SHAP/PSM bounded as exploratory and non-causal | covered |
| Deployment readiness | Deployment gate and draft hospital evidence packet included; gate remains blocked | covered |
| Reproducibility | Notebook, reports, figures, config, and environment manifest generated | covered |
