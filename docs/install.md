# 🧹 Installing PythOS

Welcome! This guide walks you through installing **PythOS**, whether you're trying it out in Live mode or setting it up on real hardware.

---

## ✅ Requirements

Before installing, make sure your device meets these minimum specs:

* **CPU**: x86\_64 (ARM chips coming soon ~)
* **RAM**: 512 MiB (4 GiB+ recommended)
* **Storage**: at least 20 GiB minimum (50 GiB+ recommended)
* **Bootable USB**, **DVD-R** or **SD card** (2 GB+)
* **Internet**: Necessary (As long as you have internet, you're good to go)

---

## 📅 Step 1: Download PythOS

Head over to the [official PythOS site](https://pythos.pages.dev) and download the latest image:

* `.iso` for PCs and virtual machines
---

## 📁 Step 2: Create Bootable Media

Use one of the following tools:

### Option A: balenaEtcher (GUI)

1. Open [balenaEtcher](https://etcher.io) and download
2. Select the PythOS.iso
3. Choose your USB drive
4. Click **Flash**

### Option B: Rufus (Windows)

1. Open [rufus](https://rufus.ie) and download
2. Select PythOS.iso
3. Choose your flash drive
4. Click **Start**

### Option C: `dd` (Linux/macOS Terminal)

```bash
sudo dd if=pythos.iso of=/dev/sdX bs=4M status=progress && sync
```

> Replace `/dev/sdX` with the correct device (e.g., `/dev/sdb`). Be careful — this will erase the target drive.

---

## 🚀 Step 3: Boot Into PythOS

1. Insert your bootable drive
2. Restart your device
3. Enter the BIOS/boot menu (usually `F2` `F12`, `Esc`, or `Del`)
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
   * Choose mount point (select or type "/")
   * Confirm and install

⚠️ **Warning**: Installing will erase the selected disk.

---

Need help? Visit the [PythOS GitHub Discussions](https://github.com/pythos-os) or join our community chat (coming soon).
