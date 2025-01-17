---
category: help for installation
tags:
- Synology NAS
- Windows file transfer
- Shared folder
- NAS setup
- Data management
title: How to Transfer Data to Your Synology NAS from Windows?
---
![](/assets/images/nas/56a29a76a9df5fdc61ff35ebdcc9d460.jpeg)

# How to Transfer Data to Your Synology NAS from Windows?

Want to quickly transfer files from your Windows PC to your Synology NAS? By adding shared folders to your File Explorer, you can easily move photos, videos, and other data. This guide provides step-by-step instructions to connect your Synology NAS to your Windows computer.

---

## Steps to Transfer Files to Your Synology NAS

Follow these steps to set up your NAS and transfer files seamlessly:

1. **Prepare your PC for the NAS connection.**  
2. **Activate the Windows File Service on your NAS.**  
3. **Connect your NAS to File Explorer.**

---

## Step 1: Prepare Your PC

Before transferring data, ensure the following prerequisites are met:

1. **Create a Shared Folder:** Set up a shared folder on your NAS for data storage.  
2. **Connect to the Same Network:** Ensure your PC and NAS are on the same local network.  
3. **Access DSM Dashboard:** Log in to your DSM dashboard via the Synology Customer Portal.  
4. **Identify Your NAS Name:** Note the name you assigned to your NAS during DSM setup.  
5. **Check Volume Name:** Go to **Storage Management > Volume Management** in DSM to find your volume name.  
6. **Remember Shared Folder Name:** For instance, a folder like "Movies."

---

## Step 2: Activate the Windows File Service

For your NAS to communicate with Windows, activate the SMB protocol:

1. Log in to the **NAS web interface**.  
2. Navigate to the **Control Panel**.  
3. Select **File Services > SMB/AFP/NFS**.  
4. Enable **SMB** under File Services.  
5. Click **Apply** to save the changes.

---

## Step 3: Connect the NAS to File Explorer

Integrate your NAS with Windows Explorer to enable smooth file transfer:

1. Open **File Explorer** on your PC.  
2. Go to **This PC** and click **Map Network Drive**.  
3. Assign a drive letter (e.g., **B**).  
4. In the **Folder** field, enter the path in this format:  
   `\\<ServerName>\<SharedFolderName>`  
   Example: `\\Diskstation\Volume1\Movies`.  
5. Click **Finish** to map the drive.  
6. Enter your **DSM username and password** and click **OK**.  
7. Your NAS folder will now appear under **This PC** in File Explorer.

---

## File Transfer Tips

You can now transfer files between your PC and NAS just as you would between two local drives. Here are some tips for an optimized experience:

- **Backup Important Files:** Regularly back up critical data to avoid accidental loss.  
- **Organize Shared Folders:** Keep files organized in your shared folders for easier access.  
- **Enable Syncing:** Use Synology Drive for real-time file synchronization.

By following these steps, your Synology NAS becomes an integrated part of your Windows environment, making data transfers straightforward and efficient.

---
