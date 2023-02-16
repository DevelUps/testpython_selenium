# Importamos el módulo 'webdriver' y 'time' de Selenium y Python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 


# Instanciamos un objeto de tipo 'webdriver' de Chrome especificando la ruta al archivo ejecutable del controlador de Chrome
driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")
# Navegamos a la página web especificada en el URL usando el método 'get' en el objeto 'driver'
driver.get("https://demoqa.com/text-box")
#maximiza la ventana
driver.maximize_window()
driver.implicitly_wait(10)

t=.1
time.sleep(t)

# Envía una cadena al elemento con id "userName"
driver.find_element(By.CSS_SELECTOR,"#userName").send_keys("Pierre")
time.sleep(t)
driver.find_element(By.CSS_SELECTOR,"#userEmail").send_keys("unemail@hotmail.com")
time.sleep(t)
driver.find_element(By.CSS_SELECTOR,"#currentAddress").send_keys(" una direccion tal ")
time.sleep(t)
driver.find_element(By.CSS_SELECTOR,"#permanentAddress").send_keys(" una direccion tal permanente ")
time.sleep(t)
driver.find_element(By.CSS_SELECTOR,"#submit").click()
time.sleep(t)

time.sleep(3)
# Cerramos la ventana del navegador usando el método 'close' en el objeto 'driver'
driver.close()
