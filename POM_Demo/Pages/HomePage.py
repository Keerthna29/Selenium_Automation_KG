from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from POM_Demo.Locators.Locators import Locators
class HomePage():

    def __init__(self,driver):
        self.driver=driver
        self.UserMenu_link_xpath=Locators.UserMenu_link_xpath
        self.Logout_link_linkText=Locators.Logout_link_linkText

    def click_usermenu(self):
        self.user_menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.UserMenu_link_xpath)))
        self.user_menu.click()

    def click_logout(self):
        self.logout_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,self.Logout_link_linkText)))
        self.logout_element.click()
