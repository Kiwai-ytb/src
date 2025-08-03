import os, time, json, requests, random, base64
from colorama import Fore, Style
from pystyle import Colors, Colorate
from Utilities import banner, id_generator

# Webhook Spammer handling
def webhookSpammer(webhook_url):
    send_count = 0

    profile_pictures = ["https://media.craiyon.com/2025-04-14/aBeNQ-bqRuC-YKZwS9ZHZQ.webp",
                        "https://i.pinimg.com/736x/2d/38/9a/2d389a89803d9494b5e59aa10e70f2fe.jpg",
                        "https://media.printler.com/media/photo/175046-1.jpg?rmode=crop&width=638&height=900",
                        "https://scontent-mrs2-1.cdninstagram.com/v/t51.2885-15/474014829_18062238865914201_6408834800685720635_n.webp?efg=eyJ2ZW5jb2RlX3RhZyI6IkZFRUQuaW1hZ2VfdXJsZ2VuLjE0NDB4MTQ0MC5zZHIuZjc1NzYxLmRlZmF1bHRfaW1hZ2UuYzIifQ&_nc_ht=scontent-mrs2-1.cdninstagram.com&_nc_cat=109&_nc_oc=Q6cZ2QFx5hyyFUP2Bi8rJAMfDvwPaz-JBwUbgvfP6fv6EbO5gDumrSfWE6TaVr6ha-MrctimhCzO3cxqtm6mE-B3gc8v&_nc_ohc=SX6E-KJjzX4Q7kNvwFyddg5&_nc_gid=4pZxXns1sOapEeCADIxPpQ&edm=APs17CUBAAAA&ccb=7-5&ig_cache_key=MzU1NDg3ODQxMDM1MzIzNTA1NA%3D%3D.3-ccb7-5&oh=00_AfRVVUi38QLbeS6og-hdWr4WmEh-s45GxzIQxBaAK6lXMw&oe=688C7AB8&_nc_sid=10d13b",
                        "https://boo-prod.b-cdn.net/database/profiles/169383729996999c896e4bec71bb24a1b6174c15584df.jpg",
                        "https://static1.cbrimages.com/wordpress/wp-content/uploads/2023/01/marin-kitagawa-from-my-dress-up-darling.jpg",
                        "https://static.wikia.nocookie.net/shigatsu-wa-kimi-no-uso/images/c/c5/Kaori_Miyazono_Infobox.png/revision/latest?cb=20200330204003",
                        "https://www.nautiljon.com/images/perso/00/80/hori_kyoko_19908.webp",
                        "https://www.japanpowered.com/media/images/shikimori-cutie.png",
                        "https://cdn.rafled.com/anime-icons/images/B6OLUJzyBgqnxfQdfAJRveCGjFHhX0eE.jpg",
                        "https://animotaku.fr/wp-content/uploads/2024/09/anime-alya-sometimes-hides-her-feelings-in-russian-saison-2-annonce.jpg",
                        "https://yt3.googleusercontent.com/zNp0b-1XrCOR_JJ2sVXdw36CkImS3yo_zfUcG8Ip67FafeydoM9BkSe2eBeCInuzs5heIaBJZuE=s900-c-k-c0x00ffffff-no-rj",
                        "https://static.wikia.nocookie.net/remixfavoriteshowandgame/images/c/c9/Sakura_Yamauchi.png/revision/latest?cb=20201210172033",
                        
    ]

    username = input(f"    {Fore.CYAN}[!]{Style.RESET_ALL} Enter the Username or Leave Empty for Random: ")
    if username == "":
        username = "random"

    while True:
        os.system("cls")
        banner(WEBHOOKSPAMMERSMALL_BANNER)
        message = input(f"    {Fore.CYAN}[!]{Style.RESET_ALL} Enter the Message to Spam: ")
        if message == "":
            print(f"\n    {Fore.RED}[-]{Style.RESET_ALL} Message cannot be empty.")
            input("\n    Press Enter to go Back")
        else:
            break

    try:
        banner(WEBHOOKSPAMMERSMALL_BANNER)
        while True:
            if username == "random":
                username = id_generator(80)

            profile_picture = random.choice(profile_pictures)

            data = json.dumps({
                "content": message,
                "username": username,
                "avatar_url": profile_picture,
                "tts": False
            })
            header = {"content-type": "application/json"}

            response = requests.post(webhook_url, data, headers=header)

            if response.status_code == 204 or response.ok:
                send_count += 1
                print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} Message Sent {send_count} times.")
            elif response.status_code == 429:
                retry_after = response.json().get("retry_after", 2)
                print(f"    {Fore.YELLOW}[*]{Style.RESET_ALL} Rate limited. Waiting {retry_after:.2f}s...")
                time.sleep(retry_after)
                continue
            else:
                print(f"    {Fore.RED}[-]{Style.RESET_ALL} Failed to send message (status {response.status_code}, text: {response.text})")
                time.sleep(2)
                continue

            time.sleep(0.1)

    except KeyboardInterrupt:
        print(f"\n    {Fore.YELLOW}[*]{Style.RESET_ALL} Spamming stopped.")
        input("    Press Enter to go Back...")


# Webhook Destroyer handling
def webhookDestroyer(webhook_url):
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} Webhook Destroyed.")
    else:
        print(f"    {Fore.RED}[-]{Style.RESET_ALL} Error: {response.status_code}, text: {response.text}")
    input("\n    Press Enter to go Back...")

# Webhook Status Checker handling
def webhookStatus(webhook_url):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        webhook_info = response.json()
        print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} Webhook exist:\n\n {webhook_info}")
    elif response.status_code == 404:
        print(f"    {Fore.RED}[-]{Style.RESET_ALL} Webhooh doesn't exist.")
    else:
        print(f"    {Fore.RED}[-]{Style.RESET_ALL} Error: {response.status_code}, text: {response.text}")
    input("\n    Press Enter to go Back...")

# ID To First Token Part handling
def idToFirstTokenPart(id):
    encodedId = base64.b64encode(id.encode("utf-8"))
    firstTokenPart = str(encodedId, "utf-8")
    print(f"    {Fore.GREEN}[+]{Style.RESET_ALL} First Token Part of User ID {id}: {firstTokenPart}")
    input("\n    Press Enter to go Back...")

# Banners
WEBHOOKSPAMMER_BANNER = Colorate.Diagonal(Colors.blue_to_cyan, r"""
    __      __   _    _            _     ___                               
    \ \    / ___| |__| |_  ___ ___| |__ / __|_ __ __ _ _ __  _ __  ___ _ _ 
     \ \/\/ / -_| '_ | ' \/ _ / _ | / / \__ | '_ / _` | '  \| '  \/ -_| '_|
      \_/\_/\___|_.__|_||_\___\___|_\_\ |___| .__\__,_|_|_|_|_|_|_\___|_| 
                                            |_|                            
                                                          
    ========================================================================

    [B] To go Back
    [*] Or Enter the Webhook Url
""", 1)

WEBHOOKSPAMMERSMALL_BANNER = Colorate.Diagonal(Colors.blue_to_cyan, r"""
    __      __   _    _            _     ___                               
    \ \    / ___| |__| |_  ___ ___| |__ / __|_ __ __ _ _ __  _ __  ___ _ _ 
     \ \/\/ / -_| '_ | ' \/ _ / _ | / / \__ | '_ / _` | '  \| '  \/ -_| '_|
      \_/\_/\___|_.__|_||_\___\___|_\_\ |___| .__\__,_|_|_|_|_|_|_\___|_| 
                                            |_|                            
                                                          
    ========================================================================
""", 1)

WEBHOOKDESTROYER_BANNER = Colorate.Diagonal(Colors.blue_to_black, r"""
    __      __   _    _            _     ___         _                        
    \ \    / ___| |__| |_  ___ ___| |__ |   \ ___ __| |_ _ _ ___ _  _ ___ _ _ 
     \ \/\/ / -_| '_ | ' \/ _ / _ | / / | |) / -_(_-|  _| '_/ _ | || / -_| '_|
      \_/\_/\___|_.__|_||_\___\___|_\_\ |___/\___/__/\__|_| \___/\_, \___|_|  
                                                                 |__/    

    ===========================================================================

    [B] To go Back
    [*] Or Enter the Webhook Url
""", 1)

WEBHOOKDESTROYERSMALL_BANNER = Colorate.Diagonal(Colors.blue_to_black, r"""
    __      __   _    _            _     ___         _                        
    \ \    / ___| |__| |_  ___ ___| |__ |   \ ___ __| |_ _ _ ___ _  _ ___ _ _ 
     \ \/\/ / -_| '_ | ' \/ _ / _ | / / | |) / -_(_-|  _| '_/ _ | || / -_| '_|
      \_/\_/\___|_.__|_||_\___\___|_\_\ |___/\___/__/\__|_| \___/\_, \___|_|  
                                                                 |__/    

    ===========================================================================
""", 1)

WEBHOOKSTATUSCHECKER_BANNER = Colorate.Diagonal(Colors.blue_to_white, r"""
    __      __   _    _            _     ___ _        _              ___ _           _           
    \ \    / ___| |__| |_  ___ ___| |__ / __| |_ __ _| |_ _  _ ___  / __| |_  ___ __| |_____ _ _ 
     \ \/\/ / -_| '_ | ' \/ _ / _ | / / \__ |  _/ _` |  _| || (_-< | (__| ' \/ -_/ _| / / -_| '_|
      \_/\_/\___|_.__|_||_\___\___|_\_\ |___/\__\__,_|\__|\_,_/__/  \___|_||_\___\__|_\_\___|_|  
                                                                                              
    ==============================================================================================

    [B] To go Back
    [*] Or Enter the Webhook Url
""", 1)

WEBHOOKSTATUSCHECKERSMALL_BANNER = Colorate.Diagonal(Colors.blue_to_white, r"""
    __      __   _    _            _     ___ _        _              ___ _           _           
    \ \    / ___| |__| |_  ___ ___| |__ / __| |_ __ _| |_ _  _ ___  / __| |_  ___ __| |_____ _ _ 
     \ \/\/ / -_| '_ | ' \/ _ / _ | / / \__ |  _/ _` |  _| || (_-< | (__| ' \/ -_/ _| / / -_| '_|
      \_/\_/\___|_.__|_||_\___\___|_\_\ |___/\__\__,_|\__|\_,_/__/  \___|_||_\___\__|_\_\___|_|  
                                                                                              
    ==============================================================================================
""", 1)

IDTOFIRSTTOKENPART_BANNER = Colorate.Diagonal(Colors.blue_to_purple, r"""
     ___ ___    _____      ___ _        _     _____    _              ___          _   
    |_ _|   \  |_   ____  | __(_)_ _ __| |_  |_   ____| |_____ _ _   | _ \__ _ _ _| |_ 
     | || |) |   | |/ _ \ | _|| | '_(_-|  _|   | |/ _ | / / -_| ' \  |  _/ _` | '_|  _|
    |___|___/    |_|\___/ |_| |_|_| /__/\__|   |_|\___|_\_\___|_||_| |_| \__,_|_|  \__|

    ====================================================================================

    [B] To go Back
    [*] Or Enter the User ID
""", 1)

IDTOFIRSTTOKENPARTSMALL_BANNER = Colorate.Diagonal(Colors.blue_to_purple, r"""
     ___ ___    _____      ___ _        _     _____    _              ___          _   
    |_ _|   \  |_   ____  | __(_)_ _ __| |_  |_   ____| |_____ _ _   | _ \__ _ _ _| |_ 
     | || |) |   | |/ _ \ | _|| | '_(_-|  _|   | |/ _ | / / -_| ' \  |  _/ _` | '_|  _|
    |___|___/    |_|\___/ |_| |_|_| /__/\__|   |_|\___|_\_\___|_||_| |_| \__,_|_|  \__|
                                                   
    ====================================================================================
""", 1)

# Menus
def webhookSpammer_menu():
    while True:
        os.system("cls")
        os.system("title Webhook Spammer -- Made by Kiwai")
        banner(WEBHOOKSPAMMER_BANNER)
        choice = input("    > ").strip()
        if choice.startswith("https://discord.com/api/webhooks/"):
            banner(WEBHOOKSPAMMERSMALL_BANNER)
            webhook_url = choice
            webhookSpammer(webhook_url)
        elif choice.lower() == "b":
            break
        else:
            banner(WEBHOOKSPAMMER_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice/Url.")
            input("\n    Press Enter to go back...")

def webhookDestroyer_menu():
    while True:
        os.system("cls")
        os.system("title Webhook Destroyer -- Made by Kiwai")
        banner(WEBHOOKDESTROYER_BANNER)
        choice = input("    > ").strip()
        if choice.startswith("https://discord.com/api/webhooks/"):
            banner(WEBHOOKDESTROYERSMALL_BANNER)
            webhook_url = choice
            webhookDestroyer(webhook_url)
        elif choice.lower() == "b":
            break
        else:
            banner(WEBHOOKDESTROYER_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice/Url.")
            input("\n    Press Enter to go back...")

def webhookStatusChecker_menu():
    while True:
        os.system("cls")
        os.system("title Webhook Status Checker -- Made by Kiwai")
        banner(WEBHOOKSTATUSCHECKER_BANNER)
        choice = input("    > ").strip()
        if choice.startswith("https://discord.com/api/webhooks/"):
            banner(WEBHOOKSTATUSCHECKERSMALL_BANNER)
            webhook_url = choice
            webhookStatus(webhook_url)
        elif choice.lower() == "b":
            break
        else:
            banner(WEBHOOKSTATUSCHECKER_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice/Url.")
            input("\n    Press Enter to go back...")

def idToFirstTokenPart_menu():
    while True:
        os.system("cls")
        os.system("title ID To First Token Part -- Made by Kiwai")
        banner(IDTOFIRSTTOKENPART_BANNER)
        choice = input("    > ").strip()
        if choice.isdigit() and len(choice) >= 16:
            banner(IDTOFIRSTTOKENPARTSMALL_BANNER)
            id = choice
            idToFirstTokenPart(id)
        elif choice.lower() == "b":
            break
        else:
            banner(IDTOFIRSTTOKENPART_BANNER)
            print(f"    {Fore.RED}[-]{Style.RESET_ALL} Invalid choice/ID.")
            input("\n    Press Enter to go back...")
