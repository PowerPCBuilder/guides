---
category: help for installation
tags:
- Synology NAS
- NAS setup
- DSM installation
- Storage setup
- Shared folder
- Troubleshooting
title: How to Install Your Synology NAS?
---
![](/assets/images/nas/19d5211f60fd16c86b9d2833b62ba550.jpeg)

Written by Giorgos  
24 October 2023 08:51  

# How to Install Your Synology NAS?

Setting up your Synology NAS for the first time can feel overwhelming. This guide breaks down the installation process step by step, so you can start storing and sharing files with ease. Follow along to get your NAS up and running.

---

## Set Up Your Synology NAS in 7 Steps

![Set up your Synology NAS in 7 steps](/assets/images/nas/037fd09028ef9b4d811bad4ed1787e02.jpeg)

### Summary of Steps:
1. Place the hard drives in the NAS.  
2. Connect the NAS to the network.  
3. Install the DSM software.  
4. Complete the initial setup by entering your information.  
5. Configure the storage pool and volume.  
6. Create a shared folder.  
7. Make the NAS accessible on other devices.  

---

## Step 1: Place the Hard Drives in the NAS

![Expert places drive in NAS](/assets/images/nas/c73c4c6c6ac6aecfc9197aadafad3bc7.jpeg)

1. Remove the front panel of your NAS (if applicable).  
2. Pull out the drive holders and remove the side panels.  
3. Insert the hard drive into the holder and reattach the side panels.  
4. Slide the holder into the NAS.  
5. For 2.5-inch drives, secure them using screws in the designated spots.  

Repeat for multiple drives, then proceed to the next step.

---

## Step 2: Connect the NAS to the Network

![Find Synology via browser](/assets/images/nas/0bb72a569b7c4fd12e0b2683dc1f764a.jpeg)

1. Use a network cable to connect your NAS to the router.  
2. Power on the NAS.  
3. Open a web browser and go to [find.synology.com](http://find.synology.com).  
4. Select your NAS and click **Connect**.  
5. Click **Install** to continue with the DSM setup.

---

## Step 3: Install the DSM Software

![Loading time Synology DSM installation](/assets/images/nas/fdfe19cde763b83cc20f4da31991dbbf.jpeg)

1. After clicking **Install**, choose **Automatic Installation**.  
2. Note that this process erases all data on your drives.  
3. Confirm the setup to begin DSM installation.  
4. Wait approximately 10 minutes for the process to complete.  

---

## Step 4: Complete the Initial Setup

![Go through the Synology installation](/assets/images/nas/99f2d9e248991c0f677b630721a0db01.jpeg)

1. Assign a **Device Name** for your NAS.  
2. Create an **Administrator Account** with a secure password.  
3. Choose your preferred update settings (automatic is recommended).  
4. Click **Next** to proceed to the NAS desktop.

---

## Step 5: Configure the Storage Pool and Volume

![Select the storage pool in the Synology volume menu](/assets/images/nas/83a5b454934219c0707f879279a82cce.jpeg)

1. Navigate to **Storage Manager > Volume Menu**.  
2. Click **Create** to start the setup.  
3. For a simple setup, choose **Automatic Installation** with the SHR configuration.  
4. Select the drive(s) for the volume and click **Next**.  
5. Enable the **Btrfs** file system for advanced storage features.  

The NAS will perform a parity test but remains operational during this time.

---

## Step 6: Create a Shared Folder

![Create a shared folder for other users](/assets/images/nas/a45f8571e1a11fae0a2cf580357a9fbd.jpeg)

1. Open the **Control Panel** and select **Shared Folder**.  
2. Click **Create** and provide a name and description for the folder.  
3. Assign a volume and configure user permissions.  


---

## Step 7: Make the NAS Accessible on Other Devices

![Expert working on a Windows PC with a Synology NAS](/assets/images/nas/d69226d227423545ab2951e142a5041f.jpeg)

### On Windows:
- Ensure your PC is on the same network as the NAS.  
- Have the NAS name, volume name, and shared folder details ready.  


### On Mac:
- Connect your MacBook, iMac, or Mac Mini to the same network.  
- Use the NAS name, volume name, and shared folder details.  

---

## Troubleshooting Common Issues

![](/assets/images/nas/b885121e9f0ed6147c89fc45bb4d5102.jpeg)

### Why Doesn't the NAS Recognize Your Drive?
- Ensure the drive is securely inserted.  
- Verify the drive's compatibility on the Synology website.  

### What If the NAS Bay or Hard Drive Is Broken?
- Try another NAS slot to check for a defective bay.  
- If the drive still doesn’t appear, it may need replacement.  

### Why Doesn't the NAS Appear in Your Network?
- Reset the NAS and reconnect via [find.synology.com](http://find.synology.com).  
- Restart your router if the issue persists.  

If all else fails, contact Synology customer service for assistance.

---
