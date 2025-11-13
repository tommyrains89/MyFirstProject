# scout_backup.py
"""
A tiny local backup simulator for My First Project.
This script copies files from `project_files/` into a timestamped folder under `backups/`.
Purpose: practice scripting, file ops, and create some local artifacts to commit.
Safe: no network, no credentials, no destructive operations.
"""

import os
import shutil
from datetime import datetime

SRC_DIR = "project_files"
BACKUP_ROOT = "backups"

def ensure_dirs():
    os.makedirs(SRC_DIR, exist_ok=True)
    os.makedirs(BACKUP_ROOT, exist_ok=True)

def create_sample_file():
    # If the source dir is empty, create a dummy file so the backup isn't empty.
    sample_path = os.path.join(SRC_DIR, "notes.txt")
    if not os.path.exists(sample_path):
        with open(sample_path, "w", encoding="utf-8") as f:
            f.write("Some random notes about this little project.\n")
            f.write("Date: {}\n".format(datetime.now().isoformat()))
            f.write("Scout is the best debugging buddy. 🐶\n")

def make_backup():
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = os.path.join(BACKUP_ROOT, f"backup_{ts}")
    shutil.copytree(SRC_DIR, dest)
    return dest

def append_log(dest):
    log_path = os.path.join(BACKUP_ROOT, "backup.log")
    with open(log_path, "a", encoding="utf-8") as logf:
        logf.write(f"{datetime.now().isoformat()} - created backup at {dest}\n")

def main():
    ensure_dirs()
    create_sample_file()
    dest = make_backup()
    append_log(dest)
    print(f"Backup created at: {dest}")
    print("Log appended to backups/backup.log")

if __name__ == "__main__":
    main()
