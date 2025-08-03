import os, base64
from colorama import Fore, Style
from pystyle import Colors, Colorate
from Utilities import banner, resize_and_center_console, easterEgg_Xpt00, easterEgg_Doralexplosion

# Banners
SIMPLE_CREDITS_BANNER = Colorate.Diagonal(Colors.blue_to_red, r"""
      ___            _ _ _      
     / __|_ _ ___ __| (_) |_ ___
    | (__| '_/ -_) _` | |  _(_-<
     \___|_| \___\__,_|_|\__/__/

    ============================
""", 1)

ALL_CREDITS_BANNER = Colorate.Diagonal(Colors.blue_to_red, r"""
      ___            _ _ _      
     / __|_ _ ___ __| (_) |_ ___
    | (__| '_/ -_) _` | |  _(_-<
     \___|_| \___\__,_|_|\__/__/

    ============================

    This Tool as only been made by myself aka Kiwai, I did it only for fun, it is not intented to be shared but if it is,
    I hope it is useful and works welln shared with <3.
    
    Here are some of my links:
              
    |-> Github: https://github.com/Kiwai-ytb/
    |-> Discord: kiwai_yt or midasdefn

    [B] Back to Main Menu
""", 1)

# Menu
def credits_menu():
    while True:
        os.system("cls")
        os.system("title Credits -- Made by Kiwai")
        banner(ALL_CREDITS_BANNER)
        choice = input("    > ").strip().lower()
        if choice == "xpt00" or choice == "rayan":
            resize_and_center_console(152, 30)
            banner(SIMPLE_CREDITS_BANNER)
            print(base64.b64decode(easterEgg_Xpt00).decode("utf-8"))
        elif choice == "doralexplosion" or choice == "célestin":
            resize_and_center_console(154, 30)
            banner(SIMPLE_CREDITS_BANNER)
            print(base64.b64decode(easterEgg_Doralexplosion).decode("utf-8"))
        elif choice == "b":
            break
        else:
            banner(ALL_CREDITS_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice.")
        input("\n    Press Enter to go back...")