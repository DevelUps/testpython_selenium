Automatización de pruebas con Python y Selenium
Este proyecto utiliza la biblioteca Selenium para automatizar pruebas en la web.

Requisitos
-Python 3.x
-Selenium
-Archivo ejecutable del controlador de Chrome (chromedriver.exe)

Uso
Descargue el archivo ejecutable del controlador de Chrome (chromedriver.exe) y guárdelo en una ubicación conocida.
Instale las dependencias necesarias ejecutando el siguiente comando en su terminal o consola:


1. Descargue el archivo ejecutable del controlador de Chrome (chromedriver.exe) y guárdelo en una ubicación conocida.
2. Instale las dependencias necesarias ejecutando el siguiente comando en su terminal o consola:

> pip install -r requirements.txt

3.Abra el archivo main.py en su editor de código y modifique la línea siguiente para especificar la ruta correcta al archivo ejecutable del controlador de Chrome:
> driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")

4. Ejecute el script con el siguiente comando en su terminal o consola:
>  python main.py

Funcionamiento
El script se encarga de abrir una ventana de navegador de Chrome, navegar a la página web https://demoqa.com/, imprimir en la consola un mensaje de bienvenida y el título de la página web actual, esperar 5 segundos y finalmente cerrar la ventana del navegador

Advertencia
Este script se proporciona solo con fines educativos y de demostración. No se garantiza su correcto funcionamiento en todas las situaciones y puede producir errores no deseados en el sistema. Use bajo su propia responsabilidad.