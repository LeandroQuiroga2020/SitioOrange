from selenium.webdriver.common.by import By
from pages.Test_BasePage import Test_BasePage

class Test_OrangePage(Test_BasePage):

    admin = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a')
    organization = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
    structure = (By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]')

    def __init__(self, driver):
        super(Test_OrangePage, self).__init__(driver)

    def click_admin(self):
        self.do_click(self.admin)
        self.do_click(self.organization)
        self.do_click(self.structure)
