#conding:utf-8

# Importation des modules
import keyboard
import os
import time
import win32api
import win32con
import sys
from color import *
from tkinter import*
from tkinter.messagebox import *

os.system("CLS")    

# Variable - Logiciel
version = "0.0"
logiciel_name = "Automatizer"

# Variable - STAFF
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

#  Configuration du logiciel
main = Tk()
main.geometry("800x800")
main.maxsize(800, 800)
main.minsize(800, 800)
main.title("Automatizer | En Dev")

# Bar de menus
def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(main)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Editer", command=alert)
menu1.add_separator()
menu1.add_command(label="Quitter", command=main.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Couper", command=alert)
menu2.add_command(label="Copier", command=alert)
menu2.add_command(label="Coller", command=alert)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=alert)
menu3.add_command(label="Le staff", command=alert)
menubar.add_cascade(label="Aide", menu=menu3)

main.config(menu=menubar)

# Liste des événements
l = LabelFrame(main, text="Les événement :", padx=20, pady=250, cursor="cross")
l.pack(side=BOTTOM, fill="both", expand="no")
 
Label(l, text="[0] : Keyboard", compound=TOP).pack()
Label(l, text="[1] : Mousse").pack()

# Bouton !!!!!
def clavier():
    ClavierFEN = Tk()

    value = StringVar() 
    write = Radiobutton(ClavierFEN, text="écrire un text", variable=value, value=1)
    presse = Radiobutton(ClavierFEN, text="Cliquez sur un bouton puis relachez", variable=value, value=2)
    write.pack()
    presse.pack()

    entree = Entry(ClavierFEN, width=30)
    entree.pack()

clavier  = Button(main, text="Clavier", command=clavier)
clavier.pack(side=TOP)

main.mainloop()
