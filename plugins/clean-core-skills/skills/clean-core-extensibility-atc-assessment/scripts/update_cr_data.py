"""
Cloudification Repository Data Updater
=======================================
Checks whether the bundled CR data files are current against GitHub,
and optionally downloads the latest versions.

Usage:
  python scripts/update_cr_data.py --check     # check only, no download
  python scripts/update_cr_data.py             # check and download if outdated
"""

import json
import sys
import urllib.request
import urllib.error
import os
import argparse
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
METADATA_FILE = DATA_DIR / "cr_metadata.json"
GITHUB_REPO = "SAP/abap-atc-cr-cv-s4hc"
FILES = {
    "objectReleaseInfo_PCELatest.json": "src/objectReleaseInfo_PCELatest.json",
    "objectClassifications_SAP.json": "src/objectClassifications_SAP.json",
}
RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_REPO}/main"
API_BASE = f"https://api.github.com/repos/{GITHUB_REPO}"


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "atc-skill-updater/1.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode())


def get_latest_commit(file_path: str) -> dict:
    url = f"{API_BASE}/commits?path={file_path}&per_page=1"
    data = fetch_json(url)
    commit = data[0]
    return {
        "commit_sha": commit["sha"][:12],
        "commit_date": commit["commit"]["committer"]["date"][:10],
        "commit_message": commit["commit"]["message"].split("\n")[0],
    }


def download_file(filename: str, remote_path: str) -> int:
    url = f"{RAW_BASE}/{remote_path}"
    req = urllib.request.Request(url, headers={"User-Agent": "atc-skill-updater/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        content = resp.read()
    dest = DATA_DIR / filename
    dest.write_bytes(content)
    data = json.loads(content.decode())
    # return object count from whichever top-level list key exists
    for key in ("objectReleaseInfo", "objectClassifications"):
        if key in data:
            return len(data[key])
    return 0


def load_metadata() -> dict:
    if not METADATA_FILE.exists():
        return {}
    return json.loads(METADATA_FILE.read_text())


def save_metadata(meta: dict):
    METADATA_FILE.write_text(json.dumps(meta, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Check / update bundled CR data files.")
    parser.add_argument("--check", action="store_true",
                        help="Check for updates only — do not download.")
    args = parser.parse_args()

    print("Cloudification Repository Data Updater")
    print("=" * 45)

    try:
        meta = load_metadata()
    except Exception as e:
        print(f"Warning: could not read metadata file: {e}")
        meta = {}

    bundled_files = meta.get("files", {})

    print(f"\nChecking GitHub ({GITHUB_REPO}) for latest versions...\n")

    updates_available = []
    latest_info = {}

    for filename, remote_path in FILES.items():
        bundled = bundled_files.get(filename, {})
        bundled_sha = bundled.get("commit_sha", "unknown")
        bundled_date = bundled.get("commit_date", "unknown")

        try:
            latest = get_latest_commit(remote_path)
        except urllib.error.URLError as e:
            print(f"  {filename}")
            print(f"    Bundled : {bundled_date} ({bundled_sha})")
            print(f"    GitHub  : Could not reach GitHub — {e}")
            print()
            continue

        latest_info[filename] = latest
        is_current = latest["commit_sha"] == bundled_sha

        status = "UP TO DATE" if is_current else "UPDATE AVAILABLE"
        print(f"  {filename}")
        print(f"    Bundled : {bundled_date} ({bundled_sha})")
        print(f"    GitHub  : {latest['commit_date']} ({latest['commit_sha']})  —  {latest['commit_message']}")
        print(f"    Status  : {status}")
        print()

        if not is_current:
            updates_available.append(filename)

    if not updates_available:
        print("All files are current. No action needed.")
        return

    print(f"{len(updates_available)} file(s) can be updated.")

    if args.check:
        print("\nRun without --check to download the latest files.")
        print("Example:")
        print("  python scripts/update_cr_data.py")
        return

    print("\nDownloading updated files...")
    from datetime import date
    updated_meta = dict(meta)
    updated_meta["bundled_on"] = date.today().isoformat()
    updated_meta.setdefault("source_repo", f"https://github.com/{GITHUB_REPO}")
    updated_meta["files"] = dict(bundled_files)

    for filename in updates_available:
        remote_path = FILES[filename]
        print(f"  Downloading {filename}... ", end="", flush=True)
        try:
            count = download_file(filename, remote_path)
            latest = latest_info[filename]
            updated_meta["files"][filename] = {**latest, "object_count": count}
            print(f"done ({count} objects)")
        except Exception as e:
            print(f"FAILED — {e}")
            print("  Keeping existing file unchanged.")

    save_metadata(updated_meta)
    print("\nMetadata updated. Bundled files are now current.")
    print(f"Metadata written to: {METADATA_FILE}")


if __name__ == "__main__":
    main()
