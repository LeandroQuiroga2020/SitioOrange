from selenium.webdriver.support import expected_conditions as ec  
from selenium.webdriver.support.wait import WebDriverWait  
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

class Test_BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def do_click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, text):
        self.wait.until(ec.visibility_of_element_located(locator)).send_keys(text)

    def do_clear(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator)).clear()

    def get_text(self, locator):
       return self.wait.until(ec.visibility_of_element_located(locator)).text
    
#ESta parte lo hice para correr los script en varios navegadores, bajar siempre chromedriver(chrome),msedgedriver(edge), y los que correspondan a cada navegador     
    
@pytest.fixture(params=["chrome", "edge"])
def init_driver(request):
    driver = None  # Inicializamos driver como None
    
    if request.param == "chrome":
        chrome_driver_path = r"C:\Users\LeandroQA\Desktop\GitHub\SitioOrange\chromedriver.exe"
        chrome_service = ChromeService(chrome_driver_path)
        driver = webdriver.Chrome(service=chrome_service)
    elif request.param == "edge":
        edge_driver_path = r"C:\Users\LeandroQA\Desktop\GitHub\SitioOrange\msedgedriver.exe"
        edge_service = EdgeService(edge_driver_path)
        driver = webdriver.Edge(service=edge_service)
    
    yield driver  # Retornamos driver después de la inicialización
    
    if driver is not None:
        driver.quit()