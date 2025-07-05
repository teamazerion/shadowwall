# 🛡️ ShadowWall - WiFi Threat Detector for Android-Termux

**ShadowWall** is a lightweight, open-source **WiFi threat detection tool** built for Android devices using **Termux**. It monitors for suspicious network activity, intrusion patterns, and potential surveillance threats like unknown devices or packet sniffers.

> ⚙️ Built for ethical hackers, students, security testers, and anyone needing real-time WiFi monitoring from their phone.

---

## 🌟 Features

- 🔍 Real-time detection of nearby suspicious networks or devices
- 📢 Voice alerts on threat detection (TTS-enabled)
- 📄 Logs threats with timestamps
- 🧠 Lightweight: Runs entirely in Termux (no root required)
- 🛠️ Customizable threat ID input and checks

---

## 📥 Installation

Open Termux and run:

```bash
pkg update && pkg upgrade
pkg install git python -y
git clone https://github.com/teamaze/shadowwall
cd shadowwall
chmod +x install.sh
./install.sh
