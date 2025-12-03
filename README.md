# 🏠 Enterprise HomeLab Infrastructure

This repository documents the implementation of **Infrastructure as Code (IaC)** for a home laboratory environment, simulating a real-world enterprise client-server architecture.

The primary goal is to master modern DevOps practices by automating the provisioning, configuration, and orchestration of services.

## 🎯 Project Objectives
- **IaC:** Configuration management and provisioning using **Ansible**.
- **Containerization:** Service orchestration using **Docker** and **Docker Compose**.
- **Automation:** Maintenance and setup scripts using **Bash** and **Python**.
- **Security:** Linux server hardening, SSH key management, and network security practices.

## 💻 Hardware Inventory

| Role | Device | Specs | OS | Function |
| :--- | :--- | :--- | :--- | :--- |
| **Control Node** | Custom Workstation | Ryzen 7 5700G, 32GB RAM, RTX 4060 | Windows 11 Pro (VS Code via SSH) | Development, Testing & Playbook Execution |
| **Server Node** | Lenovo ThinkPad L460 | i5-6200U, 12GB RAM, 120GB SSD + 500GB HDD | Ubuntu Server 24.04 LTS | Headless Docker Host & Storage Server |

## 🛠️ Tech Stack
- **Operating System:** Ubuntu Server 24.04 LTS (Noble Numbat)
- **Configuration Management:** Ansible
- **Container Engine:** Docker CE & Docker Compose
- **Scripting:** Bash (Bootstrapping), Python (Automation, database creation and manipulation)
- **Editor:** VS Code (Remote - SSH extension)

## 📂 Repository Structure
```text
.
├── docs/            # Documentation and technical decisions
├── inventory/       # Ansible inventory files (hosts)
├── inventory-system/ # Docker container
├── playbooks/       # Ansible playbooks for configuration
├── scripts/         # Bash script for bootstrapping/maintenance
└── README.md        # Project overview
```
