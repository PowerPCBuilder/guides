---
category: help for installation
permalink: /nas/how_to_transfer_drives_from_your_old_synology_nas/
tags:
- Synology NAS
- Hard drive transfer
- NAS migration
- Data backup
- NAS setup
- Troubleshooting
title: How to Transfer Drives from Your Old Synology NAS?
---
![](/assets/images/nas/how_to_transfer_drives_from_your_old_synology_nas.jpeg)

# How to Transfer Drives from Your Old Synology NAS?

Transferring hard drives from your old Synology NAS to a new one involves more than simply moving the drives. Compatibility, backup, and proper setup are essential steps. This guide walks you through the process in six detailed steps, ensuring a smooth migration.

---

## Transfer Your Hard Drives in 6 Easy Steps

![Synology NAS on a table](/assets/images/nas/1197c524e1895b13256f3a26bce70113.jpeg)

Follow these six steps to successfully transfer your drives:

1. **Check the compatibility of your drives.**  
2. **Create a backup of your settings.**  
3. **Back up your data using Hyper Backup.**  
4. **Transfer the hard drives.**  
5. **Install the hard drives in the new NAS.**  
6. **Set up your new NAS and restore settings.**

### What You’ll Need:
- Your old and new Synology NAS devices.  
- A laptop or desktop computer.  
- A network connection (router or modem).  
- Internal hard drives and one temporary extra drive.

---

## Step 1: Check the Compatibility of Your Drives

![IronWolf HDD next to a Synology NAS](/assets/images/nas/920e8c09edc0c3799a22d62bb9d3994b.jpeg)

Before transferring, ensure your drives are compatible with the new NAS. If you’re using an M.2 SSD for caching, check its compatibility too.

- For the **same NAS model**, proceed to Step 2.  
- For a **different NAS model**, consult the [HDD/SSD compatibility list](https://www.synology.com/en-global/compatibility).  

**Note:** Drives like Seagate IronWolf or WD Red are compatible with most Synology NAS models released after 2015. If using HDDs larger than 8TB, ensure the NAS supports drives from 2021 or later.

---

## Step 2: Create a Backup of Your Settings

![Make a backup of your settings via Synology DSM](/assets/images/nas/ecd0e7b8924220e63622540b48be4f25.jpeg)

Log into your old NAS and navigate to the **Configuration screen**.  

1. Select **Update and Restore** to ensure DSM is up to date.  
2. Under the **Configuration Backup** tab, choose **Backup** and save the settings.  
3. Store the backup on a temporary drive, not one of your main hard drives.  

---

## Step 3: Back Up Your Data Using Hyper Backup

![Make backups of your files via Synology Hyper Backup](/assets/images/nas/a3c93000db01bf1bf643c397549b2904.jpeg)

While data isn’t usually lost during transfer, a backup is always a safe choice.

1. Install the **Hyper Backup** app from the Synology Store.  
2. Create a new backup task, selecting **External NAS Device** as the destination.  
3. Enter the IP address of your new NAS (found at [find.synology.com](https://find.synology.com)).  
4. Select folders and apps for backup and click **Complete**.  
5. Power down both NAS systems once the backup is finished.

---

## Step 4: Transfer the Hard Drives

![Expert replaces hard drive in Synology NAS](/assets/images/nas/88506d4ae37599e782c492f33b03d44a.jpeg)

With both NAS devices turned off:

1. Remove the hard drives from the old NAS.  
2. Note the installation order of the drives for proper setup in the new NAS.  
3. Insert the drives into the new NAS and power it on.

---

## Step 5: Install the Hard Drives in the New NAS

![Migrate your settings to the new NAS via Synology Find](/assets/images/nas/37198b8a8517a11c21d30a7df5810249.jpeg)

Access the new NAS via your computer:

1. Visit [find.synology.com](https://find.synology.com) in your browser.  
2. Double-click the new NAS and confirm its status is **Migratable**.  
3. Select **Install** and choose the **Migrate** option.  

If you encounter a warning about data deletion, ensure the drives are installed in the correct order and retry.

---

## Step 6: Set Up Your New NAS

![Restore your configuration via Synology DSM](/assets/images/nas/d7e2996b5956374d062c14d519809fed.jpeg)

Complete the setup:

1. Choose the latest DSM version during installation.  
2. Restore settings from the backup file saved in Step 2.  
3. Finalize the configuration, and your new NAS is ready for use.

---

## How to Replace Drives in a Broken NAS?

![Expert replaces HDD for Synology NAS in bracket](/assets/images/nas/037fd09028ef9b4d811bad4ed1787e02.jpeg)

If your old NAS is defective:

1. Use a temporary hard drive to install DSM on the new NAS.  
2. Insert your old drives into the same model NAS in the original order.  
3. Sign in to restore functionality.

---

## Common Questions

![Synology troubleshooting image](/assets/images/nas/4407d7076f0c7bd98cc407dfdbeeed2e.jpeg)

### How Do I Migrate My SSD Cache to a New NAS?  
Ensure the new NAS uses the same DSM version. If not, remove the cache and reinstall it on the new NAS.

### Can I Move a Drive from a Single-Slot NAS to a Multi-Slot Model?  
No, unless the NAS models are identical. Otherwise, format the drive or back it up before transferring.

### Can Drives Be Moved to a Less Powerful NAS?  
It’s technically possible, but performance may suffer. Upgrade to a similar or better model for optimal results.

---
