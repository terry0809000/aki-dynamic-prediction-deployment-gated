# Intended Use and Workflow

DRAFT_NOT_APPROVED_FOR_CLINICAL_USE

## Intended Use
This artifact is a draft workflow specification for prospective shadow validation of the severe AKI/RRT dynamic prediction model. It is not an order set, treatment recommendation, autonomous diagnostic system, or clinically approved alert. It may only be used in silent mode until the deployment gate passes with local evidence.

## Eligible Population
Adult ICU patients after the first 6 hours of an ICU stay, excluding patients with ESRD/chronic dialysis, kidney transplant status where captured, ICU stays shorter than 24 hours, severe AKI/RRT already present by the 6-hour landmark, and stays with insufficient urine-output observability under the configured KDIGO urine-output coverage rule.

## Prediction Timing
The primary operating horizon is 72 hours after each eligible landmark, with a 6-hour actionability gap. Repeated landmark rows must be interpreted as serial assessments within the same stay, not independent patients.

## Recipients and Actions
During shadow validation, predictions are logged only for evaluation. After governance approval, any alert must be routed to the locally named ICU/nephrology clinical owner and paired with a written clinical pathway covering medication review, hemodynamic assessment, fluid balance review, repeat creatinine/urine-output assessment, and nephrology escalation criteria.

## Required Local Customization
The hospital must specify the alert recipient, escalation window, override workflow, audit owner, downtime procedure, model version, EHR integration owner, and patient-safety contact. No bedside display or interruptive alert is allowed until those fields are locally approved.
