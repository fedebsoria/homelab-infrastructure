# 16. Refactoring to REST API (FastAPI)

## 📅 Date: 2025-12-03

## 📝 Summary
We evolved the application from a one-off execution script into a persistent RESTful API using **FastAPI**. This allows external clients (browsers, other scripts) to interact with the inventory data in real-time via HTTP requests.

## ⚙️ Technical Changes

### 1. Framework Implementation (`main.py`)
- **FastAPI:** Replaced the linear logic with an event-driven application.
- **Pydantic Models:** Defined `MaterialBase` and `EmployeeBase` classes. This provides automatic data validation (e.g., ensuring 'name' is a string) and documentation.
- **Endpoints:**
    - `GET /materials`: Retrieves data as JSON.
    - `POST /materials`: Accepts JSON payloads to insert new records using parameterized SQL queries.

### 2. Dependency Management
Updated `requirements.txt` to include:
- `fastapi`: The web framework.
- `uvicorn[standard]`: The ASGI web server implementation.
- `pydantic`: For data validation.

### 3. Container Lifecycle (`docker-compose.yml`)
- **Command Change:** Switched from `sleep infinity` to `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`.
    - This keeps the container active as a foreground service.
    - `--reload` enables hot-reloading during development.
- **Port Exposure:** Mapped host port `8000` to container port `8000` to allow access to the Swagger UI (`/docs`).
- **TTY Removal:** Removed `tty: true` as the web server process naturally keeps the container in the `Up` state.

## 🚀 Access
The API documentation and testing interface is now available at `http://<server-ip>:8000/docs`.