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
- **Scripting:** Bash (Bootstrapping), Python (Automation)
- **Editor:** VS Code (Remote - SSH extension)

## 📂 Repository Structure
```text
.
├── docs/           # Documentation and technical decisions
├── inventory/      # Ansible inventory files (hosts)
├── playbooks/      # Ansible playbooks for configuration
├── scripts/        # Bash/Python scripts for bootstrapping/maintenance
└── README.md       # Project overview
```

# 🏠 Enterprise HomeLab Infrastructure

Este repositorio documenta la implementación de infraestructura como código (IaC) para un entorno de laboratorio doméstico, simulando una arquitectura cliente-servidor empresarial.

El objetivo es automatizar el despliegue de servicios y configuraciones utilizando prácticas modernas de DevOps.

## 🎯 Objetivos del Proyecto
- **IaC:** Gestión de configuración con Ansible.
- **Contenedorización:** Despliegue de servicios con Docker y Docker Compose.
- **Scripting:** Automatización de tareas de mantenimiento (Bash/Python).
- **Seguridad:** Hardening de servidores Linux y gestión de SSH.

## 💻 Inventario de Hardware

| Rol | Dispositivo | Specs | SO | Función |
| :--- | :--- | :--- | :--- | :--- |
| **Control Node** | PC Custom | Ryzen 7 5700G, 32GB RAM, Win 11 | WSL2 / VS Code | Desarrollo y ejecución de playbooks |
| **Server Node** | Lenovo ThinkPad L460 | i5-6200U, 12GB RAM, SSD 120GB + HDD 500GB | Ubuntu Server 24.04 | Host de Docker y almacenamiento |

## 🛠️ Stack Tecnológico
- **OS:** Ubuntu Server 24.04 LTS
- **Automation:** Ansible, Bash
- **Containers:** Docker, Docker Compose
- **Editor:** VS Code (Remote SSH)

## Roadmap
- [ ] Instalación base de Ubuntu Server (Particionamiento manual)
- [ ] Configuración de SSH y Hardening básico
- [ ] Bootstraping inicial con Bash
- [ ] Despliegue de Docker con Ansible