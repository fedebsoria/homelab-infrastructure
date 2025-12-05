# 21 - Backup Automation Strategy

**Date:** 2025-12-04
**Objective:** Automate daily database backups to ensure data persistence and disaster recovery.

## Changes Implemented
1. **Backup Script (`backup_db.sh`):**
   - Created a Bash script to execute `mysqldump` inside the Docker container.
   - Configured backup destination to `~/backups_db` (User Home) to decouple backup storage from the project directory.
   - Added logic to compress (`gzip`) SQL files and rotate backups (delete files older than 7 days).

2. **Automation Installer (`install_backup_job.sh`):**
   - Created a setup script to deploy the backup script to `$HOME/scripts/`.
   - Modifies the user's `crontab` to schedule execution at **03:00 AM daily**.
   - Ensures idempotency (does not add duplicate cron jobs if run multiple times).

## How to Verify
- Run `crontab -l` to see the scheduled job.
- Check `~/backups_db` the following morning to confirm the `.sql.gz` file generation.

# Cron Job Reliability Fix

**Date:** 2025-12-04
**Objective:** Prevent execution failures when running the backup script via Crontab.

## Issue Identified
Cron environments typically have a limited `$PATH`. Executing `docker` directly caused failures because the system could not locate the binary during automated runs.

## Solution
Updated `backup_db.sh` to use the absolute path for the Docker executable.

**Change:**
From: `docker exec ...`
To:   `/usr/bin/docker exec ...`

**Result:** The script is now robust against environment variable differences between interactive shells and cron sessions.