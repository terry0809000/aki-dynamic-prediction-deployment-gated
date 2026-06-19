# Target Journal Assessment

Updated after completed D-drive run: 2026-06-19

## Recommended Target: BMJ Health & Care Informatics

Rationale: the final verified result is clinically cautious rather than a high-discrimination deployment claim. The best 72-hour external AUROC was 0.763, below the aspirational 0.80 guardrail, and the deployment gate is `BLOCKED_NOT_CLINICALLY_DEPLOYABLE`. The manuscript is therefore strongest as a health-informatics, clinical AI governance, transportability, and auditability paper.

Official site access note: the BMJ Health & Care Informatics pages were checked by URL, but automated page retrieval returned HTTP 403 in this environment. The journal remains an appropriate pragmatic informatics target based on its public journal identity and the existing author/scope URL: https://informatics.bmj.com/pages/about and https://informatics.bmj.com/pages/authors.

## High-Selectivity Alternative: npj Digital Medicine

npj Digital Medicine remains a possible but higher-risk target. Its current aims and scope explicitly include clinical applications of validated AI/ML models, clinical informatics, and digital medicine ethics, governance, policy, regulation, and security. However, the same source says the journal typically does not consider purely observational studies. Because this analysis lacks prospective local validation and did not meet the 72-hour AUROC >=0.80 guardrail, submission should frame the contribution as a deployment-gated transportability framework, not a ready clinical model.

Official link checked June 2026: https://www.nature.com/npjdigitalmed/aims

## Aspirational Only: The Lancet Digital Health

The Lancet Digital Health is not recommended for this version. It would likely require prospective validation, stronger clinical impact evidence, and a more compelling deployment story than the current blocked-gate retrospective analysis.

Official author information/search result checked June 2026: https://www.thelancet.com/journals/landig/home

## Submission Positioning

- Lead with transparent transportability, calibration, subgroup audit, row-correlation sensitivity, and deployment-gate governance.
- Do not claim clinical deployability.
- Report the 12-hour AUROC >=0.80 result only as a secondary short-horizon finding; the primary 72-hour result is below 0.80.
- Emphasize that threshold operating points did not satisfy both sensitivity and alert-burden requirements.
- Treat SHAP and PSM as exploratory diagnostics only, not causal evidence.
