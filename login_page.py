

class Login_Page():

	def __init__(self,driver):

		self.driver = driver
		self.username_textbox_id = "txtUsername"
		self.password_textbox_id = "txtPassword"
		self.login_button_id = "btnLogin"
		self.invalid_username_xpath = '//*[@id="spanMessage"]'

	def enter_Username(self,username):

		self.driver.find_element_by_id(self.username_textbox_id).clear()
		self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)
		

	def enter_Password(self,password):


		self.driver.find_element_by_id(self.password_textbox_id).clear()
		self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

	def click_login(self):

		self.driver.find_element_by_id(self.login_button_id).click()

	def check_invalid_Username(self):

		msg = self.driver.find_element_by_xpath(self.invalid_username_xpath).text

		return msg