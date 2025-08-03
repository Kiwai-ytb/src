import subprocess, os
from colorama import Fore, Style
from pystyle import Colors, Colorate
from Utilities import banner

# Vulnerable Driver Blocklist handling
def set_blocklist(on: bool) -> str:
    state = "1" if on else "0"
    cmd = [
        "reg", "add", r"HKLM\SYSTEM\CurrentControlSet\Control\CI\Config",
        "/v", "VulnerableDriverBlocklistEnable",
        "/t", "REG_DWORD", "/d", state, "/f"
    ]
    rc = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    return f"{Fore.GREEN}ENABLED{Style.RESET_ALL}" if on and rc == 0 else f"{Fore.RED}DISABLED{Style.RESET_ALL}" if not on and rc == 0 else "ERROR"

def get_blocklist_status() -> str:
    try:
        out = subprocess.check_output(
            'reg query "HKLM\\SYSTEM\\CurrentControlSet\\Control\\CI\\Config" /v VulnerableDriverBlocklistEnable',
            shell=True, stderr=subprocess.DEVNULL
        ).decode()
        return f"{Fore.GREEN}ENABLED{Style.RESET_ALL}" if "0x1" in out else f"{Fore.RED}DISABLED{Style.RESET_ALL}"
    except subprocess.CalledProcessError:
        return "NOT SET (probably disabled)"

# Banners
VULNERABLEDRIVERBLOCKLIST_BANNER = Colorate.Diagonal(Colors.red_to_yellow, r"""
    __   __    _                   _    _       ___      _               ___ _        _   _ _    _   
    \ \ / _  _| |_ _  ___ _ _ __ _| |__| |___  |   \ _ _(___ _____ _ _  | _ | |___ __| |_| (_)__| |_ 
     \ V | || | | ' \/ -_| '_/ _` | '_ | / -_) | |) | '_| \ V / -_| '_| | _ | / _ / _| / | | (_-|  _|
      \_/ \_,_|_|_||_\___|_| \__,_|_.__|_\___| |___/|_| |_|\_/\___|_|   |___|_\___\__|_\_|_|_/__/\__|
     __  __                                                                                          
    |  \/  |__ _ _ _  __ _ __ _ ___ _ _                                                              
    | |\/| / _` | ' \/ _` / _` / -_| '_|                                                             
    |_|  |_\__,_|_||_\__,_\__, \___|_|                                                               
                          |___/                                                                      

    =================================================================================================

    [1] Enable Blocklist
    [2] Disable Blocklist
    [3] Check Blocklist Status
    [B] Back to Main Menu
""", 1)

VULNERABLEDRIVERBLOCKLISTSMALL_BANNER = Colorate.Diagonal(Colors.red_to_yellow, r"""
    __   __    _                   _    _       ___      _               ___ _        _   _ _    _   
    \ \ / _  _| |_ _  ___ _ _ __ _| |__| |___  |   \ _ _(___ _____ _ _  | _ | |___ __| |_| (_)__| |_ 
     \ V | || | | ' \/ -_| '_/ _` | '_ | / -_) | |) | '_| \ V / -_| '_| | _ | / _ / _| / | | (_-|  _|
      \_/ \_,_|_|_||_\___|_| \__,_|_.__|_\___| |___/|_| |_|\_/\___|_|   |___|_\___\__|_\_|_|_/__/\__|
     __  __                                                                                          
    |  \/  |__ _ _ _  __ _ __ _ ___ _ _                                                              
    | |\/| / _` | ' \/ _` / _` / -_| '_|                                                             
    |_|  |_\__,_|_||_\__,_\__, \___|_|                                                               
                          |___/                                                                      

    ==================================================================================================
""", 1)

# Menu
def vulnerableDriverBlocklist_menu():
    while True:
        os.system("cls")
        os.system("title Vulnerable Driver Blocklist -- Made by Kiwai")
        banner(VULNERABLEDRIVERBLOCKLIST_BANNER)
        choice = input("    > ").strip().lower()
        if choice == "1":
            banner(VULNERABLEDRIVERBLOCKLISTSMALL_BANNER)
            res = set_blocklist(True)
            print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} Blocklist {res}, reboot recommended.")
        elif choice == "2":
            banner(VULNERABLEDRIVERBLOCKLISTSMALL_BANNER)
            res = set_blocklist(False)
            print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} Blocklist {res}, reboot recommended.")
        elif choice == "3":
            banner(VULNERABLEDRIVERBLOCKLISTSMALL_BANNER)
            status = get_blocklist_status()
            print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} Blocklist status: {status}")
        elif choice == "b":
            break
        else:
            banner(VULNERABLEDRIVERBLOCKLIST_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice.")
        input("\n    Press Enter to continue...")