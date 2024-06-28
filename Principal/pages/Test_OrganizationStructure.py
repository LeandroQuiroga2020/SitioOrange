from selenium.webdriver.common.by import By
from pages.Test_BasePage import Test_BasePage


class Test_OrganizationStructure(Test_BasePage):

    edit = (By.XPATH,('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/label/span'))

    def __init__(self, driver):
        super(Test_OrganizationStructure, self).__init__(driver)
    
    def add_structure(self):
        self.do_click(self.edit)
