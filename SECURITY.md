# Security and clinical-use policy

## No clinical use

This repository is a retrospective research artifact. It must not be used to guide patient care unless a local institution completes prospective shadow-mode validation, locks thresholds, approves workflow and governance, completes regulatory review, and signs monitoring, incident-response, and human-factors plans.

## Data handling

Do not open pull requests or commits containing:

- raw MIMIC-IV or eICU archives;
- extracted credentialed source tables;
- patient-level feature parquet files;
- patient-level predictions;
- model checkpoints trained on patient-level data;
- logs containing local paths to sensitive files or credentials.

## Vulnerability or data-exposure reports

If a commit accidentally includes restricted data or credentials, remove public access immediately, rotate exposed credentials, and rewrite repository history before reuse.
