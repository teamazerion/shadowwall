#!/data/data/com.termux/files/usr/bin/bash

echo "🔥 ShadowWall Installer by Team Azerion 🔒"
echo "------------------------------------------"

echo "[1] Updating packages..."
pkg update -y && pkg upgrade -y

echo "[2] Installing Python, Git, Nmap..."
pkg install python git nmap -y

echo "[3] Cloning ShadowWall repo..."
cd ~
rm -rf shadowwall
git clone https://github.com/teamazerion/shadowwall.git

cd shadowwall || exit

echo "[4] Running ShadowWall..."
python shadowwall.py
