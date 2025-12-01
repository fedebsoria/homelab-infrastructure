# 11. Storage Configuration

## 📅 Date: 2025-12-01

## 📝 Summary
We configured the secondary storage drive (500GB HDD) to serve as the persistent data layer for our container infrastructure. This separates the OS/System data (on the 120GB SSD) from application data.

## ⚙️ Technical Details

### 1. Drive Identification
- **Device:** `/dev/sda` (Lenovo ThinkPad Fixed Disk)
- **Partition:** `/dev/sda1`
- **Filesystem:** `ext4`

### 2. Implementation Strategy (Ansible)
We used `ansible.posix.mount` to handle the mounting process.
- **Mount Point:** `/mnt/data`
- **Persistence:** The module automatically updates `/etc/fstab`, ensuring the drive remounts automatically after a reboot.
- **Permissions:** Ownership was transferred to the `admin-lab` user to prevent permission issues when mapping volumes in Docker Compose.

### 3. Why this matters?
By mounting this drive to `/mnt/data`, we established a standard path for all future Docker volumes (e.g., `/mnt/data/mysql`, `/mnt/data/media`). If the OS fails or needs to be reinstalled, the data on the HDD remains untouched.