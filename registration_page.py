from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class RegistrationPage:
    def __init__(self,driver):
        self.driver = driver
        self.url="https://demo.guru99.com/test/newtours/"
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(self.url)

    def go_to_register_page(self):
        # Esperar y hacer clic en el enlace de registro
        register_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "REGISTER")))
        register_link.click() 
        

    def register(self,first_name, last_name, phone, email, address, city, state, postal_code, country, username, password, confirm_password):
        

        first_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, 'firstName'))).send_keys("lucio")
        last_name = self.driver.find_element(By.NAME, 'lastName').send_keys("Albornoz")
        phone = self.driver.find_element(By.NAME, 'phone').send_keys("3813557956")
        email = self.driver.find_element(By.NAME, 'userName').send_keys("lucio.example@gmail.com")
        address = self.driver.find_element(By.NAME, 'address1').send_keys("santa fe 3232")
        city = self.driver.find_element(By.NAME, 'city').send_keys("san miguel de tucuman")
        Province = self.driver.find_element(By.NAME, 'state').send_keys("Tucuman")
        postal_code = self.driver.find_element(By.NAME, 'postalCode').send_keys("1234")
        wait = WebDriverWait(self.driver, 10)
        country_dropdown = wait.until(EC.presence_of_element_located((By.NAME,"country")))
        Select(country_dropdown).select_by_visible_text(country)
        wait = WebDriverWait(self.driver, 10)
        user_name = self.driver.find_element(By.NAME, 'email').send_keys("luxor")
        password = self.driver.find_element(By.NAME, 'password').send_keys("password123")
        confirm_password = self.driver.find_element(By.NAME, 'confirmPassword').send_keys("password123")
        submit = self.driver.find_element(By.NAME, 'submit').click()

    def get_registration_confirmation(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//tr[3]/td/p[2]/font')))