import keyboard
import os
import time
import win32api
import win32con
import sys
from color import *

os.system("CLS")

version = "Imagination du projet"
logiciel_name = "Beurre"

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


# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
# time.sleep(2)

# while True:
#     # keyboard.write("z")
#     # keyboard.press_and_release('<')
    

#     clickon = True
#     nb = 0
#     while clickon:
#         click(960,540)
#         nb =+ 1 
#         if nb == 50:
#             clickon = False

#     time.sleep(1)

print(f"Merci d'utiliser {logiciel_name} V{version}")
print(f" Créer par : Fondateur : {fondateur},\n Developeur : {developeur},\n Administrateur : {administrateur}")

sys.stdout.write(RED)
print("test !")
