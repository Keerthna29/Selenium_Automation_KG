import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from POM_Demo.Pages.LoginPage import LoginPage
from POM_Demo.Pages.HomePage import HomePage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


class Login_tests(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def test_login(self):
        driver=self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.implicitly_wait(5)

        login =LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.login_button()

        time.sleep(2)

        homepage=HomePage(driver)
        homepage.click_usermenu()
        homepage.click_logout()

        time.sleep(2)

        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # self.element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']//button")))
        # self.element.click()
        # self.user_menu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']//div/ul/li/span[@class='oxd-userdropdown-tab']")))
        # self.user_menu.click()
        # time.sleep(5)
        # self.logout_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Logout")))
        # self.logout_element.click()
        # time.sleep(5)
        print("Test Completed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    if __name__=='__main__':
        unittest.main()





