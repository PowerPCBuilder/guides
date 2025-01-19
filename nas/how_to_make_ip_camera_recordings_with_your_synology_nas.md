---
category: help for installation
permalink: /nas/how_to_make_ip_camera_recordings_with_your_synology_nas/
tags:
- Synology NAS
- IP camera
- Surveillance Station
- NAS setup
- Camera recordings
- Troubleshooting
title: How to Make IP Camera Recordings with Your Synology NAS?
description: Connect an IP camera to your Synology NAS using Surveillance Station for secure, centralized video storage. Install Surveillance Station, connect your camera, configure settings, and verify the connection. Customize video, recording, and schedules for efficient surveillance. Troubleshoot connection issues via firmware updates, firewall settings, and network compatibility checks.
---
![](/assets/images/nas/how_to_make_ip_camera_recordings_with_your_synology_nas.jpeg)

# How to Make IP Camera Recordings with Your Synology NAS?

Using Synology Surveillance Station, you can connect IP cameras to your Synology NAS to capture and store footage. This setup not only provides more storage capacity than a camera's SD card but also allows you to view live footage through a user-friendly interface. This guide walks you through the steps to connect an IP camera to your Synology NAS.

---

## Installing an IP Camera for Synology in 5 Steps

![Synology IP camera settings via Surveillance Station](/assets/images/nas/d9827851e80ee58611c02b6a8666574a.jpeg)

Follow these steps to set up your IP camera with Synology Surveillance Station:

1. Install Synology Surveillance Station.  
2. Connect the camera.  
3. Enter the camera information.  
4. Review and configure settings.  
5. Verify the connection.

### Requirements:

- A Synology NAS  
- Internal hard drives for footage storage  
- A compatible IP camera  
- A desktop or laptop  
- A (modem) router connecting the NAS, IP cameras, and computer  

---

## Step 1: Install Synology Surveillance Station

![Synology IP camera settings via Surveillance Station](/assets/images/nas/d9827851e80ee58611c02b6a8666574a.jpeg)

1. Open the **Synology Package Center** and search for "Surveillance Station."  
2. Click **Install** to download the application.  
3. Once installed, you’ll find Surveillance Station in the main menu.  
4. Open the app. If you see an empty window, don’t worry—you haven’t connected a camera yet.

---

## Step 2: Connect the Camera to Your NAS

![Add camera in Surveillance Station](/assets/images/nas/15c97edf32503c3983f324a850517bb4.jpeg)

1. Open **Surveillance Station** and navigate to **IP Camera** from the main menu.  
2. Click **Add** to launch the Camera Wizard.  
3. Choose between **Quick Installation** (basic setup) or **Complete Installation** (customize video settings, recording options, and schedules).  
4. Select the server you want to connect to and proceed.

---

## Step 3: Enter the Camera Information

![Enter the camera information in Surveillance Station](/assets/images/nas/ba80665843b803d4abb78c377f224490.jpeg)

1. Click the magnifying glass next to **IP Address** to automatically search for available devices.  
2. Select your camera from the list and click **OK**.  
3. Surveillance Station auto-fills basic details. Disable extra features like firmware or UPnP on the camera if needed.  
4. Test the connection by clicking **Test Connection**. If successful, a green check mark will appear, and you’ll see a live preview of the camera feed.

---

## Step 4: Configure and Review Settings

![Set up recording schedules in Synology Surveillance Station](/assets/images/nas/9e7221ee5a4abda18bef831651e70a7b.jpeg)

If you chose **Complete Installation**, you’ll encounter advanced settings:

1. **Video Settings:** Adjust audio format, streaming profiles, resolution, and frame rate for up to three streams.  
2. **Recording Options:** Configure pre-recording times, storage duration, and select a storage drive or volume.  
3. **Schedules:** Set specific times for recording by dragging across the timeline fields.

---

## Step 5: Verify the Connection

![Test the connection in Surveillance Station](/assets/images/nas/a390fd04f018eea801428ffdcb04ae4b.jpeg)

1. Once installation is complete, your camera will appear in the device list with its connection status:  
   - **Activate:** The camera is connecting.  
   - **Disconnected:** Indicates an issue with the connection.  

2. To view live footage, open **Surveillance Station**, navigate to **Recording**, and select the desired video.

---

## Troubleshooting Connection Issues

![](/assets/images/nas/504123826c63f5b6e74cf5e363877b17.jpeg)

### Why Won’t My Camera Connect After the Test?
- The **Test Connection** button checks HTTP settings only. Update your camera firmware, restart the device, or check your NAS firewall settings. Adjust firewall permissions under **Control Panel > Security > Firewall**.

### Surveillance Station Can’t Detect Your Camera:
- Ensure your camera is listed in the Synology-supported camera list.  
- Confirm the camera is connected to the same network as your NAS. The search function only works for devices on the same network.

### What If the Connection Test Fails?
- Verify that the correct camera type is selected in the installation menu.  
- Recheck the installation settings and retry the connection.

By following these steps and addressing common issues, you can seamlessly integrate your IP camera with your Synology NAS for secure and efficient surveillance.

---
