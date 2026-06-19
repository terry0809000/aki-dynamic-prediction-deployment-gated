# Cover Letter - BMJ Health & Care Informatics

Dear Editors,

Please consider the manuscript, "Deployment-Gated Dynamic Prediction of Severe Acute Kidney Injury in Critical Care: A Transportability and Clinical-Readiness Study," for BMJ Health & Care Informatics.

This paper is positioned as a health-informatics and clinical AI governance study, not as a ready bedside alert. The contribution is a rerunnable, deployment-gated AKI prediction workflow that explicitly tests common retrospective EHR failure modes: measurement-process bias, imperfect baseline creatinine, treatment/documentation confounding, repeated correlated landmarks, cross-database transportability, calibration, threshold burden, and non-causal interpretation of SHAP/PSM diagnostics.

The completed D-drive analysis used MIMIC-IV and eICU archives and found a best prespecified 72-hour external AUROC of 0.763 (95% cluster-bootstrap CI 0.758-0.773) for `cpu_xgb_eicu_to_mimic_no_treatment_external`. Because this did not meet the AUROC >=0.80 guardrail and no threshold met both sensitivity and alert-burden requirements, the deployment gate remained `BLOCKED_NOT_CLINICALLY_DEPLOYABLE`. This negative-to-cautious result is central to the paper: it demonstrates how a publication workflow can prevent unsupported clinical deployment claims.

The manuscript includes 59 references, a target-journal framing, calibration and threshold reporting, subgroup and baseline-source audits, first-landmark-per-stay sensitivity, and a draft hospital deployment evidence packet. The work should interest readers concerned with the safe translation of clinical AI from public ICU datasets into local health systems.

The authors confirm that any clinical use would require local prospective shadow validation, locked thresholds, governance approval, monitoring, incident response, regulatory review, and human-factors signoff.

Sincerely,

Terry Yu
