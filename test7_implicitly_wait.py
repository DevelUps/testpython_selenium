# Importamos el módulo 'webdriver' y 'time' de Selenium y Python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC


# Instanciamos un objeto de tipo 'webdriver' de Chrome especificando la ruta al archivo ejecutable del controlador de Chrome
driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")
# Navegamos a la página web especificada en el URL usando el método 'get' en el objeto 'driver'
driver.get("https://captchacoolnow.top/robot4/?c=e2738330-7423-4b60-8da6-16d48a488082&a=l57952#")
#maximiza la ventana
driver.maximize_window()
driver.implicitly_wait(10)
t=4

wait = WebDriverWait(driver, 10)
btn = wait.until(EC.element_to_be_clickable((By.ID, '//*[@id="text1"]')))
time.sleep(5)
btn.click()

time.sleep(5)

time.sleep(3)
# Cerramos la ventana del navegador usando el método 'close' en el objeto 'driver'
driver.close()

# NOTA: esta seccion esta desactualizada