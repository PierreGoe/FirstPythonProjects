import pynput
from pynput.keyboard import Key, KeyCode, Listener
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
import random
import pyautogui

pyautogui.position()



# Variable indispensable pour modul Keyborad controller 
keyboard = KeyboardController()
mouse = MouseController()




# ---------- Les fonctions ---------------


def search_pixel():
    from PIL import ImageGrab
    import time


    ValeurX = 16
    ValeurY = 161
    image = ImageGrab.grab()
    ImageTrouver = 0

    while ValeurX < 650:

        while ValeurY < 800:

            color_pixel = image.getpixel((ValeurX, ValeurY))
            # mouse.position = (ValeurX, ValeurY) 
            if ImageTrouver >= 8:
                break
            elif color_pixel == (231, 180, 119):
                ImageTrouver +=1
                mouse.position = (ValeurX + 10, ValeurY + 10) 
                # function_ctrl_clic_left()
                print("clic")
                time.sleep(1)
                image = ImageGrab.grab()
                ValeurY +=1 
                print (" Coordonner X :" + str(ValeurX)+ " Coordonner Y :" + str(ValeurY) )  
                print("Nombre d'image Trouver :" + str(ImageTrouver))
            else :
                
                ValeurY +=1  
        if ImageTrouver >= 10:
            print("fin2")
            break
        else:
            ValeurX += 1 
            ValeurY = 161
    print('fin1')



search_pixel()
