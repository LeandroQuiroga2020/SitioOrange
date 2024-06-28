
from time import sleep
from pages.Test_HomePage import Test_HomePage
from pages.Test_OrangePage import Test_OrangePage
from pages.Test_OrganizationStructure import Test_OrganizationStructure
from pages.Test_AddElement import Test_AddElement

def test_login(init_driver):
    #se subio esto nuevo a git
    homepage = Test_HomePage(init_driver)  #creo el objeto homepage, para llamar a los metodos de la clase HomePage
    homepage.load_page("https://opensource-demo.orangehrmlive.com/")
    homepage.login("Admin", "admin123")
    
    orangepage = Test_OrangePage(init_driver)
    orangepage.click_admin()
    
    organizationstructure = Test_OrganizationStructure(init_driver)
    organizationstructure.add_structure()
    
    addelement = Test_AddElement(init_driver)
    addelement.agregar_elemento("milo8884","milo8884","rocoroco")
  
    



    texto_obtenido = addelement.verificacionElemento()

    print(f"Texto obtenidoooo: '{texto_obtenido}'")
    sleep(2)
    # Realizar la aserción
    assert texto_obtenido == "milo : milo", f"Texto esperado joaqui joaqui, pero se obtuvo '{texto_obtenido}'"
    
    sleep(10)