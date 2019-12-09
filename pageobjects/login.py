from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class LoginScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.login_menu = self.element_visible(By.CLASS_NAME, "c-auth__view")

    def enter_username(self, username):
        self.type(By.ID, "login[username]", username)

    def enter_password(self, password):
        self.type(By.ID, "login[password]", password)

    def click_login_button(self):
        self.click_element(By.CLASS_NAME, "p-button")

    def login(self, username, pw):
        self.enter_username(username)
        self.enter_password(pw)
        self.click_login_button()
