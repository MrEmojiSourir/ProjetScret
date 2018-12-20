import keyboard
import os
import time
import win32api
import win32con
import sys
from color import *

os.system("CLS")    
sys.stdout.write(RESET)

version = "Imagination du projet"
logiciel_name = "Automatizer"
terminale_power = True

fondateur = [
    "MrEmojiSourir",
    "link1183"
]

developeur = [
    "Bisskote",
    "MrEmojiSourir",
    "link1183"
]
administrateur = [
    "MrEmojiSourir",
    "link1183",
    "{ Cecemel_PvP }"
]

def jsp():
    os.system("CLS")    
    sys.stdout.write(BWhite)
    print(f"Merci d'utiliser {logiciel_name} V{version}")
    print(f" Créer par : Fondateur : {fondateur},\n Developeur : {developeur},\n Administrateur : {administrateur}")

    sys.stdout.write(RESET)
    print("\nFonctionement : \n Marqué 'keyboard' ou 'mousse' puis suiver les instruction une fois fini marqué 'STOP'")


while terminale_power:
    jsp()
    fonction = input("'mousse'/'keyboard'>")

    if fonction == "mousse":
        print("Mousse")
        time.sleep(0.5)
        jsp()
    
    elif fonction == "keyboard":
        print("Keyboard")
        time.sleep(0.5)
        jsp()
    
    elif fonction == "STOP":
        terminale_power = False

    else:
        print("Marque bien 'keyboard' ou 'mousse' ou 'STOP' si tu as fini")
