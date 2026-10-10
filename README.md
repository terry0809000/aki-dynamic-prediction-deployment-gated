# Deployment-gated severe AKI dynamic prediction

This repository contains a rerunnable clinical-ML research workflow for dynamic prediction of severe acute kidney injury (AKI) or renal replacement therapy (RRT) in adult ICU patients using MIMIC-IV and eICU.

The project is intentionally **deployment-gated**. It is suitable for retrospective research, transportability analysis, manuscript preparation, and local hospital review. It is **not clinically deployable** from the retrospective public-database run alone.

## Current verified result

- Primary endpoint: severe AKI/RRT within 72 hours after an eligible dynamic landmark.
- Best verified 72-hour strict external model: `cpu_xgb_eicu_to_mimic_no_treatment_external`.
- AUROC: `0.763` with 95% cluster-bootstrap CI `0.758-0.773`.
- AUPRC: `0.333`.
- Brier score: `0.112`.
- Expected calibration error: `0.032`.
- First-landmark-per-stay AUROC: `0.712`.
- Deployment gate: `BLOCKED_NOT_CLINICALLY_DEPLOYABLE`.

No valid 72-hour external AUROC >= `0.80` candidate was found without suspicious leakage or overclaiming. A 12-hour secondary model exceeded 0.80 AUROC, but it is not the prespecified primary claim.

## Clinical guardrails

The workflow explicitly addresses:

- retrospective EHR measurement and documentation bias;
- imperfect baseline creatinine provenance;
- treatment/documentation confounding;
- repeated correlated landmark rows;
- cross-database transportability from MIMIC/eICU;
- calibration and threshold operating burden;
- subgroup auditability;
- non-causal interpretation of SHAP and propensity-score-matching diagnostics.

SHAP and PSM outputs, if generated, are exploratory diagnostics only. They must not be interpreted as causal evidence.

## Main files

- `aki_ssl_survival_sectioned_workflow_clinical_deployment_gated_v4_d_drive_publication.ipynb`  
  Rerunnable notebook with data discovery, phenotype building, model selection, reports, and deployment gate.

- `run_aki_v4_notebook.py`  
  Plain-Python runner for executing the notebook cells outside Jupyter.




- `aki_ssl_survival_output_clinical_deployment_gated_v4/reports/`  
  Model-selection report, deployment-gate report, clinical model card, and transportability audit.

- `aki_ssl_survival_output_clinical_deployment_gated_v4/figures/publication/`  
  Publication figures in PNG/PDF.

## Data access

Raw MIMIC-IV and eICU archives are not included. They require credentialed access and should remain outside Git. The notebook auto-discovers:

- `D:\mimic-iv-3.1.zip`
- `D:\eicu-collaborative-research-database-2.0.zip`

Environment overrides are supported:

```powershell
$env:AKI_MIMIC_ZIP = "D:\mimic-iv-3.1.zip"
$env:AKI_EICU_ZIP = "D:\eicu-collaborative-research-database-2.0.zip"
$env:AKI_OUTPUT_ROOT = "$PWD"
```

## Rerun

Install the Python dependencies in `requirements.txt`, then run:

```powershell
python run_aki_v4_notebook.py
```

To refresh reports without retraining:

```powershell
$env:AKI_RUN_EXPERIMENT = "reports_only"
python run_aki_v4_notebook.py
```

The CPU-feasible default is `cpu_publication_benchmark`. XGBoost benchmarking can be selected with:

```powershell
$env:AKI_RUN_EXPERIMENT = "cpu_xgb_publication_benchmark"
python run_aki_v4_notebook.py
```

## Clinical deployment status

The current output is blocked for clinical deployment. A real hospital deployment requires, at minimum:

- local prospective shadow-mode validation;
- locked thresholds;
- intended-use and workflow signoff;
- clinical governance approval;
- regulatory assessment;
- monitoring and drift plan;
- incident response plan;
- human-factors testing and signoff.

The draft evidence packet is under `aki_ssl_survival_output_clinical_deployment_gated_v4/reports/deployment_evidence/`.

## Repository policy

This repository excludes raw data, caches, feature parquet files, generated model binaries, predictions, logs, and credentialed database archives.

No clinical decision should be made from this repository without local prospective validation and governance approval.

## Public Repository Release Layer

This repository has been prepared as a public, citable research-software
package rather than a notebook-only upload.

Key public-release files:

- `docs/CLINICAL_ALGORITHMICIAN_ANNOTATION.md`
- `docs/DEPLOYMENT_READINESS.md`
- `DATA_ACCESS.md`
- `.zenodo.json`
- `scripts/validate_repository.py`
- `.github/workflows/repository-publication.yml`
- `Dockerfile`

Validate the release package with:

```bash
python scripts/validate_repository.py
```

## Software-only repository

The current branch contains research software, permitted evidence and reproduction documentation. Manuscripts and editorial bundles were removed from the current tree on 10 October 2026; historical commits remain recoverable. This cleanup does not constitute a fresh empirical rerun or change the scientific results. Dataset access restrictions and deployment limits still apply.
