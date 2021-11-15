from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #Catch Exeption
from selenium.webdriver.chrome.options import Options
import stdiomask
import datetime 
import time


UserID=""
Password=""
indiceJour = None
listHoraire = []
heuresupweek = None




def _switchHoraireDansJour(driver, listHoraire, indiceJour, heuresupweek):
    
    indiceNumerosBadge = '5'
    


    while True:
        indiceJour = str(indiceJour)
        try :
            newHoraire = driver.find_element_by_xpath('//*[@id="formAction"]/table/tbody/tr/td[3]/table/tbody/tr/td/table[3]/tbody/tr['+indiceJour+']/td['+ indiceNumerosBadge +']/table/tbody/tr/td[1]/a/span/div').text
            indiceNumerosBadge = int(indiceNumerosBadge)
            indiceNumerosBadge += 1 
            indiceNumerosBadge = str(indiceNumerosBadge)
            print(f'Nouvelle entrée : {newHoraire}')
            newHoraire = str(newHoraire)
            listHoraire.append(newHoraire)
            
        except NoSuchElementException:
            
            # print('Récapitulatif de tout les horaires :')
            # print(listHoraire)
            indiceNumerosBadge = '5'
            listHoraire = ['01/01/2019 '+ heure for heure in listHoraire]
            listHoraire = [datetime.datetime.strptime(heure, '%d/%m/%Y %H:%M') for heure in listHoraire]
            try:
                test =listHoraire[3]-listHoraire[2]+listHoraire[1]-listHoraire[0]
            except :
                print("Pas assez de badgeage pour le jour. \n")

                break
            heures_sup= test- datetime.timedelta(hours=7, minutes=15)
            heuresupweek.append(heures_sup) 
            print(heures_sup)
            
            
            return heuresupweek

def Authen(driver,UserID,Password):
    #driver.get('file:///C:/Users/pgoem/Desktop/Python/Kelio/capture/Kelio.html')  # A SUPPPP
    # UserID = input("Identifiant :")
    # Password = stdiomask.getpass(prompt="Mot de passe :" )
    driver.get('http://kelio.itga.fr/open/login?authenticationFailure=1')  # FOR REAL
    pseudoLogin = driver.find_element_by_xpath('//*[@id="username"]') #fonction find qui utilise 'name'
    pseudoLogin.send_keys(UserID)
    time.sleep(1)
    mdpLogin = driver.find_element_by_xpath('//*[@id="password"]')
    mdpLogin.send_keys(Password)
    time.sleep(1)
    buttonConnection = driver.find_element_by_xpath('//*[@id="btnAction"]')  # clic button
    buttonConnection.click()
    time.sleep(3)
    if driver.current_url == 'http://kelio.itga.fr/open/homepage':
        Kelionavigation(driver)
    else:
        print("Identifiant incorrect")
        Authen(driver,UserID,Password)


def Kelionavigation(driver):
    
    #driver.get('file:///F:/capture/Badgeuse%20virtuelle.html') # A SUPPPP
    driver.get('http://kelio.itga.fr/open/global') # FOR REAL
    buttonDeclaration = driver.find_element_by_xpath('//*[@id="formAction"]/div[1]/div[4]/center/table/tbody/tr/td[8]/a')  #Open Kelio semaine 
    buttonDeclaration.click()
    #driver.get('file:///F:/capture/Déclarations%20de%20présence.html') # A SUPPPP
    # input("Appuyer sur une Touche si vous etes sur la page de Kelio")


def fonction_main():
    options = Options()
    options.headless = True  #True pour pas voir la fenetre
    driver = webdriver.Chrome(chrome_options= options)
    listHoraire = [] 
    indiceJour = 3
    heuresupweek = []
    heureSupSomme = datetime.datetime.strptime("01/01/2019 00:00","%d/%m/%Y %H:%M")



    Authen(driver,UserID,Password)


    while indiceJour <=11 :
        
        switchHoraireDansJour(driver, listHoraire, indiceJour, heuresupweek)
        
        indiceJour = int(indiceJour)
        indiceJour +=2
        listHoraire=[]
        


    for hs in heuresupweek:
        heureSupSomme += hs
        print(hs) 
    total = str(datetime.datetime.time(heureSupSomme))
    print("Temps total d'heure suplémentaire cette semaines : "+ total)


    driver.quit()

    print("Fin du Programme ")
    input() # Garde console Open 



        







