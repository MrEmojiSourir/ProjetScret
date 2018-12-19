import keyboard
import os
import time
import win32api
import win32con
import sys

os.system("CLS")
print("Microsoft Windows [version 10.0.15063]\n \
(c) 2017 Microsoft Corporation. Tous droits réservés.")


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
time.sleep(2)
while True:
    # keyboard.write("z")
    # keyboard.press_and_release('<')
    

    clickon = True
    nb = 0
    while clickon:
        click(960,540)
        nb =+ 1 
        if nb == 50:
            clickon = False

    time.sleep(1)
