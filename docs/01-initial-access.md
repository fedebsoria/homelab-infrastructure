# 01. Initial Access & Basic Configuration

## 📅 Date: 2025-11-29

## 📝 Summary
We performed the post-installation configuration of the Ubuntu Server (Server Node). The goal was to ensure the server remains operational headless (lid closed) and to establish secure, passwordless SSH connectivity from the Control Node.

## ⚙️ Configuration Details

### 1. Power Management (Lid Switch)
To prevent the laptop from suspending when the lid is closed, we modified the `systemd-logind` configuration.

- **File:** `/etc/systemd/logind.conf`
- **Change:** Set `HandleLidSwitch=ignore`
- **Reason:** This allows the ThinkPad to function as a compact server unit stored in a rack or shelf without needing to stay physically open.

### 2. SSH Key-Based Authentication
We moved away from password-based authentication for SSH to facilitate Ansible automation.

- **Algorithm:** Ed25519 (Selected for better security and performance over RSA).
- **Implementation:**
    1. Generated a keypair on the Windows Control Node.
    2. Appended the public key (`id_ed25519.pub`) to the server's `~/.ssh/authorized_keys`.
    3. Verified passwordless login.

### 3. VS Code Remote Config
Configured the SSH client config (`~/.ssh/config`) to alias the server as `homelab-server`. This streamlines the workflow in VS Code, allowing instant connection without typing credentials or IP addresses.