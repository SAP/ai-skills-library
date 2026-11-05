# How to Update the Cloudification Repository Data

## Background

The dashboard uses SAP's **Cloudification Repository (CR)** to determine the potential score for ATC findings that have a successor available. Specifically it answers the question: *if a finding's referenced object has a known successor, what level is that successor?*

- **Released** successor → potential score contribution = **0 points** (fully clean)
- **Classic API** successor → potential score contribution = **1 point** (Level B, still some debt)

This data comes from two files in the public GitHub repository [`SAP/abap-atc-cr-cv-s4hc`](https://github.com/SAP/abap-atc-cr-cv-s4hc):

| File | What it contains |
|---|---|
| `objectReleaseInfo_PCELatest.json` | All officially **released** SAP objects (~44,000) and deprecated objects with successor info |
| `objectClassifications_SAP.json` | Objects classified as **Classic API** or **noAPI** (~8,500) |

SAP updates these files with each S/4HANA release (typically twice per year — FPS0 and FPS1). The files are **bundled inside this skill** so the dashboard works without any internet connection, but they need to be refreshed when SAP ships a new release.

---

## Where the files live

```
skills/clean-core-atc-assessment/
└── scripts/
    └── data/
        ├── objectReleaseInfo_PCELatest.json   ← bundled CR data
        ├── objectClassifications_SAP.json     ← bundled CR data
        └── cr_metadata.json                   ← version record (see below)
```

---

## cr_metadata.json — the version record

Every time the files are downloaded (including the initial bundle), a `cr_metadata.json` is written next to them. It records:

- **`bundled_on`** — date you last downloaded the files
- **`commit_sha`** — the GitHub commit SHA the files came from (12 chars)
- **`commit_date`** — when SAP pushed that commit
- **`commit_message`** — SAP's commit message (usually mentions the release, e.g. "2025 FPS1 file updates")
- **`object_count`** — number of objects in the file at that point

Example:
```json
{
  "bundled_on": "2026-06-19",
  "source_repo": "https://github.com/SAP/abap-atc-cr-cv-s4hc",
  "files": {
    "objectReleaseInfo_PCELatest.json": {
      "commit_sha": "04861814ff8a",
      "commit_date": "2026-02-25",
      "commit_message": "Add files via upload - 2025 FPS1 file updates",
      "object_count": 44541
    },
    "objectClassifications_SAP.json": {
      "commit_sha": "04861814ff8a",
      "commit_date": "2026-02-25",
      "commit_message": "Add files via upload - 2025 FPS1 file updates",
      "object_count": 8479
    }
  }
}
```

The dashboard footer shows the `commit_date` and `commit_message` from this file, so anyone reading a report can immediately see which CR version was used.

---

## Checking whether an update is available

Run this from the skill root directory (requires internet access — run it from your laptop, not from a restricted system):

```bash
python scripts/update_cr_data.py --check
```

Example output when files are current:
```
Cloudification Repository Data Updater
=============================================

Checking GitHub (SAP/abap-atc-cr-cv-s4hc) for latest versions...

  objectReleaseInfo_PCELatest.json
    Bundled : 2026-02-25 (04861814ff8a)
    GitHub  : 2026-02-25 (04861814ff8a)  —  Add files via upload
    Status  : UP TO DATE

  objectClassifications_SAP.json
    Bundled : 2026-02-25 (04861814ff8a)
    GitHub  : 2026-02-25 (04861814ff8a)  —  Add files via upload
    Status  : UP TO DATE

All files are current. No action needed.
```

Example output when an update is available:
```
  objectReleaseInfo_PCELatest.json
    Bundled : 2026-02-25 (04861814ff8a)
    GitHub  : 2026-09-12 (a3f92c1d4e7b)  —  Add files via upload - 2025 FPS2 file updates
    Status  : UPDATE AVAILABLE

1 file(s) can be updated.

Run without --check to download the latest files.
```

---

## Downloading the update

When an update is available, run the same script **without** `--check`:

```bash
python scripts/update_cr_data.py
```

This will:
1. Download the new file(s) into `scripts/data/`
2. Update `cr_metadata.json` with the new commit SHA, date, and object count
3. Print a confirmation

Commit the updated files to your repository so the skill is kept in sync.

---

## When should you check?

SAP typically releases S/4HANA updates twice per year (around spring and autumn). A practical cadence:

- **After each SAP S/4HANA release** (FPS0 / FPS1) — check and update if needed
- **Before a major Clean Core assessment** — verify the files are current so potential scores reflect the latest SAP classifications
- **If a successor lookup returns "unknown"** for an object you know SAP has released — that's a sign the bundled files may be outdated

---

## Manual check (no script)

If you want to verify manually, open this URL in a browser and look at the most recent commit date and message:

```
https://github.com/SAP/abap-atc-cr-cv-s4hc/commits/main/src/objectReleaseInfo_PCELatest.json
```

Compare the date shown there against the `commit_date` in your local `cr_metadata.json`. If GitHub shows a newer date, an update is available.
