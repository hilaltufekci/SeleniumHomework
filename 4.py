from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_Sauce4:
    def test_invalid_login(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        sleep(5)
        usernameInput=driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(5)
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(5)
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)
        listOfInventory=driver.find_elements(By.CLASS_NAME,"inventory_item")
        testResult=len(listOfInventory)== 6
        print(f"Test Sonucu : {testResult}")
        sleep(5)

testClass=Test_Sauce4()
testClass.test_invalid_login()