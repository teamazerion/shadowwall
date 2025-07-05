# 🛡️ ShadowWall — WiFi Threat Detector for Termux

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-green.svg)

**ShadowWall** is a Termux-based lightweight **WiFi threat detection firewall** designed for Android users. It actively monitors your local network for suspicious devices and alerts you using text-to-speech voice warnings and logs.

---

## 🚀 Features

- 📡 Detects suspicious IPs in real-time
- 🎙️ Voice alert (TTS) on threat detection
- 📄 Logs activity for review
- 📱 Works 100% on Android with Termux
- ⚡ Fast, lightweight, and easy to use

---

## 📋 Requirements

- Android phone with Termux
- Packages:
  - `git`, `python`, `espeak`, `termux-api`
- Python libraries:
  - `scapy`, `termcolor`

---

## 📦 Installation

Open **Termux** and run:

```bash
pkg update && pkg upgrade
pkg install git python espeak termux-api -y
git clone https://github.com/teamazerion/shadowwall
cd shadowwall
chmod +x install.sh
./install.sh

---

## 📸 Screenshot

Here’s ShadowWall running inside Termux:

![ShadowWall Banner](https://github.com/teamazerion/shadowwall/blob/main/Screenshot_20250705_232342_Termux.jpg?raw=true)


