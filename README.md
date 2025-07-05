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

## 🚀 Usage

Once installed, follow these steps to run ShadowWall:

### 🔹 Step 1: Open Termux and navigate to the folder
```bash
cd shadowwall
Step 2: Start the ShadowWall program

python shadowwall.py

🔹 Step 3: Enter Suspicious Device ID

You'll be asked to enter a suspicious MAC address, IP address, or custom threat ID to monitor. Example:

Enter suspicious ID to monitor: 192.168.1.100

🔹 Step 4: Let it Monitor

ShadowWall will continuously scan the network.

If a matching threat is detected:

📢 Voice alert will play

📄 Threat will be logged



🛑 Stop the scan

Press:

Ctrl + C

to stop scanning and exit.

✅ Tip: You can run it in the background with:

nohup python shadowwall.py &
---

## 🏢 About Us — Azerion HQ

**Azerion HQ** is an independent cybersecurity and tech innovation company based in India. We specialize in:

- 🔐 Cybersecurity tools & ethical hacking solutions
- 🤖 App development (Android & Termux-based automation)
- 🧬 Bioscience & research projects (via @azerionhqforbioscience)
- 📱 Tech innovation for mobile platforms (via @azerionhqforappdevolpment)

We are dedicated to building lightweight, accessible tools that protect user privacy and enhance mobile security.

🔗 Follow us on Instagram:
- Main: [@teamazerion](https://instagram.com/teamazerion)
- Bioscience: [@azerionhqforbioscience](https://instagram.com/azerionhqforbioscience)
- App Dev: [@azerionhqforappdevolpment](https://instagram.com/azerionhqforappdevolpment)

📧 Business inquiries: teamazerion@protonmail.com





