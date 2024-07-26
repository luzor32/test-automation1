from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.url="https://demo.guru99.com/test/newtours/"

    def load(self):
        self.driver.get(self.url)    

    def login(self, username, password):
        txt_name =WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,"userName")))
        txt_name.send_keys("mercury")

        txt_password = self.driver.find_element(By.NAME,"password")
        txt_password.send_keys("mercury")
        
        btn_login = self.driver.find_element(By.NAME,"submit")
        btn_login.click()

    def get_thank_you_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"font > b")))

        
               