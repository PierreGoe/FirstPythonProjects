import pynput
from pynput.keyboard import Key, KeyCode, Listener
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time


# Variable indispensable pour modul Keyborad controller 
keyboard = KeyboardController()
mouse = MouseController()




# ---------- Les fonctions ---------------


def function_quit():
    print('Fermeture')
    quit()

def function_clic():
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)

# --------- Les Raccourcis ---------------

combination_to_function = {
    # frozenset([Key.shift, KeyCode(char='a')]): function_return_menu, # Pas de `()` aprés function_1 parce que nous voulons passer la fonction, pas la valeur de la fonction
    # frozenset([Key.shift, KeyCode(char='b')]): prator_menu,
    
    frozenset([Key.f4]): function_clic,
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

