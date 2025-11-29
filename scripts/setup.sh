#!/bin/bash

# ------------------------------------------------------------------
# [Author] Fede Soria
# [Description] Initial server bootstrapping. Updates the system
#               and installs Ansible + core dependencies.
# ------------------------------------------------------------------

set -e

#Colors for output
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}--- 🚀 Starting Server Bootstrap Process ---${NC}"

# 1. System Update
echo -e "${GREEN}[+] Updating system packages...${NC}"
export DEBIAN_FRONTEND=noninteractive
sudo apt update && sudo apt upgrade -y

# 2. Install Dependencies
echo -e "${GREEN}[+] Installing core tools (Git, Curl, Python3)...${NC}"
sudo apt install -y git curl python3 python3-pip software-properties-common

# 3. Install Ansible
# We add the official PPA to get the latest version, not the old one in default repos
echo -e "${GREEN}[+] Adding Ansible PPA and installing...${NC}"
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible

# 4. Verification
echo -e "${GREEN}[+] Bootstrap complete! Verifying Ansible installation:${NC}"
ansible --version

echo -e "${GREEN}--- ✅ Server is ready for Automation ---${NC}"