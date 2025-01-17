---
category: help for troubleshooting
tags:
- Synology NAS
- RAID setup
- Data protection
- Storage management
- NAS configuration
title: How to Change the RAID Setup on Your Synology NAS?
---
![](/assets/images/nas/beb975c0e16fd424ce9a06bf2a037532.jpeg)

# How to Adjust the RAID Setup of Your Synology NAS?

A RAID setup combines multiple hard drives to increase performance and protect against data loss. This guide explains how to create, modify, or restore a RAID setup on your Synology NAS.

---

## What Is a RAID Setup?

![Synology NAS in RAID mode](/assets/images/nas/43c96d7a229d9faeb869ea9462df69d1.jpeg)

RAID stands for **Redundant Array of Independent Disks**. It allows you to combine hard drives for increased performance or redundancy. 

---

## Options for Adjusting RAID Setup

![Adjust RAID setup](/assets/images/nas/a063afe63fd6b47ad75cdf10d4867cac.jpeg)

There are three main options for working with RAID on your Synology NAS:

1. Create a new RAID setup (deletes all files).  
2. Change the current RAID setup (without losing data).  
3. Restore an old RAID setup (deletes all files).

---

## Option 1: Create a New RAID Setup

![Create a new RAID setup](/assets/images/nas/3127c9d3d31066dff3e4513330662488.jpeg)

### New RAID Setup Options

| From      | To               | Minimum Number of Drives |
|-----------|------------------|--------------------------|
| No RAID   | Basic or JBOD    | 1                        |
| No RAID   | RAID 0 or 1      | 2                        |
| No RAID   | Synology SHR     | 2                        |
| No RAID   | RAID 5           | 3                        |
| No RAID   | RAID 6 or 10     | 4                        |
| No RAID   | Synology SHR-2   | 4                        |

### How to Create a New RAID Setup

> **Warning:** Creating a new RAID setup deletes all files on the disks. Make a backup if needed.

1. Open a browser and go to [find.synology.com](http://find.synology.com).  
2. Click **Main Menu** > **Storage Manager**.  
3. Select **Storage Pool** and click **Create**.  
4. Choose **Better Performance** or **Higher Flexibility** based on your needs.  
   - Note: SHR and SHR-2 are unavailable under **Better Performance**.  
5. Select the desired RAID type and click **Next**.  
6. Choose the hard drives for the RAID setup.  
7. Review your choices and click **Apply**.  
8. In **Storage Manager**, go to **Volume** and click **Create**.  
9. Select **Choose an Existing Storage Pool** and configure the volume size.  
10. Complete the process and click **Apply**.

---

## Option 2: Change the RAID Setup

![Change the RAID setup](/assets/images/nas/a6ff062157abb362f9ffb75c3d67edf8.jpeg)

### Supported RAID Changes

| From         | To              | Minimum Number of Drives |
|--------------|-----------------|--------------------------|
| Basic/JBOD   | RAID 1          | 2 (1 more than Basic)    |
| Basic/JBOD   | RAID 5          | 3 (2 more than Basic)    |
| RAID 1       | RAID 5          | 3 (1 more than RAID 1)   |
| RAID 5       | RAID 6          | 4 (1 more than RAID 5)   |
| SHR          | SHR-2           | 4/5 (2 more than SHR)    |

### How to Change the RAID Setup

> **Note:** Changes outside the above table will result in data loss. Always back up your data.

1. Open a browser and go to [find.synology.com](http://find.synology.com).  
2. Navigate to **Main Menu** > **Storage Manager**.  
3. Select **Volume** from the left-hand menu.  
4. Choose the target volume and click **Manage**.  
5. Select **Change RAID Type** and click **Next**.  
6. Pick the new RAID type and click **Next**.  
7. If adding new drives, select them and click **Next**.  
8. Complete the process. Your RAID setup has now been updated.

---

## Option 3: Restore a RAID Setup

![Restore RAID setup](/assets/images/nas/a6ff062157abb362f9ffb75c3d67edf8.jpeg)

> **Warning:** Restoring a RAID setup deletes all data on the disks. Backup your data before proceeding.

### How to Restore a RAID Setup

1. Open the NAS configuration page ([find.synology.com](http://find.synology.com)) and log in.  
2. Optionally, back up your data using the **Synology Hyper Backup** application.  
3. Go to **Main Menu** > **Storage Manager**.  
4. Select **Volume** and delete the current volume. Confirm the deletion.  
5. Click **Create** and choose the disks to use.  
6. Select the desired RAID setup and follow the steps to complete the process.  
7. The volume may take several hours to be fully ready. Check its status in the volume overview.

---

## Final Notes

- **Backup Regularly:** Always ensure your data is backed up before making changes to RAID setups.  
- **Choose the Right RAID:** Understand your storage needs and select the appropriate RAID type for performance or redundancy.  
- **Seek Support:** If you encounter issues, consult Synology support for assistance.

By following these steps, you can effectively manage RAID setups on your Synology NAS, ensuring optimal storage performance and data protection.

---
