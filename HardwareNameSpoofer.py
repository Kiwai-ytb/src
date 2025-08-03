import os, winreg
from colorama import Fore, Style
from pystyle import Colors, Colorate
from Utilities import banner, read_registry_value, write_registry_value

# Hardware Spoofer handling
def backup_cpu_name():
    cpu_path = r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
    cpu_name = read_registry_value(winreg.HKEY_LOCAL_MACHINE, cpu_path, "ProcessorNameString")
    if cpu_name:
        write_registry_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\CustomHWBackup", "CPU", cpu_name)

def spoof_cpu_name(fake_name):
    cpu_path = r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"
    write_registry_value(winreg.HKEY_LOCAL_MACHINE, cpu_path, "ProcessorNameString", fake_name)

def restore_cpu_name():
    original_cpu = read_registry_value(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\CustomHWBackup", "CPU")
    if original_cpu:
        spoof_cpu_name(original_cpu)

def delete_backup():
    try:
        winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\CustomHWBackup")
    except FileNotFoundError:
        pass

# Banners
HARDWARESPOOFER_BANNER = Colorate.Diagonal(Colors.green_to_white, r"""
     _  _                                _  _                  ___               __         
    | || |__ _ _ ___ __ ____ _ _ _ ___  | \| |__ _ _ __  ___  / __|_ __ ___ ___ / _|___ _ _ 
    | __ / _` | '_\ V  V / _` | '_/ -_) | .` / _` | '  \/ -_) \__ | '_ / _ / _ |  _/ -_| '_|
    |_||_\__,_|_|  \_/\_/\__,_|_| \___| |_|\_\__,_|_|_|_\___| |___| .__\___\___|_| \___|_|  
                                                                  |_|                       
    ========================================================================================

    [1] Spoof CPU Name
    [2] Restore Original CPU Name
    [3] Delete Backup Key
    [B] Back to Main Menu
""", 1)

HARDWARESPOOFERSMALL_BANNER = Colorate.Diagonal(Colors.green_to_white, r"""
     _  _                                _  _                  ___               __         
    | || |__ _ _ ___ __ ____ _ _ _ ___  | \| |__ _ _ __  ___  / __|_ __ ___ ___ / _|___ _ _ 
    | __ / _` | '_\ V  V / _` | '_/ -_) | .` / _` | '  \/ -_) \__ | '_ / _ / _ |  _/ -_| '_|
    |_||_\__,_|_|  \_/\_/\__,_|_| \___| |_|\_\__,_|_|_|_\___| |___| .__\___\___|_| \___|_|  
                                                                  |_|                       
    =========================================================================================
""", 1)

# Menu
def hardwareNameSpoofer_menu():
    while True:
        os.system("cls")
        os.system("title Hardware Spoofer -- Made by Kiwai")
        banner(HARDWARESPOOFER_BANNER)
        choice = input("    > ").strip().lower()
        if choice == "1":
            banner(HARDWARESPOOFERSMALL_BANNER)
            fake_name = input(f"    {Fore.CYAN}[!]{Style.RESET_ALL} Enter the New CPU name: ")
            backup_cpu_name()
            spoof_cpu_name(fake_name)
            banner(HARDWARESPOOFERSMALL_BANNER)
            print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} CPU name spoofed to: {fake_name}! Re-open Task Manager to apply.")
        elif choice == "2":
            banner(HARDWARESPOOFERSMALL_BANNER)
            restore_cpu_name()
            print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} CPU Name restored! Re-open Task Manager to apply.")
        elif choice == "3":
            banner(HARDWARESPOOFERSMALL_BANNER)
            input(f"    {Fore.YELLOW}[*]{Style.RESET_ALL} Be careful, if you did not recover your CPU name before deleting it, you might not be able to restore it.\nPress Enter to continue...")
            delete_backup()
            print(f"\n    {Fore.GREEN}[+]{Style.RESET_ALL} Backup key deleted.")
        elif choice == "b":
            break
        else:
            banner(HARDWARESPOOFERSMALL_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice.")
        input("\n    Press Enter to continue...")