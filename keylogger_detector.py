import psutil
import os

# Common keylogger process name patterns (expand as needed)
SUSPECT_NAMES = ["keylogger", "hook", "spy", "inputlogger", "keyboardhook"]

def check_suspicious_processes():
    print("=== Suspicious Process Detector ===")

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pname = proc.info['name'].lower()
            for keyword in SUSPECT_NAMES:
                if keyword in pname:
                    print(f"[!] Suspicious process found: {pname} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def check_keyboard_access():
    print("\n=== Keyboard Hook Check (Basic) ===")
    # This is a placeholder for more advanced API hook detection
    print("Note: Advanced detection requires system-level tools (like C++ or PowerShell).")
    print("Try tools like Microsoft Sysinternals > Process Monitor or GMER for in-depth analysis.")

def main():
    check_suspicious_processes()
    check_keyboard_access()

if __name__ == "__main__":
    main()
