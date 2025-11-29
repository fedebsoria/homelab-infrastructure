# 05. Sudoers Configuration & Package Fixes

## 📅 Date: 2025-11-29

## 📝 Summary
We encountered two hurdles during the initial Ansible execution: password prompts for privilege escalation and a missing package error. Both were resolved to establish a fully automated baseline.

## ⚙️ Technical Interventions

### 1. Passwordless Sudo (The "Become" Issue)
Ansible failed initially because the `admin-lab` user required a password for `sudo` commands.
- **Solution:** We configured a specific rule in `/etc/sudoers.d/` to allow the user to execute commands without a password prompt.
- **Command:** `echo "admin-lab ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/admin-lab`
- **Security Note:** While convenient for a lab, in production environments this is often restricted to specific commands or managed via Vault.

### 2. The Neofetch Issue (Ubuntu 24.04 Compatibility)
The playbook failed with `No package matching 'Neofetch' is available`.
- **Root Cause:** The `neofetch` project is archived and was removed from the Ubuntu 24.04 (Noble Numbat) repositories.
- **Resolution:** We replaced the package with **`fastfetch`**, a maintained, C-based alternative that serves the same purpose (displaying system info) and is available in the official repos.

### 3. Ansible Configuration Tweak
We updated `ansible.cfg` to silence the deprecation warning regarding `community.general.yaml`.
- **Change:** Switched `stdout_callback` to `ansible.builtin.default` and configured `[callback_default] result_format = yaml`.