# Day 13 – Linux Volume Management (LVM)

## Overview

On Day 13 of my #90DaysOfDevOps journey, I explored **Linux Logical Volume Management (LVM)** on an AWS EC2 instance.

This hands-on lab focused on creating flexible storage volumes, mounting them, and extending them dynamically without downtime—an essential real-world Linux administration and DevOps skill.

---

## Objectives

- Understand LVM architecture
- Create a Physical Volume (PV)
- Create a Volume Group (VG)
- Create a Logical Volume (LV)
- Format and mount storage
- Extend logical volumes online
- Verify storage changes

---

## Lab Environment

- **Platform:** AWS EC2 (Ubuntu)
- **Privilege:** Root access
- **Disk Type:** Loop device (virtual disk simulation)
- **Filesystem:** ext4

---

## Implementation Steps

### 1) Create Virtual Disk

Created a 1GB virtual disk for LVM practice:

```bash
dd if=/dev/zero of=/tmp/disk1.img bs=1M count=1024
losetup -fP /tmp/disk1.img
losetup -a
```

---

### 2) Create Physical Volume

Initialized the virtual disk as an LVM Physical Volume:

```bash
pvcreate /dev/loop4
pvs
```

---

### 3) Create Volume Group

Created a storage pool named `devops-vg`:

```bash
vgcreate devops-vg /dev/loop4
vgs
```

---

### 4) Create Logical Volume

Created logical volume `app-data`:

```bash
lvcreate -L 500M -n app-data devops-vg
lvs
```

---

### 5) Format & Mount

Formatted with ext4 and mounted:

```bash
mkfs.ext4 /dev/devops-vg/app-data
mkdir -p /mnt/app-data
mount /dev/devops-vg/app-data /mnt/app-data
```

---

### 6) Extend Volume

Extended storage online:

```bash
lvextend -L +200M /dev/devops-vg/app-data
resize2fs /dev/devops-vg/app-data
```

---

## Key Concepts Learned

### Physical Volume (PV)

Actual storage device prepared for LVM.

### Volume Group (VG)

A pool of storage built from one or more PVs.

### Logical Volume (LV)

Virtual partitions created from a VG.

---

## What I Learned

- LVM provides flexible storage management
- Storage can be resized live with minimal disruption
- Filesystems can be extended without remounting
- LVM is widely used in production Linux environments

---

## Real-World Use Cases

- Database storage expansion
- Kubernetes node disk scaling
- Log storage management
- Dynamic cloud server storage allocation

---

## Project Structure

```text
day-13/
├── screenshots/
├── day-13-lvm.md
├── reference.md
└── README.md
```

---

## Outcome

Successfully implemented the complete LVM lifecycle:

PV → VG → LV → Format → Mount → Extend → Verify

This lab strengthened my Linux storage management fundamentals and practical DevOps troubleshooting skills.

---

## Tags

#Linux #LVM #AWS #EC2 #DevOps #CloudEngineering #90DaysOfDevOps #TrainWithShubham
