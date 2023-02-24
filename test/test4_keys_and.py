# Importamos el módulo 'webdriver' y 'time' de Selenium y Python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 


# Instanciamos un objeto de tipo 'webdriver' de Chrome especificando la ruta al archivo ejecutable del controlador de Chrome
driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")

# Maximiza la ventana
driver.maximize_window()

# Navegamos a la página web especificada en el URL usando el método 'get' en el objeto 'driver'
driver.get("https://demoqa.com/text-box")
time.sleep(2)

nom = driver.find_element(By.XPATH,"//input[@id='userName' and @type='text' ]")
time.sleep(2)

nom.send_keys("nombre" + Keys.TAB + "correo@correo.com" + Keys.TAB + "direccion uno" + Keys.TAB + "direccion dos" + Keys.ENTER)
time.sleep(2)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element(By.XPATH,"//button[contains(@id,'submit')]").click()
time.sleep(2)

driver.close()
