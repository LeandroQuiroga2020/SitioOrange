

from selenium.webdriver.common.by import By
from pages.Test_BasePage import Test_BasePage


from asyncio import sleep
class Test_HomePage(Test_BasePage):  #le pasamos por parametro la clase padre para que pueda heredar

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
    button_help =(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/div/button') 
    
    def __init__(self, driver):
        super(Test_HomePage, self).__init__(driver)

    def load_page(self, url):
        self.driver.get(url)

    def login(self, username_text, password_text):
        self.do_send_keys(self.username, username_text)
        self.do_send_keys(self.password, password_text)
        self.do_click(self.button)

    def help(self):
        self.do_click(self.button_help)
        

