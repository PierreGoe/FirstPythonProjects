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


def function_quit():
    print('Fermeture')
    quit()

def function_clic():
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.1)
   

def stellaris():
    time.sleep(3)
    keyboard.type("research_technology tech_deep_sinkhole")
    time.sleep(3)
    keyboard.type("research_technology tech_massive_glacier")
    time.sleep(3)
    keyboard.type("research_technology tech_noxious_swamp")
    time.sleep(3)
    keyboard.type("research_technology tech_selected_lineages")
    time.sleep(3)
    keyboard.type("research_technology tech_quicksand_basin")
    time.sleep(3)
    keyboard.type("research_technology tech_toxic_kelp")
    time.sleep(3)
    keyboard.type("research_technology tech_mountain_range")
    time.sleep(3)
    keyboard.type("research_technology tech_dangerous_wildlife")
    time.sleep(3)
    keyboard.type("research_technology tech_volcano")
    time.sleep(3)
    keyboard.type("research_technology tech_dense_jungle")
    time.sleep(3)
    keyboard.type("play 1")
    time.sleep(3)
    keyboard.type("research_technology tech_deep_sinkhole")
    time.sleep(3)
    keyboard.type("research_technology tech_massive_glacier")
    time.sleep(3)
    keyboard.type("research_technology tech_noxious_swamp")
    time.sleep(3)
    keyboard.type("research_technology tech_selected_lineages")
    time.sleep(3)
    keyboard.type("research_technology tech_quicksand_basin")
    time.sleep(3)
    keyboard.type("research_technology tech_toxic_kelp")
    time.sleep(3)
    keyboard.type("research_technology tech_mountain_range")
    time.sleep(3)
    keyboard.type("research_technology tech_dangerous_wildlife")
    time.sleep(3)
    keyboard.type("research_technology tech_volcano")
    time.sleep(3)
    keyboard.type("research_technology tech_dense_jungle")
    time.sleep(3)
      
    
# add jungle dense tech_tb_dense_jungle




# --------- Les Raccourcis ---------------

combination_to_function = {
    # frozenset([Key.shift, KeyCode(char='a')]): function_return_menu, # Pas de `()` aprés function_1 parce que nous voulons passer la fonction, pas la valeur de la fonction
    # frozenset([Key.shift, KeyCode(char='b')]): prator_menu,
    
    frozenset([Key.f4]): function_clic,
    frozenset([Key.f12]): function_quit,
    # frozenset([Key.f10]):
    # frozenset([Key.f11]): 
    frozenset([Key.f8]): stellaris,



    
    
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
    print(current_keys)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

