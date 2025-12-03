import mysql.connector
import time
import sys
from tabulate import tabulate

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
    
def populate_data(conn, cursor):
    """Inserts initial sample data."""

    # 1. Check if data already exists to avoid duplicates
    cursor.execute("SELECT COUNT(*) FROM material")
    result = cursor.fetchone()

    #FIX: Safety check in case result is None
    if result and result[0] > 0:
        print("Data already exists. Skippint insertion.")
        return
    
    print("Inserting sample data...")

    # 2. Insert Material (The Laptop)
    # Note: We use %s as place holders for security (prevents SQL Injection)
    sql_material = "INSERT INTO material (name, category, description) VALUES (%s, %s, %s)"
    val_material = ("Lenovo ThinkPad L460", "Laptop", "Lab Server with Docker")
    cursor.execute(sql_material, val_material)

    # 3. Capture the generated ID
    laptop_id = cursor.lastrowid
    print(f" -> Material inserted with ID: {laptop_id}")

    # 4. Insert Employee (Assigning the Laptop ID)
    sql_employee = "INSERT INTO employees (name, role, material_otorgado) VALUES (%s, %s, %s)"
    val_employee = ("Admin Lab", "DevOps Student", laptop_id)
    cursor.execute(sql_employee,val_employee)

    # 5. COMMIT (Save changes permanently)
    conn.commit()
    print("Transaction committed")

def fetch_data(cursor):
    """Fetches and displays data using Tabulate"""
    print("\n--- Current Inventory ---")

    # Query with JOIN to show Employee Name + Laptop Name
    query = """
    SELECT e.id, e.name, e.role, m.name AS device
    FROM employees e
    LEFT JOIN material m ON e.given_material = m.id
    """
    cursor.execute(query)
    result = cursor.fetchall()

    # Print table
    headers = ["ID", "Employee Name", "Role", "Assigned Device"]
    print(tabulate(result, headers=headers, tablefmt="grid"))

def main():
    conn = create_connection()
    if conn is None:
        sys.exit("Error: Could not connect to the database after retries.")

    try:
        #FIX: buffered=True helps prevent sync issues with the cursor
        cursor = conn.cursor(buffered=True)

        create_tables(cursor)
        populate_data(conn, cursor)
        fetch_data(cursor) # Show the result

    except mysql.connector.Error as err:
        print(f"Error executing SQL: {err}")
    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    main()