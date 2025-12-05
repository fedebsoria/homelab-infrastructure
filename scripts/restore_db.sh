#!/bin/bash

# --- CONFIG ---
CONTAINER_NAME="inventory-system-db-1" # Make sure this matches your docker-compose name
DB_USER="user_lab"
DB_PASS="securepass"       # Or use the environment variable if set
DB_NAME="inventory_db"

# --- LOGIC ---
# 1. Check if a filename was provided
if [ -z "$1" ]; then
    echo "❌ Error: No backup file specified."
    echo "Usage: ./scripts/restore_db.sh <path_to_backup_file.sql.gz>"
    exit 1
fi

BACKUP_FILE="$1"

# 2. Check if file exists

if [ ! -f "$BACKUP_FILE" ]; then
    echo "❌ Error: File '$BACKUP_FILE' not found."
    exit 1
fi

echo "⚠️  WARNING: This will OVERWRITE the database '$DB_NAME' in container '$CONTAINER_NAME'."
read -p "Are you sure you want to proceed? (y/N): " -n 1 -r
echo    # move to a new line

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "🚫 Restore cancelled."
    exit 1
fi

echo "🔄 Restoring from $BACKUP_FILE..."

# 3. Restore
# zcat reads the compressed file to stdout
if [[ "$BACKUP_FILE" == *.gz ]]; then
    zcat "$BACKUP_FILE" | /usr/bin/docker exec -i "$CONTAINER_NAME" mysql -u"$DB_USER" -p"$DB_PASS" "$DB_NAME"
else
    # Fallback for non-compressed .sql files
    cat "$BACKUP_FILE"  | /usr/bin/docker exec -i "$CONTAINER_NAME" mysql -u"$DB_USER" -p"$DB_PASS" "$DB_NAME"
fi

# 4. Check result
if [ $? -eq 0 ]; then
    echo "✅ Restore completed successfully."
else
    echo "❌ Restore failed."
    exit 1
fi