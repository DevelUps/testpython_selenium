# Importamos el módulo 'webdriver' y 'time' de Selenium y Python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Instanciamos un objeto de tipo 'webdriver' de Chrome especificando la ruta al archivo ejecutable del controlador de Chrome
driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")

#maximiza la ventana
driver.maximize_window()

# Navegamos a la página web especificada en el URL usando el método 'get' en el objeto 'driver'
driver.get("https://demoqa.com/text-box")
time.sleep(1)

# Envía una cadena al elemento con id "userName"
driver.find_element(By.ID,"userName").send_keys("Pierre")
time.sleep(1)
driver.find_element(By.ID,"userEmail").send_keys("unemail@hotmail.com")
time.sleep(1)
driver.find_element(By.ID,"currentAddress").send_keys(" una direccion tal ")
time.sleep(1)
driver.find_element(By.ID,"permanentAddress").send_keys(" una direccion tal permanente ")
time.sleep(1)
driver.find_element(By.ID,"submit").click()
time.sleep(1)



time.sleep(3)
# Cerramos la ventana del navegador usando el método 'close' en el objeto 'driver'
driver.close()
