import pynput
from pynput.keyboard import Key, KeyCode, Listener
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time


# ---------- Les Variable ----------------

# Variable Menu démarer
escapte_from_tarkov =   ['950','650']
personnage =            ['950','730']
commerce =              ['950','800']
planque =               ['950','870']
sortie =                ['950','950']

# Variable Menu commerce
vendeur_menu =          ['750','35']
prator =                ['700','420']
toubib =                ['875','420']
fence =                 ['1045','420']
skier =                 ['1220','420']
peacekeeper =           ['700','650']
mécano =                ['875','650']
ragman =                ['1045','650']
jaeger =                ['1220','650']
onglet_vendre =         ['240','45']
# Variable return bouton
back =                  ['1800','25']

# Variable indispensable pour modul Keyborad controller 
keyboard = KeyboardController()
mouse = MouseController()

   



   
# ---------- Les fonctions ---------------

def prator_menu():
    print('Prator menu')
    # Retour Menu principale
    mouse.position = (back[0], back[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    mouse.position = (back[0], back[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Menu commerce
    mouse.position = (commerce[0], commerce[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    mouse.position = (vendeur_menu[0], vendeur_menu[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Choix du Marchant
    mouse.position = (prator[0], prator[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Vendre
    mouse.position = (onglet_vendre[0], onglet_vendre[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    
def toubib_menu():
    print('Toubib menu')
    # Retour Menu principale
    mouse.position = (back[0], back[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    mouse.position = (back[0], back[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Menu commerce
    mouse.position = (commerce[0], commerce[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    mouse.position = (vendeur_menu[0], vendeur_menu[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Choix du Marchant
    mouse.position = (toubib[0], toubib[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Vendre
    mouse.position = (onglet_vendre[0], onglet_vendre[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)

def skier_menu():
    print('skier menu')
    # Retour Menu principale
    mouse.position = (back[0], back[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    mouse.position = (back[0], back[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Menu commerce
    mouse.position = (commerce[0], commerce[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    mouse.position = (vendeur_menu[0], vendeur_menu[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Choix du Marchant
    mouse.position = (skier[0], skier[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Vendre
    mouse.position = (onglet_vendre[0], onglet_vendre[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)

def mekano_menu():
    print('mécano menu')
    # Retour Menu principale
    mouse.position = (back[0], back[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    mouse.position = (back[0], back[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Menu commerce
    mouse.position = (commerce[0], commerce[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    mouse.position = (vendeur_menu[0], vendeur_menu[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Choix du Marchant
    mouse.position = (mécano[0], mécano[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    # Vendre
    mouse.position = (onglet_vendre[0], onglet_vendre[1])
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)

def function_return_menu():
    time.sleep(0.2)
    mouse.position = (1800, 25)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.2)
    mouse.position = (1800, 25)
    mouse.press(Button.left)
    mouse.release(Button.left)

def function_quit():
    print('Fermeture')
    quit()





# --------- Les Raccourcis ---------------

combination_to_function = {
    # frozenset([Key.shift, KeyCode(char='a')]): function_return_menu, # Pas de `()` aprés function_1 parce que nous voulons passer la fonction, pas la valeur de la fonction
    # frozenset([Key.shift, KeyCode(char='b')]): prator_menu,
    frozenset([Key.f1]): prator_menu,
    frozenset([Key.f2]): toubib_menu,
    frozenset([Key.f3]): skier_menu,
    frozenset([Key.f4]): mekano_menu,
    frozenset([Key.f12]): function_quit,
}

# Currently pressed keys
current_keys = set()

def on_press(key):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
        combination_to_function[frozenset(current_keys)]()
        print(current_keys)

def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track offfdd
    current_keys.clear()


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()




