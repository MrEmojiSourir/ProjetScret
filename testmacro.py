import keyboard
import os
import time
import win32api
import win32con
import sys
from color import *
from tkinter import*

os.system("CLS")    
sys.stdout.write(RESET)

version = "Imagination du projet"
logiciel_name = "Automatizer"
terminale_power = True

nb = 0

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

main = Tk()
main.geometry("800x800")
main.maxsize(800, 800)
main.minsize(800, 800)

# def jsp():
#     os.system("CLS")    
#     sys.stdout.write(BWhite)
#     print(f"Merci d'utiliser {logiciel_name} V{version}")
#     print(f" Créer par : Fondateur : {fondateur},\n Developeur : {developeur},\n Administrateur : {administrateur}")

#     sys.stdout.write(RESET)
#     print("\nFonctionement : \n Marqué 'keyboard' ou 'mousse' puis suiver les instruction une fois fini marqué 'STOP' \n Le [0] c'est le nombre de foncgtion que vous avez mit en place \n")


# while terminale_power:
#     jsp()
#     fonction = input(f"[{nb}]'mousse'/'keyboard'>")

#     if fonction == "mousse":
#         print("Mousse")
#         time.sleep(0.5)
#         jsp()
    
#     elif fonction == "keyboard":
#         print("Keyboard / Clavier")

#         print("Choisir ce que vous voulez (Mettre le numéro selon la fonction):\
#         [0] : écrire un text\
#         ")

#         keynb = input(">>>")

#         if keynb == 0:
#             write = input("Quelle text est à ecrire : ")

#             fichier = open("macro.py", "a")
#             fichier.write(f"keyboard.write('{write}')")
#             fichier.close()

#         nb =+ 1
#         time.sleep(0.5)
#         jsp()
    
#     elif fonction == "STOP":
#         terminale_power = False

#         print("Execution du programme")

#         import macro

#     else:
#         print("Marque bien 'keyboard' ou 'mousse' ou 'STOP' si tu as fini")

main.mainloop()
