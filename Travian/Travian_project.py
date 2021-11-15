#coding:utf-8

""" Installation selenium 'pip install selenium'
    installer drive Chrome 'https://sites.google.com/a/chromium.org/chromedriver/downloads'
    https://www.youtube.com/watch?v=dZLyfbSQPXI
    https://selenium-python.readthedocs.io/

    Outil Reg EDit
    https://python.doctor/page-expressions-regulieres-regular-python
    https://regex101.com/

"""

import time
import subprocess
import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException #Catch Exeption



options = Options()
options.headless = True  #True pour pas voir la fenetre

driver = webdriver.Chrome(chrome_options= options) #Appel Driver Chrome



#------------------------------------------------------------------MAIN---------------------------------------------------------------------


Compteur = 1
CompteurCible = 1
CompteurCible = input("\n \n \n Combien d'envoi à effectuer ? ")
CompteurCible= int(CompteurCible)
Compteur = int(Compteur)


def login(driver):
    driver.get("https://ts1.travian.fr/login.php") # Site a ouvrir
    # driver.set_window_size(1120, 550)
    pseudoLogin = driver.find_element_by_name("name") #fonction find qui utilise 'name'
    pseudoLogin.send_keys("")
    mdpLogin = driver.find_element_by_name('password')
    mdpLogin.send_keys("")
    buttonConnection = driver.find_element_by_id('s1')  #fonction find qui utilise iD
    buttonConnection.click()

def SelectV1(driver):
    village = driver.find_element_by_xpath('//*[@id="sidebarBoxVillagelist"]/div[2]/div[2]/ul/li[1]/a/div') #fonction find qui utilise xpath
    village.click()

def OpenMarket(driver):
    driver.get("https://ts1.travian.fr/build.php?t=5&id=32")
    


def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def openPlaceDeRassemblement(driver):
    compteurTableau= 1 
    compteurTableau = str(compteurTableau)    
    driver.get("https://ts1.travian.fr/build.php?tt=1&id=39")
    driver.get('https://ts1.travian.fr/build.php?gid=16&tt=1&filter=4') # Avec filtre
    # driver.get('https://ts1.travian.fr/build.php?tt=1&id=39') #Sans filtre
    url = driver.find_element_by_xpath('//*[@id="build"]/div[4]/table['+ compteurTableau +']')
   
    while url != None:

        print('Tableau : ' + compteurTableau + 'selectionné ! ')
    
        
        try:
            consoCereale = driver.find_element_by_xpath('//*[@id="build"]/div[4]/table['+ compteurTableau +']/tbody[3]/tr/td/div[1]/div/div/span').text
            print('Assistance detecter')
            consoCereale = int(consoCereale)
        except NoSuchElementException:
            print("Plus d'assistance !")
            break
        
            

        if consoCereale >= 10 :
            pass
        else:
            compteurTableau = int(compteurTableau) +1
            compteurTableau = str(compteurTableau)  
            print('Consomation de Céréale pas assez suffisante, tableau suivant :')
            continue
        
        TableauAssistance = driver.find_element_by_xpath('//*[@id="build"]/div[4]/table[' + compteurTableau + ']/thead/tr/td[2]/a')
        TableauAssistance.click()
        
        envoiTroupe = driver.find_element_by_xpath('//*[@id="tileDetails"]/div[1]/div[1]/div[1]/a') # Ouverture MAP 
        envoiTroupe.click()
    
        coordX = driver.find_element_by_id('xCoordInputMap').get_attribute('value') # Coordonner X MAP
        coordY = driver.find_element_by_id('yCoordInputMap').get_attribute('value') # Coordonner Y MAP
        consoCereale = str(consoCereale)
        print(f'Vos troupe en {coordX}/{coordY} consomme {consoCereale} céréales')
        
        print(f"Envoi de Ressource au village {coordX}/{coordY} !")
        driver.get("https://ts1.travian.fr/build.php?t=5&id=32")

        cereale = driver.find_element_by_xpath('//*[@id="r4"]')
        cereale.send_keys(consoCereale)

        coordonnerX = driver.find_element_by_xpath('//*[@id="xCoordInput"]')
        coordonnerX.send_keys(coordX)

        coordonnerY = driver.find_element_by_xpath('//*[@id="yCoordInput"]')
        coordonnerY.send_keys(coordY)

        caseValide = driver.find_element_by_xpath('//*[@id="enabledButton"]')
        caseValide.click()

        time.sleep(1)

        caseValide = driver.find_element_by_xpath('//*[@id="enabledButton"]')
        caseValide.click()
        
        print('Lancement : ok ... \n\n\n')


        driver.get('https://ts1.travian.fr/build.php?gid=16&tt=1&filter=4')
        compteurTableau = int(compteurTableau)
        compteurTableau += 1
        compteurTableau = str(compteurTableau)


        
            
        # driver.find_element_by_xpath('//*[@id="build"]/div[4]/table['+ compteurTableau +']')

        # coordX = re.split(r'[^\w\s-]', coordX) # Caracter - ET présence de caratére a-z
        # for coord in coordX:
        #     print(coord)

        # coordY = re.findall(r'(\w+|[-])', coordY) #Caracter - OU présence de caratére a-z

        




while Compteur <= CompteurCible :

    login(driver)

    print("\n  Connection effectuer!  \n")

    SelectV1(driver)

    print("village Selectionner ! \n ")

    openPlaceDeRassemblement(driver)

    Compteur += 1 
    print('Compteur +1')


    time.sleep(3600)


print("--------------Fin Du Progamme---------------")
driver.quit()
print("--------------Fermeture Travian---------------")
time.sleep(1)
quit()






# from pyautogui import press, typewrite, hotkey
# hotkey('ctrl', 'c')
# press('a')
# typewrite('quick brown fox')
# hotkey('ctrl', 'w')