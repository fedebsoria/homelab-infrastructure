#!/bin/bash

# --- CONFIG ---
SOURCE_SCRIPT="./scripts/backup_db.sh"
# We'll put the script in a hidden 'bin' or 'scripts' folder in Home to keep it tidy
TARGET_DIR="$HOME/scripts"
TARGET_SCRIPT="$TARGET_DIR/backup_db.sh"
# Cron schedule: Every day at 03:00 AM
CRON_SCHEDULE="0 3 * * *"

# --- LOGIC ---

echo "🔧 Starting Backup Automation Setup..."

# 1. Check if source exist
if [ ! -f "$SOURCE_SCRIPT" ]; then
    echo "❌ Error: Source script $SOURCE_SCRIPT not found. Are you in the project root?"
    exit 1
fi

# 2. Prepare target directory
mkdir -p "$TARGET_DIR"
echo "📂 Target directory checked: $TARGET_DIR"

# 3. Copy the script
cp "$SOURCE_SCRIPT" "$TARGET_SCRIPT"
echo "Copied script to $TARGET_SCRIPT"

# 4. Make it executable
chmod +x "$TARGET_SCRIPT"
echo "🔐 Set execution permissions (+x)"

# 5. Add to Cron (Idempotent: prevents duplicates)
# We list current crons, check if the script is there, if not, append it.ç
CURRENT_CRON=$(crontab -l 2>/dev/null)

if echo "$CURRENT_CRON" | grep -q "$TARGET_SCRIPT"; then
    echo "⚠️  Notice: Cron job already exists. Skipping."
else
    (echo "$CURRENT_CRON"; echo "$CRON_SCHEDULE $TARGET_SCRIPT") | crontab -
    echo "✅ Success: Added new job to Crontab ($CRON_SCHEDULE)"
fi

echo "---"
echo "🎉 Setup Complete! backups will run daily at 3am."