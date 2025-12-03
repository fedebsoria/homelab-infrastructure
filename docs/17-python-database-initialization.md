# 17. Python Database Initialization

## 📅 Date: 2025-12-03

## 📝 Summary
We developed the initial Python logic to bootstrap the database schema. This script serves as the "Backend Initialization" layer, ensuring the SQL tables exist before the application starts processing data.

## ⚙️ Technical Details

### 1. Networking & Service Discovery
- **Hostname:** We used `db` as the hostname in the connection string. In Docker Compose networks, service names resolve to their container's internal IP address via DNS. `localhost` would incorrectly point to the Python container itself.

### 2. Resilience (Retry Logic)
- **Problem:** When starting `docker compose up`, the Python container often starts faster than the MariaDB process is ready to accept connections.
- **Solution:** We implemented a simple retry loop (5 attempts with 2-second delays) in the connection function to prevent the script from crashing immediately during a cold boot.

### 3. Schema Definition
We defined two tables using `InnoDB` engine:
- **`material`:** Inventory items.
- **`employees`:** Staff members.
- **Relationship:** A one-to-many relationship where an employee holds a reference (`material_otorgado`) to a material ID. We used `ON DELETE SET NULL` to ensure that if a laptop is deleted from inventory, the employee record remains valid (just without an assigned device).