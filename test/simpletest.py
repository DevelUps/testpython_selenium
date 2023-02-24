import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Definir las URL de los sitios web de trabajo en Colombia
urls = ['https://www.computrabajo.com.co/ofertas-de-trabajo/?q=python&prov=11&d=7',
        'https://www.indeed.com.co/trabajo?q=python&l=Colombia&fromage=7']

# Definir la fecha límite de publicación de trabajos (1 semana)
date_limit = datetime.now() - timedelta(days=7)

# Crear una lista vacía para almacenar los trabajos encontrados
jobs = []

for url in urls:
    # Realizar la solicitud HTTP a la URL
    response = requests.get(url)

    # Parsear el HTML de la página con BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar todos los trabajos en la página
    job_list = soup.find_all(class_='iO')

    for job in job_list:
        # Extraer la fecha de publicación del trabajo
        date_string = job.find(class_='dO').text.strip()
        date = datetime.strptime(date_string, '%d/%m/%Y')

        # Comprobar si el trabajo cumple con el límite de fecha
        if date >= date_limit:
            # Extraer el nombre de la empresa y el correo electrónico de contacto
            company_name = job.find(class_='iOj').text.strip()
            email = job.find(class_='at').text.strip()

            # Agregar el trabajo a la lista de trabajos encontrados
            jobs.append({'company_name': company_name, 'email': email})

# Exportar los trabajos encontrados a un archivo de texto
with open('trabajos_python_colombia.txt', 'w') as f:
    for job in jobs:
        f.write(f"Empresa: {job['company_name']}\n")
        f.write(f"Correo electrónico de contacto: {job['email']}\n\n")

print(f'Se encontraron {len(jobs)} trabajos en Python en Colombia.')
