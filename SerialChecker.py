import winreg
import os, subprocess
import wmi, re
from Utilities import banner, write_registry_value, read_registry_value
import time
from colorama import init, Fore, Style, just_fix_windows_console
from pystyle import Colors, Colorate

# Initialize everything
init()
just_fix_windows_console()
c = wmi.WMI()

# Serial Checker handling
def get_csname():
    try:
        for os_info in c.Win32_OperatingSystem():
            if os_info.CSName: 
                return os_info.CSName
        return "Not Found"
    except Exception:
        return "Not Found"
    
def get_mbSerial():
    try:
        for board in c.Win32_BaseBoard():
            if board.SerialNumber and board.SerialNumber.strip():
                return board.SerialNumber.strip()
        for bio in c.Win32_BIOS():
            if bio.SerialNumber and bio.SerialNumber.strip():
                return bio.SerialNumber.strip()
        for prod in c.Win32_ComputerSystemProduct():
            if prod.IdentifyingNumber and prod.IdentifyingNumber.strip():
                return prod.IdentifyingNumber.strip()
        return "Not Found"
    except Exception:
        return "Not Found"
    
def get_cpuSerial():
    try:
        for cpu in c.Win32_Processor():
            serial = getattr(cpu, "SerialNumber", "").strip()
            if serial:
                return serial
        return "Not Found"
    except Exception:
        return "Not Found"
    
def get_volumeC(drive="C:"):
    try:
        out = subprocess.check_output(f"vol {drive}", shell=True, text=True, encoding='cp850')
        match = re.search(r"Volume Serial Number is ([0-9A-F\-]+)", out)
        if match: 
            return match.group(1)
        return "Not Found"
    except Exception:
        return "Not Found"
    
def get_diskSerial():
    try:
        for x in c.Win32_PhysicalMedia():
            if x.Tag and 'PHYSICALDRIVE0' in x.Tag.replace("\\", ""):
                if x.SerialNumber and x.SerialNumber.strip():
                    return x.SerialNumber.strip()
        return "Not Found"
    except Exception:
        return "Not Found"

def get_macAddress():
    try:
        for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=1):
            if interface.MACAddress: 
                return interface.MACAddress
        return "Not Found"
    except Exception:
        return "Not Found"
    
def get_uuid():
    try:
        lines = [l.strip() for l in subprocess.check_output("wmic csproduct get uuid", shell=True).decode().splitlines() if l.strip()]
        if len(lines) >= 2: 
            return lines[1]
        return "Not Found"
    except Exception:
        return "Not Found"
    
def get_tpm():
    cmd = [
        "powershell.exe",
        "-ExecutionPolicy", "Bypass",
        "-NoProfile",
        "-Command", "Get-Tpm"
    ]
    try:
        out = subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT)
        match = re.search(r"TpmEnabled\s*:\s*(True|False)", out)
        if match: 
            return "Enabled" if match.group(1) == "True" else "Disabled"
        return "Disabled"
    except subprocess.CalledProcessError:
        return "Disabled"
    
def get_secureBoot():
    try:
        out = subprocess.check_output(["powershell", "-Command", "Confirm-SecureBootUEFI"], text=True, stderr=subprocess.DEVNULL).strip()
        return "Enabled" if out == "True" else "Disabled"
    except subprocess.CalledProcessError:
        return "Disabled"

GREEN = "\033[32m"
RED   = "\033[31m"
RESET = "\033[0m"

def display_hwid(name, current_value):
    try:
        base_value = read_registry_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\CustomHWBackup", name)
    except:
        base_value = None
    
    if base_value is None:
        try:
            write_registry_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\CustomHWBackup", name, current_value)
            base_value = current_value
        except:
            base_value = current_value

    if name.strip() in ["TPM", "Secure Boot"]:
        if current_value == "Disabled":
            color = GREEN
        else:
            color = RED
        print(f"{name:<28} | {color}{current_value}{RESET}")
    else:
        if current_value != base_value:
            color = GREEN
            suffix = RESET + f" ← [{base_value}]"
        else:
            color = RED
            suffix = ""
        print(f"{name:<28} | {color}{current_value}{suffix}{RESET}")

# Banner
SERIALCHECKER_BANNER = Colorate.Diagonal(Colors.green_to_cyan, r"""
     ___ ___ ___ ___   _   _       ___ _  _ ___ ___ _  _____ ___ 
    / __| __| _ \_ _| /_\ | |     / __| || | __/ __| |/ / __| _ \
    \__ \ _||   /| | / _ \| |__  | (__| __ | _| (__| ' <| _||   /
    |___/___|_|_\___/_/_\_\____|  \___|_||_|___\___|_|\_\___|_|_\
     
    =============================================================

""", 1)

# Menu
def serialChecker_menu():
    while True:
        os.system("cls")
        os.system("title Serial Checker -- Made by Kiwai")
        banner(SERIALCHECKER_BANNER)
        print(f"    {Fore.YELLOW}[*]{Style.RESET_ALL} Please wait while we retrieve your HWIDs...\n")
        
        csname = get_csname()
        print("    ▓▓", end="", flush=True)
        time.sleep(0.1)
        
        mb_serials = get_mbSerial()
        print("▓▓", end="", flush=True)
        time.sleep(0.1)
        
        cpu_serial = get_cpuSerial()
        print("▓▓", end="", flush=True)
        time.sleep(0.1)
        
        volume_c = get_volumeC()
        print("▓▓", end="", flush=True)
        time.sleep(0.1)
        
        disk_serial = get_diskSerial()
        print("▓▓", end="", flush=True)
        time.sleep(0.1)
        
        mac_address = get_macAddress()
        print("▓▓", end="", flush=True)
        
        uuid = get_uuid()
        print("▓▓", end="", flush=True)
        
        tpm = get_tpm()
        print("▓▓", end="", flush=True)
        
        secureBoot = get_secureBoot()
        print("▓▓")
        
        print(f"\n    {Fore.GREEN}[+]{Style.RESET_ALL} Done! Here are your HWIDs:\n")
        os.system("cls")
        banner(SERIALCHECKER_BANNER)
        
        print("          Type               |       HWID                 ")
        print("    ─────────────────────────┼─────────────────────────────")
        
        display_hwid("     Computer Name", csname)
        display_hwid("     Motherboard Serial", mb_serials)
        display_hwid("     CPU Serial", cpu_serial)
        display_hwid("     Volume C", volume_c)
        display_hwid("     Disk Serial", disk_serial)
        display_hwid("     MAC Address", mac_address)
        display_hwid("     UUID", uuid)
        display_hwid("     TPM", tpm)
        display_hwid("     Secure Boot", secureBoot)

        print("\n    [E] Export your HWIDs to a text file")
        print("    [B] Back to Main Menu")
        print("    [Enter] Refresh HWIDs\n")
        choice = input("    > ").strip().lower()
        if choice == "e":
            os.system("cls")
            banner(SERIALCHECKER_BANNER)
            try:
                username = os.getlogin()
                filename = f"{username}'s HWIDs.txt"
                with open(filename, "w") as file:
                    file.write(f"""
Computer Name: {csname}
Motherboard Serial: {mb_serials}
CPU Serial: {cpu_serial}
Volume C: {volume_c}
Disk Serial: {disk_serial}
MAC Address: {mac_address}
UUID: {uuid}
TPM: {tpm}
Secure Boot: {secureBoot}""")
                    print(f"\n    {Fore.GREEN}[+]{Style.RESET_ALL} Done! Your HWIDs have been written to {filename}.")
            except Exception as e:
                print(f"\n    {Fore.RED}[-]{Style.RESET_ALL} Error: {e}")
            input("    Press Enter to go back to the Main Menu...")
            break
        elif choice == "b":
            break
