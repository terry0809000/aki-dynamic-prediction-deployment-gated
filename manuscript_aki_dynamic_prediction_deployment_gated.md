# Deployment-Gated Dynamic Prediction of Severe Acute Kidney Injury in Critical Care: A Transportability and Clinical-Readiness Study

Target journal: BMJ Health & Care Informatics  
High-risk alternative: npj Digital Medicine  
Notebook: `aki_ssl_survival_sectioned_workflow_clinical_deployment_gated_v4_d_drive_publication.ipynb`  
Analysis status: Completed D-drive retrospective MIMIC-IV/eICU run with clinical deployment gate blocked.

## Abstract

### Background
Severe acute kidney injury (AKI) in intensive care is common, consequential, and difficult to predict early enough for clinical mitigation. Retrospective electronic health record (EHR) prediction models can appear strong while learning measurement intensity, treatment documentation, local workflow, or baseline-creatinine artifacts rather than transportable patient physiology.

### Methods
We developed a deployment-gated notebook workflow for dynamic prediction of severe AKI or renal replacement therapy (RRT) in adult ICU patients using MIMIC-IV and eICU. The pipeline discovers raw archives on the D drive, builds 2-hour physiologic trajectories, applies dynamic 6-hour landmarks with a 6-hour actionability gap, preserves audit-only metadata, and evaluates strict cross-database transport in both directions. The completed CPU run used engineered landmark features with calibrated histogram gradient boosting and XGBoost classifiers across full, treatment-ablated, measurement-ablated, and conservative feature sets. The notebook also retains an optional self-supervised competing-risk survival-transformer branch for GPU-capable reruns. Evaluation included AUROC, AUPRC, Brier score, expected calibration error (ECE), calibration intercept and slope, threshold operating characteristics, subgroup audit, cluster-bootstrap confidence intervals, first-landmark-per-stay sensitivity, model-selection guardrails, and a hard clinical deployment gate.

### Results
The analytic data included 49,611 final MIMIC-IV ICU stays and 81,322 final eICU stays, yielding 354,387 MIMIC-IV landmarks from 42,012 stays and 581,356 eICU landmarks from 58,427 stays. The best verified 72-hour external model was `cpu_xgb_eicu_to_mimic_no_treatment_external`, with AUROC 0.763 (95% cluster bootstrap CI 0.758-0.773), AUPRC 0.333, Brier score 0.112, ECE 0.032, calibration intercept -0.409, and calibration slope 0.893. This did not meet the prespecified aspirational AUROC >=0.80 guardrail. First-landmark-per-stay AUROC at 72 hours was 0.712, showing meaningful optimism from repeated correlated landmark rows. Treatment-feature ablation caused small discrimination changes, whereas removing measurement-process features reduced AUROC by approximately 0.020-0.022 in the HGB models. No evaluated threshold simultaneously achieved sensitivity >=0.70 and alert rate <=0.25. The deployment gate remained `BLOCKED_NOT_CLINICALLY_DEPLOYABLE` because local prospective shadow-mode validation and governance artifacts were not supplied.

### Conclusions
The workflow produced a transparent, rerunnable, clinically cautious retrospective evaluation, but the final models are not clinically deployable. The study is best framed as a transportability and deployment-readiness analysis rather than a ready bedside AKI alert. Local prospective validation, locked thresholds, workflow review, monitoring, incident response, regulatory assessment, and human-factors signoff are mandatory before any clinical use.

## Introduction

Severe AKI is associated with mortality, longer ICU stay, chronic kidney disease, and high resource utilization [1-8]. ICU patients are particularly vulnerable because serum creatinine is delayed, urine output is intermittently recorded, and kidney injury is intertwined with shock, sepsis, nephrotoxin exposure, fluid balance, mechanical ventilation, and clinical decision-making [1-12]. Predictive models could help prioritize review before irreversible injury, but retrospective EHR models have repeatedly struggled to translate safely into care because their apparent discrimination can depend on surveillance, documentation, site-specific workflows, or noncausal treatment patterns [13-26].

Baseline creatinine is a central example. True outpatient baseline is frequently unavailable, while admission or early-ICU fallback values can already reflect evolving AKI. Dynamic landmarking adds another challenge: a single ICU stay can contribute many highly correlated rows, and row-level performance can overstate precision if repeated predictions are treated as independent [27-31]. Clinical deployment requires more than a high AUROC: calibration, threshold choice, alert burden, subgroup review, local validation, monitoring, and governance are all part of the evidence chain [32-45].

We therefore built and executed a deployment-gated AKI prediction notebook that treats these risks as first-class design constraints. The study objective was not to declare a clinically deployable model from MIMIC-IV and eICU, but to test whether a rigorous, rerunnable workflow could generate transparent transportability evidence while blocking unsupported bedside use.

## Methods

### Study Design and Data Sources

This was a retrospective transportability and clinical-readiness study using MIMIC-IV and eICU [46-49]. The notebook automatically used `D:\mimic-iv-3.1.zip` and `D:\eicu-collaborative-research-database-2.0.zip` when present, with environment-variable overrides for alternate locations. All derived artifacts were written to `aki_ssl_survival_output_clinical_deployment_gated_v4` under a locked clinical pipeline version.

Adult ICU stays were screened. Exclusions included inadequate length of stay, missing baseline creatinine, insufficient urine-output observability, chronic kidney replacement therapy or incompatible renal-history signals where available, and severe AKI/RRT already present by the first actionable landmark.

### Outcome Definition

The target event was severe AKI/RRT after a prediction landmark. Severe AKI followed KDIGO stage 2/3 logic using serum creatinine, urine output, and RRT criteria [1]. Creatinine criteria required at least doubling from baseline or creatinine >=4.0 mg/dL with an acute rise. Urine-output criteria required sustained oliguria with an observation-density requirement. Death and ICU discharge were retained as clinically meaningful competing outcomes in the notebook's survival branch; the completed CPU benchmark used binary horizon-specific labels for 12, 24, 48, 72, and 168 hours.

### Baseline Creatinine

Baseline creatinine used prior measurements within a configurable lookback window when available. If prior baseline was unavailable, fallback was limited to early admission measurements available by the 6-hour first landmark. Baseline-source indicators were included, and source-specific subgroup results were written to quantify whether imperfect baseline estimation changed performance.

### Landmarking and Predictors

The workflow binned time-varying data into 2-hour intervals and created dynamic prediction landmarks every 6 hours. Each landmark used only pre-landmark history, with a 6-hour actionability gap before future events were counted. Predictors included kidney markers, vital signs, blood gases, electrolytes, liver tests, blood counts, glucose, INR, weight, urine output, fluid input, net fluid, vasopressors, diuretics, nephrotoxins, antibiotics, mechanical ventilation, and RRT documentation. Static predictors included age, sex, baseline creatinine, baseline-source indicators, missing-weight indicator, comorbidities, sepsis diagnosis, and ICU type. Race/ethnicity was retained for audit and subgroup reporting, not as a model feature.

### Modeling

The completed local run used CPU-feasible calibrated histogram gradient boosting and XGBoost landmark classifiers. Candidate feature variants were prespecified as full engineered features, treatment/documentation features removed, measurement-process features removed, and conservative feature sets with both treatment/documentation and measurement-process features removed where available. Calibration used source-domain validation data only. The notebook also includes a self-supervised transformer and competing-risk survival branch for GPU-capable reruns; it was not used as the completed local CPU result.

### Validation and Metrics

Strict external validation was performed in both directions: MIMIC-IV to eICU and eICU to MIMIC. The primary horizon was 72 hours. Metrics included AUROC, AUPRC, Brier score, ECE, calibration intercept, calibration slope, cluster-bootstrap confidence intervals using stay-level clusters, threshold operating characteristics, subgroup audit, and first-eligible-landmark-per-stay sensitivity. The claims report ranked all external candidates at 72 hours and explicitly flagged whether the best candidate met the AUROC >=0.80 guardrail.

### Clinical Deployment Gate

The notebook wrote a deployment-gate report and a draft hospital evidence packet. Clinical deployment required completed local prospective shadow-mode validation, locked thresholds, intended-use/workflow documentation, clinical governance approval, regulatory assessment, monitoring and drift plan, incident response plan, and human-factors signoff. Retrospective MIMIC/eICU performance and draft documentation could not satisfy this gate.

### Interpretation Policy

SHAP and propensity-score-matching outputs, if generated, were treated as exploratory diagnostics only. They were not interpreted as causal evidence. Treatment predictors were interpreted as risk markers that may encode clinician concern, indication bias, documentation practice, or severity, not as recommended interventions.

## Results

### Cohort Construction

| Database | Base ICU stays | Baseline sCr available | Final cohort stays | Landmarks | Stays with landmarks | Missing UO exclusions | Severe AKI/RRT by 6h exclusions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MIMIC-IV | 50066 | 49611 | 49611 | 354387 | 42012 | 713 | 872 |
| eICU | 93830 | 81322 | 81322 | 581356 | 58427 | 17207 | 1105 |

### External Model Selection

At the prespecified 72-hour horizon, the best verified external candidate was `cpu_xgb_eicu_to_mimic_no_treatment_external`. It did not reach the AUROC >=0.80 guardrail. The strongest short-horizon result was 0.803 at 12 hours for cpu_xgb_mimic_to_eicu_full_external; this was not the primary endpoint and should not be substituted for the 72-hour claim.

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

### Repeated Landmark Sensitivity

The selected model's 72-hour row-level AUROC was 0.763, compared with first-landmark-per-stay AUROC 0.712. This confirms that repeated landmark rows are correlated and that row-level estimates are optimistic for patient-level deployment reasoning.

| Horizon h | Stays | Events | AUROC | AUPRC | Brier | ECE | Cal intercept | Cal slope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 12 | 42012 | 6813 | 0.724 | 0.309 | 0.126 | 0.032 | 0.046 | 0.855 |
| 24 | 42012 | 9380 | 0.715 | 0.389 | 0.158 | 0.037 | -0.047 | 0.808 |
| 48 | 42012 | 11438 | 0.712 | 0.447 | 0.179 | 0.039 | -0.052 | 0.804 |
| 72 | 42012 | 12212 | 0.712 | 0.474 | 0.185 | 0.036 | -0.058 | 0.813 |
| 168 | 42012 | 13030 | 0.715 | 0.501 | 0.190 | 0.033 | -0.019 | 0.863 |

### Threshold Operating Characteristics

At 72 hours, low thresholds produced unacceptable alert burden, while higher thresholds sacrificed sensitivity. No evaluated threshold met both sensitivity >=0.70 and alert rate <=0.25.

| Threshold | Alert rate | Sensitivity | Specificity | PPV | NPV | Alerts |
| --- | --- | --- | --- | --- | --- | --- |
| 0.05 | 0.789 | 0.970 | 0.242 | 0.178 | 0.979 | 279626 |
| 0.10 | 0.576 | 0.884 | 0.476 | 0.222 | 0.960 | 204257 |
| 0.20 | 0.334 | 0.665 | 0.722 | 0.288 | 0.927 | 118197 |
| 0.30 | 0.197 | 0.457 | 0.847 | 0.336 | 0.902 | 69799 |

### Bias and Robustness Audits

Treatment/documentation feature removal had small effects on 72-hour external AUROC in the HGB models. Measurement-process feature removal caused larger AUROC drops, indicating that surveillance and documentation patterns contribute signal even when they do not fully explain performance.

| Direction | Full AUROC | No-treatment AUROC | No-measurement AUROC | Conservative AUROC | Full minus no-treatment | Full minus no-measurement |
| --- | --- | --- | --- | --- | --- | --- |
| mimic to eicu | 0.752 | 0.749 | 0.730 | 0.722 | 0.003 | 0.022 |
| eicu to mimic | 0.763 | 0.762 | 0.743 | 0.747 | 0.001 | 0.020 |

Baseline-source subgroup performance showed clinically relevant differences.

| Baseline source | Landmarks | Events | AUROC | AUPRC | Brier | ECE | Cal intercept | Cal slope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| early_min_0_6h | 39160 | 7229 | 0.748 | 0.388 | 0.133 | 0.018 | -0.178 | 0.880 |
| prior | 315227 | 44041 | 0.765 | 0.325 | 0.110 | 0.036 | -0.443 | 0.895 |

### Subgroup Audit

The subgroup audit identified variation by age, sex, comorbidity, sepsis status, baseline source, and race/ethnicity. These findings require local review before any clinical deployment and should not be interpreted as proof of model fairness.

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

### Deployment Gate

The deployment gate status was `BLOCKED_NOT_CLINICALLY_DEPLOYABLE`. The rerunnable notebook now writes a draft intended-use/workflow document, governance approval template, regulatory assessment, monitoring and drift plan, incident-response plan, human-factors signoff, prospective shadow-validation protocol, threshold-locking protocol, local data-mapping specification, and packet index. These documents remain explicitly marked as not locally approved. The active blockers are absent completed prospective shadow-validation metrics, absent locked threshold approval, and missing local completion/approval of the required governance, regulatory, monitoring, incident-response, workflow, and human-factors artifacts. Therefore, the model must not be used for patient care from this retrospective run alone.

## Discussion

This completed D-drive run provides a rigorous retrospective evaluation but not a clinically deployable AKI alert. The best 72-hour external AUROC was 0.763, below the aspirational 0.80 threshold, and first-landmark-per-stay AUROC fell to 0.712. These results argue against a bedside-readiness claim and support a more cautious publication framing: transportability, bias auditing, and deployment governance are the study's main contributions.

The analysis directly addressed the main risks for retrospective ICU EHR modeling. First, measurement and documentation bias were evaluated through feature ablation; the observed AUROC drop after removing measurement-process features shows that surveillance intensity is informative and must be audited locally. Second, baseline creatinine uncertainty was preserved as metadata and evaluated through source-specific subgroup metrics. Third, treatment and documentation confounding were evaluated by removing treatment-related variables; effects were small in the HGB benchmark and the selected XGBoost model excluded treatment/documentation features, but causal interpretation remains inappropriate. Fourth, repeated landmark correlation was evaluated with cluster bootstrap and first-landmark-per-stay metrics. Fifth, weak prospective transportability was handled by strict cross-database validation and by refusing deployment claims when the external AUROC guardrail and prospective evidence requirements were not met. Sixth, SHAP and PSM were explicitly bounded as exploratory diagnostics, not causal tools.

The threshold analysis is particularly important. A threshold of 0.20 produced sensitivity 0.665 with alert rate 0.334; a threshold of 0.30 reduced alert rate to 0.197 but sensitivity fell to 0.457. This makes the current model unsuitable for an unvalidated alerting workflow.

### Target Journal Interpretation

Given the final results, BMJ Health & Care Informatics is the most realistic target because the paper is strongest as a pragmatic informatics, auditability, and governance study. npj Digital Medicine remains possible only if framed as a rigorous deployment-readiness and transportability workflow rather than a high-performing deployable model; the journal's scope fits clinical AI and governance, but it typically expects stronger novelty and validation for clinical AI claims.

## Limitations

This study is retrospective and uses public ICU databases rather than a local prospective hospital deployment environment. MIMIC-IV and eICU differ in time period, hospitals, documentation systems, clinical practice, coding, and measurement frequency. Baseline creatinine remains imperfect despite audit safeguards. Urine-output phenotyping depends on documentation density and interval semantics. Dynamic landmark rows are correlated, and row-level AUROC overstates patient-level performance. XGBoost and HGB benchmarks are practical CPU models, while the notebook's optional SSL survival transformer was not completed in this CPU run. Subgroup estimates for smaller race/ethnicity groups are unstable. Finally, AUROC, SHAP, PSM, or threshold tables cannot substitute for prospective validation, governance, and regulatory review.

## Conclusion

The adjusted notebook is rerunnable, clinically stricter, and publication-ready as a transparent retrospective transportability and deployment-readiness study. It should not be described as clinically deployable. The best verified 72-hour external AUROC was 0.763, below the 0.80 guardrail, and the clinical deployment gate remains blocked until local prospective shadow-mode validation, locked thresholds, governance approval, monitoring, incident response, regulatory assessment, and human-factors signoff are completed.

## Data and Code Availability

The notebook artifact is `aki_ssl_survival_sectioned_workflow_clinical_deployment_gated_v4_d_drive_publication.ipynb`. Outputs were written to `aki_ssl_survival_output_clinical_deployment_gated_v4/`. Data access requires appropriate credentialed access to MIMIC-IV and eICU and local availability of the corresponding archives.

## References

1. KDIGO AKI Work Group. KDIGO clinical practice guideline for acute kidney injury. Kidney Int Suppl. 2012;2:1-138.
2. Kellum JA, Romagnani P, Ashuntantang G, Ronco C, Zarbock A, Anders HJ. Acute kidney injury. Nat Rev Dis Primers. 2021;7:52.
3. Hoste EAJ, Bagshaw SM, Bellomo R, et al. Epidemiology of acute kidney injury in critically ill patients. Intensive Care Med. 2015;41:1411-1423.
4. Chertow GM, Burdick E, Honour M, Bonventre JV, Bates DW. Acute kidney injury, mortality, length of stay, and costs. J Am Soc Nephrol. 2005;16:3365-3370.
5. Coca SG, Peixoto AJ, Garg AX, Krumholz HM, Parikh CR. The prognostic importance of a small acute decrement in kidney function in hospitalized patients. Am J Kidney Dis. 2007;50:712-720.
6. Uchino S, Kellum JA, Bellomo R, et al. Acute renal failure in critically ill patients: a multinational study. JAMA. 2005;294:813-818.
7. Bagshaw SM, George C, Bellomo R. A comparison of the RIFLE and AKIN criteria for acute kidney injury in critically ill patients. Nephrol Dial Transplant. 2008;23:1569-1574.
8. Siew ED, Ikizler TA, Matheny ME, et al. Estimating baseline kidney function in hospitalized patients with impaired kidney function. Clin J Am Soc Nephrol. 2012;7:712-719.
9. Waikar SS, Betensky RA, Emerson SC, Bonventre JV. Imperfect gold standards for kidney injury biomarker evaluation. J Am Soc Nephrol. 2012;23:13-21.
10. Waikar SS, Bonventre JV. Creatinine kinetics and the definition of acute kidney injury. J Am Soc Nephrol. 2009;20:672-679.
11. Mehta RL, Kellum JA, Shah SV, et al. Acute Kidney Injury Network: report of an initiative to improve outcomes. Crit Care. 2007;11:R31.
12. Bellomo R, Ronco C, Kellum JA, Mehta RL, Palevsky P. Acute renal failure: definition, outcome measures, animal models, fluid therapy and information technology needs. Crit Care. 2004;8:R204-R212.
13. Tomasev N, Glorot X, Rae JW, et al. A clinically applicable approach to continuous prediction of future acute kidney injury. Nature. 2019;572:116-119.
14. Koyner JL, Carey KA, Edelson DP, Churpek MM. The development of a machine learning inpatient acute kidney injury prediction model. Crit Care Med. 2018;46:1070-1077.
15. Flechet M, Guiza F, Schetz M, et al. AKIpredictor, an online prognostic calculator for acute kidney injury in adult critically ill patients. Ann Intensive Care. 2017;7:39.
16. Mohamadlou H, Lynn-Palevsky A, Barton C, et al. Prediction of acute kidney injury with a machine learning algorithm using electronic health record data. Can J Kidney Health Dis. 2018;5:2054358118776326.
17. Kate RJ, Perez RM, Mazumdar D, Pasupathy KS, Nilakantan V. Prediction and detection models for acute kidney injury in hospitalized older adults. BMC Med Inform Decis Mak. 2016;16:39.
18. Zimmerman LP, Reyfman PA, Smith ADR, et al. Early prediction of acute kidney injury following ICU admission using a multivariate panel of physiological measurements. BMC Med Inform Decis Mak. 2019;19:16.
19. Wilson FP, Shashaty M, Testani J, et al. Automated, electronic alerts for acute kidney injury: a single-blind, parallel-group, randomised controlled trial. Lancet. 2015;385:1966-1974.
20. Selby NM, Hill R, Fluck RJ. Standardizing the early identification of acute kidney injury: the NHS England national patient safety alert. Nephron. 2015;131:113-117.
21. Gianfrancesco MA, Tamang S, Yazdany J, Schmajuk G. Potential biases in machine learning algorithms using electronic health record data. JAMA Intern Med. 2018;178:1544-1547.
22. Obermeyer Z, Powers B, Vogeli C, Mullainathan S. Dissecting racial bias in an algorithm used to manage population health. Science. 2019;366:447-453.
23. Chen IY, Pierson E, Rose S, Joshi S, Ferryman K, Ghassemi M. Ethical machine learning in healthcare. Annu Rev Biomed Data Sci. 2021;4:123-144.
24. Rajkomar A, Oren E, Chen K, et al. Scalable and accurate deep learning with electronic health records. npj Digit Med. 2018;1:18.
25. Beam AL, Kohane IS. Big data and machine learning in health care. JAMA. 2018;319:1317-1318.
26. Kelly CJ, Karthikesalingam A, Suleyman M, Corrado G, King D. Key challenges for delivering clinical impact with artificial intelligence. BMC Med. 2019;17:195.
27. Steyerberg EW. Clinical Prediction Models. 2nd ed. Springer; 2019.
28. Riley RD, van der Windt D, Croft P, Moons KGM. Prognosis Research in Healthcare. Oxford University Press; 2019.
29. Van Calster B, McLernon DJ, van Smeden M, Wynants L, Steyerberg EW. Calibration: the Achilles heel of predictive analytics. BMC Med. 2019;17:230.
30. Vickers AJ, Elkin EB. Decision curve analysis: a novel method for evaluating prediction models. Med Decis Making. 2006;26:565-574.
31. Vickers AJ, Van Calster B, Steyerberg EW. Net benefit approaches to the evaluation of prediction models. BMJ. 2016;352:i6.
32. Collins GS, Reitsma JB, Altman DG, Moons KGM. Transparent Reporting of a multivariable prediction model for Individual Prognosis Or Diagnosis: TRIPOD. Ann Intern Med. 2015;162:55-63.
33. Collins GS, Dhiman P, Andaur Navarro CL, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024.
34. Moons KGM, Wolff RF, Riley RD, et al. PROBAST: a tool to assess risk of bias and applicability of prediction model studies. Ann Intern Med. 2019;170:51-58.
35. Wolff RF, Moons KGM, Riley RD, et al. PROBAST: explanation and elaboration. Ann Intern Med. 2019;170:W1-W33.
36. Wolff RF, Moons KGM, Dhiman P, et al. PROBAST+AI: a risk-of-bias and applicability tool for prediction model studies using artificial intelligence. BMJ. 2025;388:e082505.
37. Liu X, Rivera SC, Moher D, Calvert MJ, Denniston AK. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: CONSORT-AI. Nat Med. 2020;26:1364-1374.
38. Cruz Rivera S, Liu X, Chan AW, et al. Guidelines for clinical trial protocols for interventions involving artificial intelligence: SPIRIT-AI. Nat Med. 2020;26:1351-1363.
39. Vasey B, Nagendran M, Campbell B, et al. DECIDE-AI: reporting guidelines for early-stage clinical evaluation of decision support systems driven by artificial intelligence. Nat Med. 2022;28:924-933.
40. Hernandez-Boussard T, Bozkurt S, Ioannidis JPA, Shah NH. MINIMAR: minimum information for medical AI reporting. Nat Med. 2020;26:1320-1324.
41. Sendak MP, Gao M, Brajer N, Balu S. Presenting machine learning model information to clinical end users with model facts labels. npj Digit Med. 2020;3:41.
42. Wiens J, Saria S, Sendak M, et al. Do no harm: a roadmap for responsible machine learning for health care. Nat Med. 2019;25:1337-1340.
43. Vayena E, Blasimme A, Cohen IG. Machine learning in medicine: addressing ethical challenges. PLoS Med. 2018;15:e1002689.
44. Cabitza F, Rasoini R, Gensini GF. Unintended consequences of machine learning in medicine. JAMA. 2017;318:517-518.
45. Topol EJ. High-performance medicine: the convergence of human and artificial intelligence. Nat Med. 2019;25:44-56.
46. Johnson AEW, Bulgarelli L, Shen L, et al. MIMIC-IV, a freely accessible electronic health record dataset. Sci Data. 2023;10:1.
47. Johnson AEW, Pollard TJ, Shen L, et al. MIMIC-III, a freely accessible critical care database. Sci Data. 2016;3:160035.
48. Pollard TJ, Johnson AEW, Raffa JD, Celi LA, Mark RG, Badawi O. The eICU Collaborative Research Database. Sci Data. 2018;5:180178.
49. Goldberger AL, Amaral LAN, Glass L, et al. PhysioBank, PhysioToolkit, and PhysioNet. Circulation. 2000;101:e215-e220.
50. Wynants L, Van Calster B, Collins GS, et al. Prediction models for diagnosis and prognosis of COVID-19: systematic review and critical appraisal. BMJ. 2020;369:m1328.
51. Luo W, Phung D, Tran T, et al. Guidelines for developing and reporting machine learning predictive models in biomedical research. J Med Internet Res. 2016;18:e323.
52. Norgeot B, Quer G, Beaulieu-Jones BK, et al. Minimum information about clinical artificial intelligence modeling: the MI-CLAIM checklist. Nat Med. 2020;26:1320-1324.
53. Komorowski M, Celi LA, Badawi O, Gordon AC, Faisal AA. The Artificial Intelligence Clinician learns optimal treatment strategies for sepsis in intensive care. Nat Med. 2018;24:1716-1720.
54. Futoma J, Hariharan S, Heller K. Learning to detect sepsis with a multitask Gaussian process RNN classifier. Proc Mach Learn Res. 2017;68:117-125.
55. Subbe CP, Kruger M, Rutherford P, Gemmel L. Validation of a modified Early Warning Score in medical admissions. QJM. 2001;94:521-526.
56. US Food and Drug Administration. Clinical Decision Support Software: Guidance for Industry and Food and Drug Administration Staff. 2026.
57. US Food and Drug Administration. Marketing Submission Recommendations for a Predetermined Change Control Plan for Artificial Intelligence-Enabled Device Software Functions. 2024.
58. Office of the National Coordinator for Health Information Technology. Health Data, Technology, and Interoperability: Certification Program Updates, Algorithm Transparency, and Information Sharing. 2024.
59. Nature Portfolio. npj Digital Medicine guide to authors and aims and scope. Accessed June 2026.
