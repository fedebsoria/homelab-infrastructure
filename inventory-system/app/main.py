import mysql.connector
import time
import sys

# Connection config.
# NOTE: 'host' is 'db', the name given to the service in docker-compose.yml
DB_CONFIG = {
    'host': 'db',
    'user': 'user_lab',
    'password': 'securepass',
    'database': 'inventory_db',
    'port': 3306
}

def create_connection():
    """Try connect to the data base with severeral intents."""
    conn = None
    # We try 5 times as sometimes the database starts slower than Python
    for i in range(5):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            print("Successfully connected to the database!")
            return conn
        except mysql.connector.Error as err:
            print(f"Connection faile ({i+1}/5): {err}")
            time.sleep(2) #Waits 2 seconds and then retry
    return None

def create_tables(cursor):
    """Creates the tables' structure"""
    # 1. IT Material table
    # Use AUTO_INCREMENTE so the ID is automatically generated
    table_material = """
    CREATE TABLE IF NOT EXISTS material (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        category VARCHAR(50) NOT NULL,
        description TEXT
    ) ENGINE=InnoDB;
    """

    # 2. Employees table
    # Include the Foreign Key (FK) pointing to material table
    table_employees = """
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        role VARCHAR(100),
        given_material INT,
        FOREIGN KEY (given_material) REFERENCES material(id) ON DELETE SET NULL
    ) ENGINE=InnoDB;
    """
    print("Creating table 'material'...")
    cursor.execute(table_material)

    print("Creating table 'employees...")
    cursor.execute(table_employees)

def main():
    conn = create_connection()
    if conn is None:
        sys.exit("Error: Could not connect to the database after retries.")

    try:
        cursor = conn.cursor()
        create_tables(cursor)
        print("\nSUCCESS: Database structure initialized correctly.")
    except mysql.connector.Error as err:
        print(f"Error executing SQL: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()