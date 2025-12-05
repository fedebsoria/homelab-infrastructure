# 06 - Database Restoration Script

**Date:** 2025-12-05
**Objective:** Create a mechanism to restore the database from the compressed backups created by the automation script.

## Solution implemented
Created `scripts/restore_db.sh`.

**Key Features:**
1. **Safety Check:** Prompts the user for confirmation (y/N) before overwriting the database.
2. **On-the-fly Decompression:** Uses `zcat` to pipe the compressed SQL data directly into the mysql process inside the Docker container.
3. **Format Support:** Automatically detects if the file is `.gz` or plain `.sql`.

**Usage:**
`./scripts/restore_db.sh <path_to_backup_file>`