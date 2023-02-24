from selenium import webdriver


driver=webdriver.Chrome(executable_path=("C:\Drivers\chromedriver.exe)"))
#driver=webdriver.Firefox(executable_path=("C:\Drivers\geckodriver.exe)"))

driver.get(" https://testingqarvn.com.es//")

print("Bienvenido a Selenium")

print(driver.title)

driver.close()