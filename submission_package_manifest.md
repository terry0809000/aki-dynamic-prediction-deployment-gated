# AKI Publication and Deployment-Review Package

Generated: 2026-06-19

## Primary Submission Files
- Manuscript DOCX: `manuscript_aki_dynamic_prediction_deployment_gated_submission.docx`
- Manuscript Markdown source: `manuscript_aki_dynamic_prediction_deployment_gated.md`
- Cover letter draft: `cover_letter_bmj_health_care_informatics.md`
- Target journal assessment: `target_journal_assessment.md`
- TRIPOD+AI-oriented checklist: `tripod_ai_readiness_checklist.md`
- PROBAST+AI-oriented risk-of-bias summary: `probast_ai_risk_of_bias_summary.md`

## Rerunnable Analysis Files
- Notebook: `aki_ssl_survival_sectioned_workflow_clinical_deployment_gated_v4_d_drive_publication.ipynb`
- Runner: `run_aki_v4_notebook.py`
- Output directory: `aki_ssl_survival_output_clinical_deployment_gated_v4/`

## Key Reports
- Model selection and claims: `aki_ssl_survival_output_clinical_deployment_gated_v4/reports/model_selection_and_claims_report.md`
- Clinical deployment gate: `aki_ssl_survival_output_clinical_deployment_gated_v4/reports/clinical_deployment_gate_report.md`
- Clinical bias/transportability audit: `aki_ssl_survival_output_clinical_deployment_gated_v4/reports/clinical_bias_transportability_audit.md`
- Model card: `aki_ssl_survival_output_clinical_deployment_gated_v4/reports/clinical_model_card.md`

## Deployment Evidence Packet
- Folder: `aki_ssl_survival_output_clinical_deployment_gated_v4/reports/deployment_evidence/`
- Status: draft/not approved for clinical use
- Gate: `BLOCKED_NOT_CLINICALLY_DEPLOYABLE`

## Primary Verified Result
- 72-hour selected external model: `cpu_xgb_eicu_to_mimic_no_treatment_external`
- AUROC: 0.763 (95% CI 0.758-0.773)
- AUPRC: 0.333
- Brier: 0.112
- ECE: 0.032
- Interpretation: no valid 72-hour external AUROC >=0.80 candidate; no clinical deployability claim.
