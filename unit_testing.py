import unittest , HtmlTestRunner

from selenium import webdriver
from time import sleep

from login_page import Login_Page
from home_page import Home_Page
from subprocess import Popen, PIPE

class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):

		cls.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')

		#cls.driver.implicitly_wait(10)
		
		cls.driver.maximize_window()

	def test_login_01_valid(self):

		driver = self.driver

		driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login");

		sleep(1)

		login = Login_Page(driver)

		login.enter_Username("admin")

		login.enter_Password("admin123")

		login.click_login()

		home_page = Home_Page(driver)

		home_page.click_welcome()

		sleep(2)

		home_page.click_logout()

		sleep(2)

	def test_login_02_invalid(self):

		driver = self.driver

		driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login");

		sleep(1)

		login = Login_Page(driver)

		login.enter_Username("admin1")

		login.enter_Password("admin1")

		login.click_login()

		msg = login.check_invalid_Username()

		self.assertEqual(msg,"Invalid credentials")

		sleep(2)

	@classmethod
	def tearDownClass(cls):

		cls.driver.close();
		cls.driver.quit();

		print("test completed")

def open(file_name):

	Popen(['xdg-open', file_name],stdout=PIPE, stderr=PIPE)

if __name__ == '__main__':

	unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output = "reports"))


