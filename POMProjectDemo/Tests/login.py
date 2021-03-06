from selenium import webdriver
import HtmlTestRunner
import xlrd
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.homePage import HomePage

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='C:/Users/Allah/Desktop/Pythan/Projects/FirstSeleniumTest/Drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        DataSheet = ("C:\Users\Allah\Desktop\Data.xls")
        wb = xlrd.open_workbook(DataSheet)
        sheet = wb.sheet_by_index(0)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        # login.enter_username("Admin")
        # login.enter_password("admin123")
        username = sheet.cell_value(1, 0)
        password = sheet.cell_value(1, 1)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Allah/Desktop/Pythan/Projects/Selenium/reports/abc.html'))
