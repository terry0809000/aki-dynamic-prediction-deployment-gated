# Data access

This repository does not include raw MIMIC-IV or eICU data.

The workflow expects credentialed local archives:

- `mimic-iv-3.1.zip`
- `eicu-collaborative-research-database-2.0.zip`

The notebook searches `D:\` first on Windows and also supports environment overrides:

```powershell
$env:AKI_MIMIC_ZIP = "D:\mimic-iv-3.1.zip"
$env:AKI_EICU_ZIP = "D:\eicu-collaborative-research-database-2.0.zip"
```

Do not commit credentialed data, extracted CSVs, parquet feature tables, patient-level prediction files, or derived caches.

The included reports and figures are aggregate retrospective research artifacts. They do not make the model clinically deployable.
