# Clinical Deployment Gate Report

Pipeline version: `2026-06-19-d-drive-publication-gated-v4`
Status: **BLOCKED_NOT_CLINICALLY_DEPLOYABLE**

## Blockers
- Incomplete required deployment evidence: prospective_shadow_validation_metrics (CSV has no completed evidence rows); locked_thresholds (CSV has no completed evidence rows); intended_use_and_workflow (draft document requires local completion and approval); clinical_governance_approval (draft document requires local completion and approval); regulatory_assessment (draft document requires local completion and approval); monitoring_and_drift_plan (draft document requires local completion and approval); incident_response_plan (draft document requires local completion and approval); human_factors_signoff (draft document requires local completion and approval)
- No completed local prospective shadow-mode validation metrics were provided.

## Retrospective Clinical Warnings
- No retrospective warning thresholds were crossed, or audits have not been run yet.

## Required Evidence Files
- `prospective_shadow_validation_metrics`: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\prospective_shadow_validation_metrics.csv`
- `locked_thresholds`: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\locked_thresholds.csv`
- `intended_use_and_workflow`: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\intended_use_and_workflow.md`
- `clinical_governance_approval`: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\clinical_governance_approval.md`
- `regulatory_assessment`: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\regulatory_assessment.md`
- `monitoring_and_drift_plan`: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\monitoring_and_drift_plan.md`
- `incident_response_plan`: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\incident_response_plan.md`
- `human_factors_signoff`: `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\human_factors_signoff.md`

## Supporting Draft Deployment Documents
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\clinical_governance_approval.md`
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\deployment_evidence_packet_index.md`
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\human_factors_signoff.md`
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\incident_response_plan.md`
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\intended_use_and_workflow.md`
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\local_data_mapping_specification.md`
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\monitoring_and_drift_plan.md`
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\prospective_shadow_validation_protocol.md`
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\regulatory_assessment.md`
- `aki_ssl_survival_output_clinical_deployment_gated_v4\reports\deployment_evidence\threshold_locking_protocol.md`

## Non-Causal Interpretation Warning
- SHAP and PSM outputs are exploratory diagnostics. They must not be used as causal evidence for treatment decisions.

