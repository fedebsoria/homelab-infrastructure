#!/bin/bash

# --- CONFIG. ---
BACKUP_DIR="$HOME/backups_db"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
CONTAINER_NAME="inventory-system-db-1"
DB_USER="user_lab"
DB_PASS="securepass"
DB_NAME="inventory_db"
FILENAME="backup_$DB_NAME_$DATE.sql"

# --- LOGIC ---

echo "Initiating backup for MariaDB container: $CONTAINER_NAME..."

# 1. Make folder if it doesn't exist
mkdir -p "$BACKUP_DIR"

# 2. Execute mysqldump from inside the container
/usr/bin/docker exec "$CONTAINER_NAME" \
    mysqldump -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$BACKUP_DIR/$FILENAME"


# 3. Check if it worked
if [ $? -eq 0 ]; then
    echo "✅ Success: SQL Backup created at $BACKUP_DIR/$FILENAME"
    # compress file
    gzip "$BACKUP_DIR/$FILENAME"
    echo "📦 Compressed to $BACKUP_DIR/$FILENAME.gz"
else
    echo "❌ Error: Backup failed. Check container name and credentials."
fi

# 4. Clean: Erase back-ups older than 7 days
find "$BACKUP_DIR" -type f -name "*.gz" -mtime +7 -delete