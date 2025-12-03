from fasapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
import time
from typing import List, Optional

# --- CONFIGURATION ---
# Connection config.
# NOTE: 'host' is 'db', the name given to the service in docker-compose.yml
DB_CONFIG = {
    'host': 'db',
    'user': 'user_lab',
    'password': 'securepass',
    'database': 'inventory_db',
    'port': 3306
}

# --- PYDANTIC MODELS ---
# These classes define the "Shape" of the JSON data we expect from users.
# Security: if data is wrong, it rejects the request automatically.

class MarialBase(BaseModel):
    name: str
    category: str
    description: Optional[str] = None

class EmployeeBase(BaseModel):
    name: str
    role: str
    given_material: Optional[str] = None

# --- DATABASE FUNCTIONS ---

def get_db_connection():
    """Establishes a fresh connection to the DB."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        # If DB is down, we tell the API user "Service Unavailable"
        raise HTTPException(status_code=503, detail=f"Database connection failed: {err}")

def init_db():
    """Initializes tables on startup."""
    conn = None
    for i in range(5):
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            
            # Table: material
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS material (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                category VARCHAR(50) NOT NULL,
                description TEXT
            ) ENGINE=InnoDB;
            """)
            
            # Table: employees
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                role VARCHAR(100),
                given_material INT,
                FOREIGN KEY (given_material) REFERENCES material(id) ON DELETE SET NULL
            ) ENGINE=InnoDB;
            """)
            
            conn.commit()
            print("SUCCESS: Database initialized.")
            return
        except Exception as e:
            print(f"Waiting for DB... ({i+1}/5)")
            time.sleep(2)
    
    if conn: conn.close()

# --- API APPLICATION ---

app = FastAPI(title="Inventory System API")

# This event runs automatically when the server starts
@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/")
def read_root():
    """Health check endpoint."""
    return {"status": "online", "message": "Welcome to the Inventory API"}

# GET /materials -> Returns a list of all materials
@app.get("/materials")
def get_materials():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) #dictionary=True makes result look like JSON!

    cursor.execute("SELECT * FROM material")
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

# POST /materials -> Adds a new item using the Pydantic Model
@app.post("/materials")
def create_material(item: MaterialBase):
    conn = get_db_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO material (name, category, description) VALUES (%s, %s, %s)"
    val = (item.name, item.category, item.description)

    try:
        cursor.execute(sql, val)
        conn.commit()
        new_id = cursor.lastrowid
        return {"id": new_id, "Message": "Material created successfully"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detal=str(err))
    finally:
        cursor.close()
        conn.close()
