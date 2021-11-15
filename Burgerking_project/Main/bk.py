from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import smtplib
import config

options = Options()
options.headless = True  #True pour pas voir la fenetre
driver = webdriver.Chrome(chrome_options= options)
# driver = webdriver.Chrome()
valueCodePromo =''
compteurNombreDePage = 0



def Open_webdriver(driver, options):
    driver.get('https://www.bk-feedback-de.com/Index.aspx?LanguageID=fr-CH')
    print('Chargement:')


def Click_bouton(driver, options):

    boutonSuivant = driver.find_element_by_id('NextButton')
    boutonSuivant.click()



def code_promo(driver, options):
    global valueCodePromo 
    valueCodePromo = driver.find_element_by_class_name('ValCode').text
    print(valueCodePromo)
      


def boucle(driver, options, compteurNombreDePage):
    try :
        driver.find_element_by_id('NextButton')
        compteurNombreDePage += 4
        print(f"Progression : {compteurNombreDePage}%")
        Click_bouton(driver, options)
        boucle(driver, options, compteurNombreDePage)
    except Exception as e:
        print('Chargement Terminer')


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADRESS, config.PASSWORD)
        message = 'Subject : {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADRESS, config.DESTINATAIRE, message)
        server.quit
        print('Email envoyer')
    except:
        print('Fail')

Open_webdriver(driver, options)
boucle(driver, options, compteurNombreDePage)
code_promo(driver, options)
msg = valueCodePromo
subject = 'Code Promotion Burger King !'
send_email(subject, msg)

