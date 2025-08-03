import os
from colorama import Fore, Style
from pystyle import Colors, Colorate
from Utilities import banner, resize_and_center_console
from HVCIManager import hvciManager_menu
from VulnerableDriverBlocklist import vulnerableDriverBlocklist_menu
from HardwareNameSpoofer import hardwareNameSpoofer_menu
from SerialChecker import serialChecker_menu
from DiscordStuff import webhookSpammer_menu, webhookDestroyer_menu, webhookStatusChecker_menu, idToFirstTokenPart_menu
from Credits import credits_menu

#Banners
MAIN_BANNER = Colorate.Diagonal(Colors.blue_to_purple, r"""
    __      __   _                    _         _  ___             _ _                           
    \ \    / /__| |__ ___ _ __  ___  | |_ ___  | |/ (_)_ __ ____ _(_| )___                       
     \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \ | ' <| \ V  V / _` | |/(_-<                       
      \_/\_/\___|_\__\___/_|_|_\___|  \__\___/ |_|\_\_|\_/\_/\__,_|_| /__/  _    _____         _ 
     / _ \__ __ ___ _   | _ \_  _ _ _ _ __  ___ ___ ___  |  \/  |_  _| | |_(_)__|_   _|__  ___| |
    | (_) \ V  V / ' \  |  _/ || | '_| '_ \/ _ (_-</ -_) | |\/| | || | |  _| |___|| |/ _ \/ _ \ |
     \___/ \_/\_/|_||_| |_|  \_,_|_| | .__/\___/__/\___| |_|  |_|\_,_|_|\__|_|    |_|\___/\___/_|
                                     |_|                                                         

    =============================================================================================

    [1] HVCI & Vulnerable Driver Blocklist Managers
    [2] Discord Webhooks
    [3] Misc
    [C] Credits
    [Q] Quit
""", 1)

HVCIVULNERABLEDRIVERBLOCKLIST_BANNER = Colorate.Diagonal(Colors.blue_to_red, r"""
     _  ___   _____ ___   __                                                                         
    | || \ \ / / __|_ _| / _|___                                                                     
    | __ |\ V | (__ | |  > _|_ _|                                                                    
    |_||_| \_/ \___|___| \_____|                                                                     

    __   __    _                   _    _       ___      _               ___ _        _   _ _    _   
    \ \ / _  _| |_ _  ___ _ _ __ _| |__| |___  |   \ _ _(___ _____ _ _  | _ | |___ __| |_| (_)__| |_ 
     \ V | || | | ' \/ -_| '_/ _` | '_ | / -_) | |) | '_| \ V / -_| '_| | _ | / _ / _| / | | (_-|  _|
      \_/ \_,_|_|_||_\___|_| \__,_|_.__|_\___| |___/|_| |_|\_/\___|_|   |___|_\___\__|_\_|_|_/__/\__|

    =================================================================================================

    [1] HVCI Manager
    [2] Vulnerable Driver Blocklist Manager
    [B] Back to Main Menu
""", 1)

DISCORDWEBHOOKS_BANNER = Colorate.Diagonal(Colors.blue_to_cyan, r"""
     ___  _                  _   ___ _         __  __ 
    |   \(_)_____ ___ _ _ __| | / __| |_ _  _ / _|/ _|
    | |) | (_-/ _/ _ | '_/ _` | \__ |  _| || |  _|  _|
    |___/|_/__\__\___|_| \__,_| |___/\__|\_,_|_| |_|  
    
    ===========================

    [1] Webhook Spammer
    [2] Webhook Destroyer
    [3] Webhook Status Checker
    [4] ID to First Token Part
    [B] Back to Main Menu
""", 1)

MISC_BANNER = Colorate.Diagonal(Colors.blue_to_green, r"""
     __  __ _       
    |  \/  (_)_____ 
    | |\/| | (_-/ _|
    |_|  |_|_/__\__|    

    =======================

    [1] Serial Checker
    [2] Hardware Name Spoofer
    [B] Back to Main Menu                  
""", 1)

# Main Menu
def main_menu():
    while True:
        resize_and_center_console(150, 30)
        os.system("cls")
        os.system("title Kiwai's Own Purpose Multi-Tool -- Made by Kiwai")
        banner(MAIN_BANNER)
        choice = input("    > ").strip().lower()
        if choice == "1":
            while True:
                os.system("cls")
                os.system("title HVCI & Vulnerable Driver Blocklist Managers -- Made by Kiwai")
                banner(HVCIVULNERABLEDRIVERBLOCKLIST_BANNER)
                choice = input("    > ").strip().lower()
                if choice == "1":
                    hvciManager_menu()
                elif choice == "2":
                    vulnerableDriverBlocklist_menu()
                elif choice == "b":
                    break
                else:
                    banner(HVCIVULNERABLEDRIVERBLOCKLIST_BANNER)
                    print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice.")
                    input("\n    Press Enter to go back...")
        elif choice == "2":
            while True:
                os.system("cls")
                os.system("title Discord Stuff -- Made by Kiwai")
                banner(DISCORDWEBHOOKS_BANNER)
                choice = input("    > ").strip().lower()
                if choice == "1":
                    webhookSpammer_menu()
                elif choice == "2":
                    webhookDestroyer_menu()
                elif choice == "3":
                    webhookStatusChecker_menu()
                elif choice == "4":
                    idToFirstTokenPart_menu()
                elif choice == "b":
                    break
                else:
                    banner(DISCORDWEBHOOKS_BANNER)
                    print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice.")
                    input("\n    Press Enter to go back...")
        elif choice == "3":
            while True:
                os.system("cls")
                os.system("title Misc -- Made by Kiwai")
                banner(MISC_BANNER)
                choice = input("    > ").strip().lower()
                if choice == "1":
                    serialChecker_menu()
                elif choice == "2":
                    hardwareNameSpoofer_menu()
                elif choice == "b":
                    break
                else:
                    banner(MISC_BANNER)
                    print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice.")
                    input("\n    Press Enter to go back...")
        elif choice == "c":
            credits_menu()
        elif choice == "q":
            break
        else:
            banner(MAIN_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice.")
            input("\n    Press Enter to go back...")

if __name__ == "__main__":
    main_menu()