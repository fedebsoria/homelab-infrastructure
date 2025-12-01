# 04. Ansible Initialization & First Playbook

## 📅 Date: 2025-11-29

## 📝 Summary
We successfully transitioned from Bash scripting to Ansible automation. We configured the Ansible environment on the Server Node and executed a "Hello World" playbook to validate the installation pipeline.

## ⚙️ Configuration Details

### 1. Ansible Configuration (`ansible.cfg`)
Created a project-level configuration file to standardize behavior:
- **`inventory = inventory/hosts.ini`**: Defines the default inventory path.
- **`stdout_callback = yaml`**: Improves output readability in the terminal.

### 2. Inventory Strategy (`local`)
For this initial phase, we are using a **Local execution model**.
- **Host:** `localhost`
- **Connection:** `local`
- **Reason:** This allows the server to configure itself without needing complex SSH keys setups from the controller yet. It simplifies the learning curve for the first run.

### 3. The "Hello World" Playbook
We created `playbooks/00-hello-world.yml` to test the core modules:
- `ansible.builtin.ping`: Verified Python execution.
- `ansible.builtin.apt`: Installed `neofetch` (proved `sudo` privileges work).
- `ansible.builtin.copy`: Created a file to verify filesystem write access.

### 4. Workflow Established
We established the GitOps-lite workflow:
1.  **Code** changes on Control Node (Windows).
2.  **Push** to GitHub.
3.  **Pull** on Server Node.
4.  **Execute** with `ansible-playbook`.