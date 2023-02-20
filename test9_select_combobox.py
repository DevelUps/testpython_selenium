# Import the 'webdriver' and 'time' modules from Selenium and Python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
print("Drivers have been successfully loaded.")

# Instantiate a Chrome 'webdriver' object by specifying the path to the Chrome driver executable file
driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")
print("Drivers have been successfully loaded.")

# Navigate to the web page specified in the URL using the 'get' method on the 'driver' object
driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
print("Web page has been successfully loaded.")

# Maximize the window
driver.maximize_window()
print("Window has been maximized.")

# Implicitly wait for 10 seconds for the page to load
driver.implicitly_wait(10)
print("Implicitly waiting for 10 seconds for the page to load.")

# Time delay for the execution of each task
t = 0.01
print("Locate if the element exists")
#day = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "//select[contains(@id,'wsf-1-field-53')]")))
daySelect=driver.find_element(By.XPATH,"//select[@id='select-demo']")
driver.execute_script("window.scrollTo(0,500)")
day = Select(daySelect)
time.sleep(t)
print("Select Sunday OK")
time.sleep(t)
day.select_by_index(1)
time.sleep(t)
print("Select Monday OK")
day.select_by_index(2)
time.sleep(t)
print("Select Tuesday OK")
day.select_by_index(3)
time.sleep(t)
print("Select Wednesday OK")
day.select_by_index(4)
time.sleep(t)
print("Select Thursday OK")
day.select_by_index(5)
time.sleep(t)
print("Select Friday OK")
day.select_by_index(6)
time.sleep(t)

print("Select Saturday OK")
day.select_by_index(7)
time.sleep(t)
print("The select list is ok")
print("A second play list Join in multi select list")
ct=driver.find_element(By.ID,"multi-select")
ct = Select(ct)
print("Multi-select has been selected")
time.sleep(t)
ct.select_by_index(0)
print("Select California OK")
time.sleep(t)
ct.select_by_index(1)
print("Select Florida OK")
time.sleep(t)
ct.select_by_index(2)
print("Select New Jersey OK")
time.sleep(t)
ct.select_by_index(3)
print("Select New York OK")
time.sleep(t)
ct.select_by_index(4)
print("Select Ohio OK")
time.sleep(t)
ct.select_by_index(5)
print("Select Texas OK")
ct.select_by_index(6)
print("Select Pennsylvania OK")
time.sleep(t)
ct.select_by_index(7)
print("Select New Washington OK")
time.sleep(t)
print("Finished automation of Multi-checkbox OK")

# Close the browser window using the 'close' method on the object
driver.close()

print("The test has been successful. The window and drivers have been closed.")
print("This was a test generated by software development engineer Pierre Grandett - Develups.")
