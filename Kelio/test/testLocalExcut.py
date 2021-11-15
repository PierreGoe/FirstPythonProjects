from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException #Catch Exeption
from selenium.webdriver.chrome.options import Options
import stdiomask
import datetime 
import time


UserID=""
Password=""

listHoraire = []




options = Options()
options.headless = True  #True pour pas voir la fenetre
driver = webdriver.Chrome(chrome_options= options)
listHoraire = [] 
indiceJour = 3
heuresupweek = []
heureSupSomme = datetime.datetime.strptime("01/01/2019 00:00","%d/%m/%Y %H:%M")
newHoraire=[]




while indiceJour <=11 :
    
    indiceNumerosBadge = '5'
    driver.get('file:///C:/Users/pgoem/Desktop/Python/Kelio/capture/D%C3%A9clarations%20de%20pr%C3%A9sence.htm')

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