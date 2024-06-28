from selenium.webdriver.common.by import By
from pages.Test_BasePage import Test_BasePage
from selenium.webdriver.common.keys import Keys

class Test_HelpPage(Test_BasePage):  #le pasamos por parametro la clase padre para que pueda heredar

    search = (By.XPATH, '//*[@id="query"]')
    texto_searchbuscado= (By.XPATH, '//*[@id="main-content"]/h1')
    boton_signo = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/div/button')
    
    
    
    def __init__(self, driver):
        super(Test_HelpPage, self).__init__(driver)

    def boton_click(self):
        self.do_click(self.boton_signo)    

    def search_help(self , search_text):
        
        self.do_send_keys(self.search , search_text)      
        self.driver.find_element(*self.search).send_keys(Keys.ENTER) #mando un enter al webelement, ya que no tiene boton de enter

    def verificacion_search(self):
        return self.get_text(self.texto_searchbuscado)
