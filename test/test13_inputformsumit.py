# Print message to indicate that the 'webdriver' and 'time' modules are being imported from Selenium and Python
print("Importing 'webdriver' and 'time' modules from Selenium and Python...")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# Print message to indicate that drivers have been loaded successfully
print("Drivers have been successfully loaded.")

# Instantiate a webdriver object of Chrome by specifying the path to the Chrome driver executable file
print("Instantiating a webdriver object of Chrome...")

driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")

# Maximize the window
#print("Maximizing the window...")

#driver.maximize_window()

# Define wait time
t = 0.001

# Navigate to the webpage specified in the URL using the 'get' method on the 'driver' object
print("Navigating to the webpage...")

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")

# Enter first name
print("Entering first name...")

driver.find_element(By.XPATH, "//input[contains(@name,'first_name')]").send_keys("Pepito")
time.sleep(t)

# Enter last name
print("Entering last name...")

driver.find_element(By.XPATH, "//input[contains(@name,'last_name')]").send_keys("perez")
time.sleep(t)

# Enter email
print("Entering email...")

driver.find_element(By.XPATH, "//input[contains(@name,'email')]").send_keys("Pepito@gmail.com")
time.sleep(t)

# Enter phone number
print("Entering phone number...")

driver.find_element(By.XPATH, "//input[contains(@name,'phone')]").send_keys("3010818422")
time.sleep(t)

# Enter address
print("Entering address...")

driver.find_element(By.XPATH, "//input[contains(@name,'address')]").send_keys("Primera direccion")
time.sleep(t)

# Enter city
print("Entering city...")

driver.find_element(By.XPATH, "//input[contains(@name,'city')]").send_keys("Barranquilla")
time.sleep(t)

# Select state
print("Selecting state...")

stSelect = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@name,'state')]")))
st = Select(stSelect)
st.select_by_index(3)
time.sleep(t)

# Enter zip code
print("Entering zip code...")

driver.find_element(By.XPATH, "//input[contains(@name,'zip')]").send_keys("85001")
time.sleep(t)

# Enter website
print("Entering website...")

driver.find_element(By.XPATH, "//input[contains(@name,'website')]").send_keys("https://demo.seleniumeasy.com/")
time.sleep(t)

# Select first checkbox
print("Selecting first checkbox...")

checkbox1 = driver.find_element(By.XPATH, "//label[contains(.,'Yes')]")
checkbox1.click()
print("Button 1 has been selected.")

# Enter project description
print("Entering project description...")

driver.find_element(By.XPATH, "//textarea[contains(@class,'form-control')]").send_keys("Se requiere realizar el registro por que soy estudiante")
time.sleep(t)

# Click the submit button
print("Clicking the submit button...")

driver.find_element(By.XPATH, "//button[@type='submit'][contains(text(),'Send')]").click()
time.sleep(t)

# Print message to indicate that the form has been submitted
print("The form has been submitted successfully.")



driver.close()
print("The test has been successful. The window and drivers have been closed.")
print("This was a test generated by software development Engineer Pierre Grandett - Develups.")
