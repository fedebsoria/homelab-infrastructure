# 14. Inventory System Development (Python + SQL)

## 📅 Date: 2025-12-03

## 📝 Summary
We successfully developed and containerized a "Full Stack" application consisting of a custom Python API and a MariaDB database. The application is designed to manage IT inventory and employee assignments.

## ⚙️ Technical Architecture

### 1. Docker Composition
We moved beyond using pre-built images and authored our own infrastructure:
- **`docker-compose.yml`**: Orchestrates two services (`app` and `db`).
- **`Dockerfile`**: A custom recipe for the Python environment using `python:3.11-slim`. We optimized the build process by copying `requirements.txt` separately to leverage Docker's layer caching.

### 2. Networking & Service Discovery
- **Internal DNS:** The Python application connects to the database using the hostname `db`. This abstracts the IP address management, relying on Docker's internal DNS resolver to route traffic between containers.
- **Port Isolation:** The database port (3306) is exposed internally to the network but not published to the host machine, increasing security. Only the application container can talk to the database.

### 3. Application Logic (`main.py`)
The Python script implements the following robust patterns:
- **Resilience:** A retry loop (5 attempts) handles the "race condition" where the Python container starts before the Database is ready to accept connections.
- **Idempotency:** The `CREATE TABLE IF NOT EXISTS` statement ensures the script can run multiple times without failing or corrupting the schema.
- **Transaction Management:** We used `conn.commit()` to persist changes and `buffered=True` in the cursor to prevent synchronization errors when reading fetch results.

### 4. Data Model
- **`material`**: Stores hardware details (Laptops, GPUs, etc.).
- **`employees`**: Stores staff details with a Foreign Key (`ON DELETE SET NULL`) linking to the assigned hardware.