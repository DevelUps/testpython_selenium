Automating Tests with Python and Selenium
This project uses the Selenium library to automate tests on the web.

Requirements

Python 3.x
Selenium
Chrome Driver Executable File (chromedriver.exe)
Usage

Download the Chrome Driver Executable File (chromedriver.exe) and save it in a known location.
Install the necessary dependencies by running the following command in your terminal or console:
pip install -r requirements.txt

Open the main.py file in your code editor and modify the following line to specify the correct path to the Chrome Driver Executable File:
driver = webdriver.Chrome("executable_path=C:\Drivers\chromedriver.exe")

FOR Run the scripts with the following command in your terminal or console:
python "name.py"
test1_XPATH_sel 
test2_ID_sel
test3_CSS_sel

Operation
The script takes care of opening a Chrome browser window, navigating to the https://demoqa.com/ web page, printing a welcome message and the current web page title to the console, waiting for 5 seconds, and finally closing the browser window.

Warning
This script is provided for educational and demonstration purposes only. Its correct operation in all situations is not guaranteed and it may produce unintended errors in the system. Use at your own risk.