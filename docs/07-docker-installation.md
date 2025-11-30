# 07. Docker Engine Implementation

## 📅 Date: 2025-11-29

## 📝 Summary
We deployed the containerization runtime (Docker Engine) using Ansible. This marks the transition from a standard OS to a Container Host. We prioritized using the official Docker repositories over the Ubuntu upstream ones to ensure access to the latest features and patches.

## ⚙️ Technical Strategy

### 1. Repository Management (The Secure Way)
Instead of `apt-key add` (which is deprecated), we implemented the modern approach for handling GPG keys in Debian/Ubuntu:
- **Keyring:** Downloaded the official Docker GPG key to `/etc/apt/keyrings/docker.asc`.
- **Source Definition:** Explicitly referenced the keyring in the apt source string (`signed-by=...`). This prevents other repositories from spoofing Docker packages.

### 2. Architecture Agnosticism
We used Ansible facts (`ansible_architecture` and `ansible_distribution_release`) to dynamically construct the repository URL.
- **Benefit:** This same playbook will work whether the server is running on an Intel/AMD CPU (`amd64`) or an ARM chip (like a Raspberry Pi), and regardless of the Ubuntu version.

### 3. User Privileges (Rootless-ish)
We added the administration user (`admin-lab`) to the `docker` group.
- **Why:** This grants the user access to the Docker Unix socket `/var/run/docker.sock`, allowing them to run containers without invoking `sudo`.
- **Note:** A session logout/login is required for group changes to take effect.