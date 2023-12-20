from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_Sauce2:
    def test_invalid_login(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com")
        driver.maximize_window()
        sleep(5)
        usernameInput=driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        sleep(5)
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys("")
        sleep(5)
        loginButton=driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage=driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult=errorMessage.text=="Epic sadface: Password is required"
        print(f"Test Sonucu: {testResult}")
        sleep(5)

testClass=Test_Sauce2()
testClass.test_invalid_login()