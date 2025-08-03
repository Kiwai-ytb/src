import subprocess, os
from colorama import Fore, Style
from pystyle import Colors, Colorate
from Utilities import banner


# HVCI handling
def set_hvci(on: bool) -> str:
    state = "1" if on else "0"
    cmds = [
        f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard" /v EnableVirtualizationBasedSecurity /t REG_DWORD /d {state} /f',
        f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard\\Scenarios\\HypervisorEnforcedCodeIntegrity" /v Enabled /t REG_DWORD /d {state} /f',
        f'bcdedit /set hypervisorlaunchtype {"auto" if on else "off"}'
    ]
    for cmd in cmds:
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return f"{Fore.GREEN}ENABLED{Style.RESET_ALL}" if on else f"{Fore.RED}DISABLED{Style.RESET_ALL}"

def get_hvci_status() -> str:
    try:
        out = subprocess.check_output(
            'reg query "HKLM\\SYSTEM\\CurrentControlSet\\Control\\DeviceGuard\\Scenarios\\HypervisorEnforcedCodeIntegrity" /v Enabled',
            shell=True, stderr=subprocess.DEVNULL
        ).decode()
        return f"{Fore.GREEN}ENABLED{Style.RESET_ALL}" if "0x1" in out else f"{Fore.RED}DISABLED{Style.RESET_ALL}"
    except subprocess.CalledProcessError:
        return "NOT SET (probably disabled)"
    
# Banners
HVCI_BANNER = Colorate.Diagonal(Colors.red_to_white, r"""
     _  ___   _____ ___   __  __                             
    | || \ \ / / __|_ _| |  \/  |__ _ _ _  __ _ __ _ ___ _ _ 
    | __ |\ V | (__ | |  | |\/| / _` | ' \/ _` / _` / -_| '_|
    |_||_| \_/ \___|___| |_|  |_\__,_|_||_\__,_\__, \___|_|  
                                                |___/         

    ==========================================================

    [1] Enable HVCI
    [2] Disable HVCI
    [3] Check HVCI Status
    [B] To go Back
""", 1)

HVCISMALL_BANNER = Colorate.Diagonal(Colors.red_to_white, r"""
     _  ___   _____ ___   __  __                             
    | || \ \ / / __|_ _| |  \/  |__ _ _ _  __ _ __ _ ___ _ _ 
    | __ |\ V | (__ | |  | |\/| / _` | ' \/ _` / _` / -_| '_|
    |_||_| \_/ \___|___| |_|  |_\__,_|_||_\__,_\__, \___|_|  
                                                |___/         

    ==========================================================
""", 1)

# Menu
def hvciManager_menu():
    while True:
        os.system("cls")
        os.system("title HVCI Control -- Made by Kiwai")
        banner(HVCI_BANNER)
        choice = input("    > ").strip().lower()
        if choice == "1":
            banner(HVCISMALL_BANNER)
            res = set_hvci(True)
            print(f"   {Fore.GREEN}[+]{Style.RESET_ALL} HVCI {res}, reboot required.")
        elif choice == "2":
            banner(HVCISMALL_BANNER)
            res = set_hvci(False)
            print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} HVCI {res}, reboot required.")
        elif choice == "3":
            banner(HVCISMALL_BANNER)
            status = get_hvci_status()
            print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} HVCI is {status}")
        elif choice == "b":
            break
        else:
            banner(HVCI_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice.")
        input("\n    Press Enter to continue...")