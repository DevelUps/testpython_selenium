# Importamos el módulo 'webdriver' y 'time' de Selenium y Python
from selenium import webdriver
import time

# Instanciamos un objeto de tipo 'webdriver' de Chrome especificando la ruta al archivo ejecutable del controlador de Chrome
driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")

# Navegamos a la página web especificada en el URL usando el método 'get' en el objeto 'driver'
driver.get("https://demoqa.com/")

# Imprimimos en la consola un mensaje de bienvenida
print("Bienvenido a prueba automatizada con Python y Selenium")

# Imprimimos en la consola el título de la página web actual
print(driver.title)

# Esperamos 5 segundos antes de cerrar la ventana del navegador
time.sleep(5)

# Cerramos la ventana del navegador usando el método 'close' en el objeto 'driver'
driver.close()
