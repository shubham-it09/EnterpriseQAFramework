from playwright.sync_api import Page

from pages.base_page import BasePage
from config.config_manager import config


class LoginPage(BasePage):

    def __init__(self, page: Page, logger):

        super().__init__(page, logger)

        self.username = page.get_by_placeholder(
            "Username"
        )

        self.password = page.get_by_placeholder(
            "Password"
        )

        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )

        self.forgot_password = page.get_by_text(
            "Forgot your password?"
        )

        self.error_message = page.locator(
            ".oxd-alert-content-text"
        )
    def open(self):

        self.navigate_to_url(
            config.base_url
        )
    def enter_username(
        self,
        username: str
    ):

        self.fill(
            self.username,
            username
        )
    def enter_password(
        self,
        password: str
    ):

        self.fill(
            self.password,
            password
        )
    def click_login(self):

        self.click(
            self.login_button
        )
    def click_forgot_password(self):

        self.click(
            self.forgot_password
        )
    def get_error_message(self):

        return self.get_text(
            self.error_message
        )
    def enter_credentials(self,username: str,password: str):
       self.enter_username(username)
       self.enter_password(password)