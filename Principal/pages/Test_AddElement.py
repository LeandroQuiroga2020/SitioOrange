from pages.Test_BasePage import Test_BasePage
from selenium.webdriver.common.by import By

class Test_AddElement(Test_BasePage):
    
    botonadd = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[2]/button')
    unitId = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[1]/div/div[2]/input')
    name = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[2]/div/div[2]/input')
    description = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[3]/div/div[2]/textarea')
    botonsave = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/form/div[4]/button[2]')
    elemento_creado =  (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/ul/li/ul/li[11]/div[1]/div/div/div') 

    

    

    def __init__(self, driver):
        super(Test_AddElement, self).__init__(driver)

    def agregar_elemento(self,unitId,name,description):
        self.do_click(self.botonadd)
        self.do_send_keys(self.unitId,unitId)
        self.do_send_keys(self.name,name)
        self.do_send_keys(self.description,description)
        self.do_click(self.botonsave)

    def verificacionElemento(self):
        #self.get_text(self.elemento_creado)
        return self.get_text(self.elemento_creado)