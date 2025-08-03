import os, winreg, ctypes, sys, random, string
from sys import stdout

# Check if the script is run as Admin, if not, UAC request
def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable,
        " ".join([f'"{arg}"' for arg in sys.argv]),
        None, 1
    )
    sys.exit(0)

# Resize and center the window
def resize_and_center_console(width=100, height=30):
    os.system(f"mode con: cols={width} lines={height}")

    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        screen_width = ctypes.windll.user32.GetSystemMetrics(0)
        screen_height = ctypes.windll.user32.GetSystemMetrics(1)

        font_width = 8
        font_height = 16

        window_width = width * font_width
        window_height = height * font_height

        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)

        ctypes.windll.user32.MoveWindow(hwnd, x, y, window_width, window_height, True)

#Webhook Username Generator
def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Banner
def banner(txt: str):
    os.system("cls")
    print(txt + "\n")

# Regedit Utility
def read_registry_value(root, path, name):
    try:
        with winreg.OpenKey(root, path, 0, winreg.KEY_READ) as key:
            value, _ = winreg.QueryValueEx(key, name)
            return value
    except FileNotFoundError:
        return None
    
def write_registry_value(root, path, name, value):
    with winreg.CreateKeyEx(root, path, 0, winreg.KEY_WRITE) as key:
        winreg.SetValueEx(key, name, 0, winreg.REG_SZ, value)

# Base64 EasterEggs
easterEgg_Xpt00 = "U2FsdXQgbW9uIGJnIMOnYSBmYWl0IHVuIG1vbWVudCBxdSdvbiBzZSBjb25uYcOudCBldCBxdSdvbiBlc3QgbWVpbGxldXIgcG90ZSBldCBqJ8Opc3DDqHJlIHF1ZSBjJ2VzdCBwYXMgcHLDqnQgZGUgYm91Z2VyLCB0J2VzIGwndW4gZGVzIHNldWwgw6AgcXVpIGonYWkgcGFybGVyIGRlIG1lcyBwcm9ibMOobWVzIGV0IHRhIGZhaXQgZGUgbcOqbWUgw6dhIGZhaXQgcXUnb24gYSB1bmUgY29uZmlhbmNlIGwndW4gcG91ciBsJ2F1dHJlIHF1aSBzJ8OpcHVpc2VyYSBqYW1haXMgPDMu"
easterEgg_Doralexplosion = "U2FsdXQgbW9uIGJnLCDDp2EgZmFpdCBtw6ptZSBwYXMgdW4gYW4gcXUnb24gZXN0IHBvdGUgZXQgdCdlcyBsZSBtZWlsbGV1ciBhbWkgcXVlIGonYWkgamFtYWlzIGV1LCBqJ8Opc3DDqHJlIHF1J2VudHJlIG5vdXMgw6dhIHZhIHBhcyBib3VnZXIgZXQgcXVlIHBvdXIgIHRvaSBhdXNzaSBqZSBzdWlzIHRvbiBtZWlsbGV1ciBwb3RlLCBzYWNoZSBxdWUgaidhaSBwYXMgZW52aWUgcXUnb24gcmVkZXZpZW5uZSBkZXMgaW5jb25udXMgcGFyY2UgcXVlIGMnZXN0IGF2ZWMgdG9pIHF1ZSBqJ2FpIGxlcyBwbHVzIGdyb3MgZm91IHJpcmVzIDwzLg=="