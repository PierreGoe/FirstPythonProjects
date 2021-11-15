import random
import time

import pyautogui
import pynput
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key, KeyCode, Listener
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController

pyautogui.position()

# Variable indispensable pour modul Keyborad controller
keyboard = KeyboardController()
mouse = MouseController()


# ---------- Les fonctions ---------------

# ---------- variable Global ---------------

OBJET_TROUVER=False

def functionExit():
    print('Fermeture')
    quit()


def functionClicLeft():
    mouse.press(Button.left)
    mouse.release(Button.left)

def functionDoubleClic():
    mouse.click(Button.left, 2)


def functionCtrlClicLeft():
    with keyboard.pressed(Key.ctrl):
        mouse.click(Button.left, 2)


def functionClicRight():
    mouse.press(Button.right)
    mouse.release(Button.right)


# def attack_essencedrain():
#     keyboard.press(key="r")
#     keyboard.release(key="r")
#     # timesleep = random.randrange(0.100, 0.20i0)
#     # timesleep = random.uniform(0.050, 0.100)
#     timesleep = random.uniform(0.100, 0.200)
#     time.sleep(timesleep)
#     print(timesleep)
#     keyboard.press(key="t")
#     keyboard.release(key="t")


def portal():
    # mouse.position = (1100, 550)
    # time.sleep(0.5)
    # functionClicLeft()
    # time.sleep(1)
    # keyboard.press(key="i")
    # keyboard.release(key="i")
    # time.sleep(0.1)
    # mouse.position = (1875, 670)
    # time.sleep(0.1)
    # functionClicRight()
    # keyboard.press(key="i")
    # keyboard.release(key="i")
    # mouse.position = (975, 400)
    # time.sleep(0.2)
    # functionClicLeft()
    keyboard.press(key="i")
    keyboard.release(key="i")
    time.sleep(0.1)
    searchPixel(origine_valeur_x=1250, OrigineValeurY=575, FinValeurX=1920, FinValeurY=1080, NombresObjetRechercher=1, ValeurDeRouge=138, ValeurDeVert=160, ValeurDeBleu=179)
    keyboard.press(key="i")
    keyboard.release(key="i")
    time.sleep(0.5)
    searchPixel(origine_valeur_x=680, OrigineValeurY=100, FinValeurX=1300, FinValeurY=700, NombresObjetRechercher=1, ValeurDeRouge=200, ValeurDeVert=200, ValeurDeBleu=220)
    functionClicLeft()
# def returnBase():
    
def CleanInventorFast():
    with keyboard.pressed(Key.ctrl):
        mouseX = 1870
        while mouseX > 1355:
            mouseX -= 50
            mouseY = 885
            while mouseY > 620:
                mouseY -= 55
                time.sleep(0.02)
                mouse.position = (mouseX, mouseY)
                time.sleep(0.02)
                functionClicLeft()

def CleanInventor():
    
    from PIL import ImageGrab
    import time

    image = ImageGrab.grab()
    
    origine_valeur_x=1280
    origine_valeur_y=600
    fin_valeur_x=1810
    fin_valeur_y=810
    mouse_possition_valeur_x = origine_valeur_x
    mouse_possition_valeur_y = origine_valeur_y
    nombres_objet_rechercher=20
    ValeurDeRouge=4
    ValeurDeVert=5
    ValeurDeBleu=30
    image_trouver = 0
    while mouse_possition_valeur_x < fin_valeur_x:
    
        while mouse_possition_valeur_y < fin_valeur_y:

            color_pixel = image.getpixel((mouse_possition_valeur_x, mouse_possition_valeur_y))
            if image_trouver >= nombres_objet_rechercher:
                break
            elif color_pixel == (4, 5, 30):
                time.sleep(0.05)
                image_trouver += 1
                mouse.position = (mouse_possition_valeur_x + 3, mouse_possition_valeur_y + 3)
                time.sleep(0.05)
                functionCtrlClicLeft()                
                mouse_possition_valeur_y += 1
                time.sleep(0.25)
                image = ImageGrab.grab()
            elif color_pixel == (43, 4, 4):
                time.sleep(0.05)
                image_trouver += 1
                mouse.position = (mouse_possition_valeur_x + 3, mouse_possition_valeur_y + 3)
                time.sleep(0.05)
                functionCtrlClicLeft()
                mouse_possition_valeur_y += 1
                time.sleep(0.25)
                image = ImageGrab.grab()
            else:

                mouse_possition_valeur_y += 1
        if image_trouver >= nombres_objet_rechercher:
            print("Trop D'objet detecter")
            break
        else:
            mouse_possition_valeur_x += 1
            mouse_possition_valeur_y = origine_valeur_y
    print('Inventaire vide.')
    
def selectStach(selectNumStash = 1, nombreDeStashMax=17):
    
    i = 1
    while i < nombreDeStashMax:
        keyboard.press(Key.left)
        keyboard.release(Key.left)
        i += 1 

    j=0   
    while j < selectNumStash-1:
        keyboard.press(Key.right)
        keyboard.release(Key.right)
        j += 1 
    
    print("Stash principale ouvert !")

def openCoffre():
    mouse.position = (855, 93)
    time.sleep(0.1)
    functionClicLeft()
    time.sleep(2)

def main_fonction():
    portal()
    time.sleep(3)
    openCoffre()
    time.sleep(1)
    selectStach
    time.sleep(0.5)
    cleanInventor()

def rechercheObjectStach(nom_objet_rechercher = 'Currency'):
    # Recherche Ctrl+F
    with keyboard.pressed(Key.ctrl):
        keyboard.press('f')
        keyboard.release('f')
    time.sleep(0.2)
    keyboard.type(nom_objet_rechercher)
    time.sleep(0.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.2)

def searchPixelCtrl(origine_valeur_x=16, OrigineValeurY=161, FinValeurX=650, FinValeurY=800, NombresObjetRechercher=50, ValeurDeRouge=231, ValeurDeVert=180, ValeurDeBleu=119): 
    # (231, 180, 119):
    from PIL import ImageGrab
    import time
    global OBJET_TROUVER

    
    ValeurX = origine_valeur_x
    ValeurY = OrigineValeurY
    image = ImageGrab.grab()
    image_trouver = 0
    print('La couleur rechercher : '+ str(ValeurDeRouge) +'-'+ str(ValeurDeVert) +'-'+ str(ValeurDeBleu))

    while ValeurX < FinValeurX:

        while ValeurY < FinValeurY:

            color_pixel = image.getpixel((ValeurX, ValeurY))
            if image_trouver >= NombresObjetRechercher:
                break
            elif color_pixel == (ValeurDeRouge, ValeurDeVert, ValeurDeBleu):
                image_trouver += 1
                OBJET_TROUVER=True
                mouse.position = (ValeurX + 3, ValeurY + 3)
                time.sleep(0.05)
                functionCtrlClicLeft()
                time.sleep(0.05)
                ValeurY += 1
                time.sleep(0.25)
                image = ImageGrab.grab()
            else:
                ValeurY += 1
        if image_trouver >= NombresObjetRechercher:
            print("Trop D'objet detecter")
            break
        else:
            ValeurX += 1
            ValeurY = OrigineValeurY

    print('Objet trouver :'+str(image_trouver))
    print('Recherche Terminer.\n')
    
def searchPixel(origine_valeur_x=16, OrigineValeurY=161, FinValeurX=650, FinValeurY=800, NombresObjetRechercher=50, ValeurDeRouge=231, ValeurDeVert=180, ValeurDeBleu=119): 
    # (231, 180, 119):
    from PIL import ImageGrab
    import time

    
    ValeurX = origine_valeur_x
    ValeurY = OrigineValeurY
    image = ImageGrab.grab()
    image_trouver = 0
    print('La couleur rechercher: '+ str(ValeurDeRouge) +'-'+ str(ValeurDeVert) +'-'+ str(ValeurDeBleu))

    while ValeurX < FinValeurX:

        while ValeurY < FinValeurY:

            color_pixel = image.getpixel((ValeurX, ValeurY))
            if image_trouver >= NombresObjetRechercher:
                break
            elif color_pixel == (ValeurDeRouge, ValeurDeVert, ValeurDeBleu):
                image_trouver += 1
                mouse.position = (ValeurX + 3, ValeurY + 3)
                time.sleep(0.05)
                functionClicRight()
                time.sleep(0.05)
                
                print("Nombre d'objet Trouver :" + str(image_trouver))
                ValeurY += 1
                time.sleep(0.25)
                image = ImageGrab.grab()
            else:

                ValeurY += 1
        if image_trouver >= NombresObjetRechercher:
            print("Trop D'objet detecter")
            break
        else:
            ValeurX += 1
            ValeurY = OrigineValeurY
    print('Objet trouver :'+str(image_trouver))
    print('Recherche Terminer.\n')
    
def cleanBigStash ():
    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Incubator'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 8)
        CleanInventor()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")

    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Delirium'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 8)
        CleanInventorFast()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")

    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Sample'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 8)
        CleanInventor()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")

    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'adds qual'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 2)
        CleanInventor()
        selectStach()
    else :
        print("Pas d'objet de type Catalyste dans votre coffre")
    
    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Simulacrum'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 2)
        CleanInventor()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")
        

    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Splinter'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 6)
        CleanInventor()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")

    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Oils'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 8)
        CleanInventor()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")

    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'guaran'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 5)
        CleanInventor()
        selectStach()
    else :
        print("Pas d'objet de type Essence dans votre coffre")

    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'fossil'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 8)
        CleanInventor()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")


    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Atlas'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 3)
        CleanInventorFast()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")


    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Divination'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 4)
        CleanInventorFast()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")  


    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Currency'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 2)
        CleanInventorFast()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")
        return False 

    selectStach() #Select Stash a trier 
    nom_objet_rechercher = 'Currency'
    time.sleep(1)
    rechercheObjectStach(nom_objet_rechercher)
    searchPixelCtrl(NombresObjetRechercher=50) # Recherche "l'objet" le selectionne 
    if OBJET_TROUVER == True:
        selectStach(selectNumStash = 2)
        CleanInventorFast()
        selectStach()
    else :
        print("Pas d'objet de type "+nom_objet_rechercher+" dans votre coffre")
        return False 



    functionExit()












# --------- Les Raccourcis ---------------
combination_to_function = {
    # frozenset([Key.shift, KeyCode(char='a')]): function_return_menu, # Pas de `()` aprés function_1 parce que nous voulons passer la fonction, pas la valeur de la fonction
    # frozenset([Key.shift, KeyCode(char='b')]): prator_menu,

    frozenset([Key.f4]): functionClicLeft,
    frozenset([Key.f4]): functionExit,
    frozenset([Key.f11]): portal,
    # frozenset([Key.f8]): main_fonction,
    # frozenset([Key.f8]): cleanInventor,
    frozenset([Key.shift, KeyCode(char='a')]): portal,
    frozenset([Key.shift, KeyCode(char='w')]): CleanInventor,
    frozenset([Key.f2]): cleanBigStash,

}


# Currently pressed keys
current_keys = set()

def on_press(key):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
        combination_to_function[frozenset(current_keys)]()
        # print(current_keys)

def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track offfdd
    current_keys.clear()
    # print(current_keys)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
