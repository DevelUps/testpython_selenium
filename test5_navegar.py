# Importamos el módulo 'webdriver' y 'time' de Selenium y Python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 


# Instanciamos un objeto de tipo 'webdriver' de Chrome especificando la ruta al archivo ejecutable del controlador de Chrome
driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")

# Maximiza la ventana
driver.maximize_window()
print("Bienvenido al sistema de busqueda de portales de empleo")
print("En breve te mostrare varias opciones de portales de empleos")
# Navegamos a la página web especificada en el URL usando el método 'get' en el objeto 'driver'
print("linkedin")
driver.get("https://www.linkedin.com/")
time.sleep(1)
print("el empleo")
driver.get("https://www.elempleo.com/")
time.sleep(1)
print("eficacia")
driver.get("https://eficacia.zohorecruit.com/")
time.sleep(1)
print("michaelpage")
driver.get("https://www.michaelpage.com.co/")
time.sleep(1)
print("falabella")
driver.get("https://falabella.airavirtual.com/l")
time.sleep(1)
print("infojobs")
driver.get("https://www.infojobs.net/")
time.sleep(1)
print("magneto365")
driver.get("https://login.magneto365.com/c")
time.sleep(1)
print("servicio de empleo")
driver.get("https://personas.serviciodeempleo.gov.co/")
time.sleep(1)
print("ticjob")
driver.get("https://ticjob.co/es/")
time.sleep(1)

print("Gracias por visitarnos, hasta pronto!")
driver.close()