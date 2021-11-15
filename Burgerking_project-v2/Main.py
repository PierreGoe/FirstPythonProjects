
class SeleniumBrowser: 
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys

    OPTIONS_SELENIUM = Options()
    OPTIONS_SELENIUM.headless = False  #True pour pas voir la fenetre
    DRIVER = webdriver.Chrome(chrome_options= OPTIONS_SELENIUM)
    valueCodePromo =''
    
    def open_url_on_webdriver(self, url): # Les fonction sont sans majuscule # Fonction d'ouverture du driver qui prend comme argument un srting'URL'
        self.url = url # Création Variable Url
        self.DRIVER.delete_all_cookies() # delete cookies pour eviter des problemes 
        self.DRIVER.get(url)# ouverture Driver avec l'url
        return print('Chargement:')
    
    def form_completion(self):# Fonction de ciblage et clic d'un element HTML en fonction de sont ID
        while True:# Boucle tant que l'élément est présent sur la page
            try :
                self.DRIVER.find_element_by_id('NextButton').click()
            except Exception as e:
                print('Chargement Terminer')
                return False
                
    
    def get_code_promo(self):    
        self.valueCodePromo = self.DRIVER.find_element_by_class_name('ValCode').text # Fonction de ciblage d'un element HTML en fonction de sont sont classe name. 
        return self.valueCodePromo
    


def main():
    browser = SeleniumBrowser() 
    browser.open_url_on_webdriver("https://www.bk-feedback-de.com/Index.aspx?LanguageID=fr-CH")
    browser.form_completion()
    print(browser.get_code_promo())



main()