from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from POM_Demo.Locators.Locators import Locators
class LoginPage():

    def __init__(self,driver):
        self.driver=driver
        # self.username_textbox_Name="username"
        # self.password_textbox_Name="password"
        # self.login_button_Xpath="//*[@id='app']//button"

    def enter_username(self,username):
        self.driver.find_element(By.NAME,Locators.username_textbox_Name).clear()
        self.driver.find_element(By.NAME,Locators.username_textbox_Name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.NAME,Locators.password_textbox_Name).clear()
        self.driver.find_element(By.NAME,Locators.password_textbox_Name).send_keys(password)

    def login_button(self):
        self.element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,Locators.login_button_Xpath)))
        self.element.click()