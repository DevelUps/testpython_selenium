# Importamos el módulo 'webdriver' y 'time' de Selenium y Python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 


# Instanciamos un objeto de tipo 'webdriver' de Chrome especificando la ruta al archivo ejecutable del controlador de Chrome
driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")
t=4
# Maximiza la ventana
driver.maximize_window()
# Imprimimos mensaje de bienvenida
print("Bienvenido al sistema de búsqueda de portales de empleo")
print("En breve te mostrare varias opciones de portales de empleos")

# Navegamos a cada sitio web de portal de empleo y luego volvemos atrás en cada uno
sites = ["https://www.linkedin.com/", "https://www.elempleo.com/", "https://eficacia.zohorecruit.com/",
         "https://www.michaelpage.com.co/", "https://falabella.airavirtual.com/l", "https://www.infojobs.net/",
         "https://login.magneto365.com/", "https://personas.serviciodeempleo.gov.co/", "https://ticjob.co/"]
for site in sites:
    print(site)
    driver.get(site)
    time.sleep(0.5)
    driver.back()
    driver.execute_script("window.history.go(-1)")
   

# Imprimimos mensaje de despedida
print("Gracias por visitarnos, hasta pronto!")

# Cerramos el objeto 'webdriver' de Chrome
driver.close()
