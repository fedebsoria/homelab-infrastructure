# 14. Project Init: Inventory API

## 📅 Date: 2025-12-02

## 📝 Summary
We initialized a new development project aimed at building a Python-based Inventory API backed by a SQL database. We adopted a container-first approach to ensure the environment is replicable across the Control Node and the Server Node.

## ⚙️ Architectural Decisions

### 1. Microservices Pattern
We split the application into two distinct containers managed by Docker Compose:
- **Database Layer:** Uses the official `mariadb:10.6` image.
- **Application Layer:** A custom Python container that will host our API logic.

### 2. Development Workflow (Bind Mounts)
To facilitate rapid development, we configured a volume mapping (`./app:/app`) in the Compose file.
- **Benefit:** This allows editing code on the host (VS Code on Windows) and executing it immediately inside the container without rebuilding the image for every change.

### 3. Dependencies
We selected `mysql-connector-python` for database connectivity and `tabulate` for CLI output formatting, defined in `requirements.txt`.