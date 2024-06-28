
from time import sleep
from pages.Test_HomePage import Test_HomePage
from pages.Test_HelpPage import Test_HelpPage

def test_login(init_driver):
    #se subio esto nuevo a git
    homepage = Test_HomePage(init_driver)  #creo el objeto homepage, para llamar a los metodos de la clase HomePage
    init_driver.maximize_window()
    homepage.load_page("https://opensource-demo.orangehrmlive.com/")
    homepage.login("Admin", "admin123")
    homepage.help()
    
    original_window = init_driver.current_window_handle  # ventana principal  

    pestanas = init_driver.window_handles # Obtener la lista de pestañas abiertas
    
    init_driver.switch_to.window(pestanas[-1])# Cambiar a la nueva pestaña (la última en la lista por eso el -1)

    helppage = Test_HelpPage(init_driver)
    helppage.search_help("test")

    texto_obtenido = helppage.verificacion_search()

    assert texto_obtenido == 'One result for "test"', f"Texto esperado One result for 'test', pero se obtuvo '{texto_obtenido}'"

    sleep(3)

    init_driver.switch_to.window(original_window) #vuelve a la pagina original(default)
    
    sleep(3)