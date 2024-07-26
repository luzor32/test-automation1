from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from login_Page import LoginPage
from registration_page import RegistrationPage
#from home_page import HomePage

class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        

    def test_login_successful(self):
        login_Page =LoginPage(self.driver)
        login_Page.load()
        
        login_Page.login("mercury","mercury")
        
        btn_register = self.driver.find_element(By.LINK_TEXT,"REGISTER").click()
        thank_you_message = login_Page.get_thank_you_message()
        assert "Thank you for Loggin." in thank_you_message.text, "El texto esperado no se encontro"
        print("El test de logueo se realizo correctamente")          


    def test_registration_successful(self):

       # homePage = HomePage(self.driver)
        #homePage.go_to_register_page()
        
        registration_page = RegistrationPage(self.driver)
        registration_page.load()  
        btn_register = self.driver.find_element(By.LINK_TEXT,"REGISTER").click()  

        registration_page.register(
            first_name="Lucio",
            last_name="Albornoz",
            phone="3813557956",
            email="lucio.example@gmail.com",
            address="Santa Fe 3232",
            city="San Miguel de Tucumán",
            state="Tucumán",
            postal_code="1234",
            country="ARGENTINA",
            username="luxor",
            password="password123",
            confirm_password="password123")
       
        thank_you_messege2 = registration_page.get_registration_confirmation() 

        self.assertIn("Thank you for registering", thank_you_messege2.text, "El texto esperado no se encontró")
        print("El test de registracion se realizó correctamente")

        
    def tearDown(self): 
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()            


  #assert "Login: Mercury Tours" in driver.title, "La página de éxito de login no se cargó correctamente"

  #thank_you_message = self.driver.find_element(By.CSS_SELECTOR,"font > b")
  

