# 02. Server Bootstrapping

## 📅 Date: 2025-11-29

## 📝 Summary
We created the first automation artifact: a Bash script (`setup.sh`) designed to prepare a fresh Ubuntu installation for configuration management. This script handles system updates and installs Ansible locally on the server.

## ⚙️ Technical Details

### Why a Bash Script?
While Ansible is our goal, we need a way to get from a "clean ISO install" to an "Ansible-ready state". Bash is the native language of Linux and requires no dependencies, making it perfect for this "chicken and egg" problem.

### Key Actions Performed by `setup.sh`
1.  **System Update:** Runs `apt update && apt upgrade` with `DEBIAN_FRONTEND=noninteractive` to prevent the script from hanging on "Are you sure?" prompts.
2.  **Core Tools:** Installs `git` (to pull this repo later), `curl`, and `python3` (required by Ansible).
3.  **Ansible Installation:**
    - Adds the official PPA (`ppa:ansible/ansible`).
    - Installs the latest stable version of Ansible.
    - *Decision:* We installed Ansible **on the server** (Pull/Local model) for this phase. This allows the server to configure itself by running playbooks locally if needed, simplifying the initial learning curve compared to setting up WSL2 inventory immediately.