# Installing PythOS

You can run PythOS as a live system or install it on a device for full performance and customization.

## 💻 Requirements

- x86_64 machine or Raspberry Pi
- USB drive (for live boot)
- 2GB RAM minimum (4GB recommended)
- Internet connection (for updates)

## 🔧 Installation Steps

### 1. Download ISO

Visit the [official website](https://pythos.pages.dev) and download the latest ISO or image file.

### 2. Flash to USB

Use [balenaEtcher](https://etcher.io) or the `dd` command to flash the image onto your USB drive.

```bash
sudo dd if=pythos.iso of=/dev/sdX bs=4M status=progress
