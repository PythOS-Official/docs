# 🧹 Installing PythOS

Welcome! This guide walks you through installing **PythOS**, whether you're trying it out in Live mode or setting it up on real hardware.

---

## ✅ Requirements

Before installing, make sure your device meets these minimum specs:

* **CPU**: x86\_64 or ARM (Raspberry Pi supported)
* **RAM**: 2 GB (4 GB recommended)
* **Storage**: 4 GB minimum (8 GB recommended)
* **Bootable USB** or SD card (4 GB+)
* **Internet**: optional but recommended for updates

---

## 📅 Step 1: Download PythOS

Head over to the [official PythOS site](https://pythos.pages.dev) and download the latest image:

* `.iso` for PCs and virtual machines
* `.img` for Raspberry Pi and ARM devices

---

## 📁 Step 2: Create Bootable Media

Use one of the following tools:

### Option A: balenaEtcher (GUI)

1. Open [balenaEtcher](https://etcher.io)
2. Select the PythOS image
3. Choose your USB drive
4. Click **Flash**

### Option B: `dd` (Linux/macOS Terminal)

```bash
sudo dd if=pythos.iso of=/dev/sdX bs=4M status=progress && sync
```

> Replace `/dev/sdX` with the correct device (e.g., `/dev/sdb`). Be careful — this will erase the target drive.

---

## 🚀 Step 3: Boot Into PythOS

1. Insert your bootable drive
2. Restart your device
3. Enter the BIOS/boot menu (usually `F12`, `Esc`, or `Del`)
4. Select the USB drive

You’ll see the PythOS boot menu:

```
[ Boot PythOS ]
[ Boot the next volume ]
```

Choose **Boot PythOS** to start the system.

---

## 💻 Step 4: Install to Disk (Optional)

If you want to install PythOS permanently:

1. Boot into Live mode
2. Follow on-screen instructions:

   * Select target disk
   * Choose automatic or custom partitioning
   * Confirm and install

⚠️ **Warning**: Installing will erase the selected disk.

---

Need help? Visit the [PythOS GitHub Discussions](https://github.com/pythos-os) or join our community chat (coming soon).
