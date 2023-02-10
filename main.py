from selenium import webdriver

driver=webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")

driver.get("https://testingqarvn.com.es/")
print("Bienvenido a prueba automatizada con python y selenium")

print(driver.title)
#driver.close(TimeoutError)#