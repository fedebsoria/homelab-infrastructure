# 00. Project Initialization & Architecture Design

## 📅 Date: 2025-11-29

## 📝 Summary
We established the directory structure and initialized the Git repository to track the infrastructure as code (IaC) journey. The hardware roles were defined, separating the Control Node (Windows Workstation) from the Server Node (Ubuntu Headless).

##  decisions Made

### 1. Repository Structure
We adopted a standard Ansible-compatible structure from day one:
- `inventory/`: For future host definitions.
- `playbooks/`: For automation logic.
- `docs/`: To maintain "Documentation as Code" separate from the codebase.

### 2. Hardware Allocation
- **Lenovo ThinkPad L460:** Selected as the server due to its low power consumption (U-series processor) and built-in UPS (battery).
- **Storage Strategy:**
    - **SSD (120GB):** Dedicated to the OS (`/`) for fast boot and read/write operations for container overlays.
    - **HDD (500GB):** Reserved as raw block storage. It will be formatted and mounted later via automation to serve as the persistent data volume for Docker.

### 3. Language & Standards
- Adopted **English** as the primary language for code and documentation to align with industry standards.
- Documentation will be generated iteratively after each major implementation step.