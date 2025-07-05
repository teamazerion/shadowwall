# 🛡️ ShadowWall — WiFi Threat Detector for Termux

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-green.svg)

**ShadowWall** is a Termux-based lightweight **WiFi threat detection firewall** built for Android. It helps you detect and block suspicious IP addresses with real-time alerts using voice and text.

---

## 🚀 Features

- 🧠 Detects suspicious IP addresses in real-time
- 🎙️ Voice alerts using `espeak` / `termux-tts-speak`
- 📄 Logs for activity monitoring
- 💻 Simple terminal UI
- ⚡ Works offline and fast on any Android via Termux

---

## 📋 Requirements

- Android phone with [Termux](https://f-droid.org/en/packages/com.termux/)
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
