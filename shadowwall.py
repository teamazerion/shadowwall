import os
import time
import threading

# ==============================
# 🔐 SHADOWWALL FIREWALL SYSTEM
# 🛡 Developed by: TEAM AZERION
# 📲 Instagram: @teamazerion
# ==============================

log_file = "shadowwall_log.txt"
banned_ips = []

# 🔥 TEAM AZERION BANNER 🔥
def show_banner():
    print("\033[1;91m")  # Red bold text
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃ 🔐 SHADOWWALL - ACTIVE DEFENSE FIREWALL    ┃")
    print("┃                                            ┃")
    print("┃ 👨‍💻 Developed by: TEAM AZERION              ┃")
    print("┃ 📲 Instagram: @teamazerion                 ┃")
    print("┃ 🛡 Protecting Your Device from Threats     ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print("\033[0m")  # Reset colors

# 🎤 Non-blocking voice output
def speak(text):
    threading.Thread(target=lambda: os.system(f'termux-tts-speak "{text}"')).start()

# 🚫 Block suspicious IP
def block_ip(ip):
    if ip not in banned_ips:
        banned_ips.append(ip)
        with open(log_file, "a") as f:
            f.write(f"[{time.ctime()}] Blocked IP by Team Azerion: {ip}\n")
        print(f"🚨 Blocked IP: {ip}")
        speak(f"Blocked suspicious IP {ip} by Team Azerion firewall")
    else:
        print("⚠️ IP already blocked.")

# 🚀 Main function
def main():
    show_banner()
    speak("ShadowWall by Team Azerion is now monitoring threats.")
    print("🛡️ Enter suspicious IPs to block them. Press Ctrl+C to exit.\n")

    while True:
        try:
            ip = input("Enter suspicious IP: ").strip()
            if ip:
                block_ip(ip)
        except KeyboardInterrupt:
            print("\n🛑 Exiting ShadowWall. Stay protected! 🛡️")
            break

# Run
main()
