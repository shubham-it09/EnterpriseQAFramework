from playwright.sync_api import Page,Locator
from pages.base_page import Page
from pages.dashboard_page import DashboardPage
import time

class AddUserPage(DashboardPage):
    def __init__(self, page, logger):
        super().__init__(page, logger)

        # Form Controls

        # self.user_role = page.locator(
        #     "div:has(> label:has-text('User Role')) .oxd-select-text-input"
        # )
        # //label[contains(text(),'User Role')]//following::i[1]
        self.user_role = page.locator(
            "//label[contains(text(),'User Role')]//following::i[1]"
        )
        
        self.employee_name = page.get_by_placeholder("Type for hints...")

        self.status = page.locator(
            "//label[contains(text(),'Status')]//following::i[1]"
        )

        self.username = page.locator(
            "div:has(> label:has-text('Username')) + div input"
        )

        self.password = page.locator(
            "div:has(> label:has-text('Password')) + div input"
        ).first

        self.confirm_password = page.locator(
            "div:has(> label:has-text('Confirm Password')) + div input"
        )

        self.save_button = page.get_by_role(
            "button",
            name="Save"
        )

        self.cancel_button = page.get_by_role(
            "button",
            name="Cancel"
        )
    def user_role_option(self, user_role_option: str) -> Locator:
        return self.page.locator(
            f"div[role='option'] span:has-text('{user_role_option}')"
    )


    def status_option(self, status: str) -> Locator:
        return self.page.locator(
            f"div[role='option'] span:has-text('{status}')"
        )
        
    def enter_username(
        self,
        username: str):

        self.fill(
            self.username,
            username
        )
    def enter_employee_name(
        self,
        employee_name: str):
        print("employee name is ",employee_name)
        self.type(self.employee_name,employee_name,delay=10)
        time.sleep(20)
        
        # self.fill(
        #     self.employee_name,
        #     employee_name
        # )
        self.press_key(key="ArrowDown")
        self.press_key(key="Enter")

        
    def enter_password(
        self,
        password: str):

        self.fill(
            self.password,
            password
        )

    def enter_confirm_password(
        self,
        password: str):

        self.fill(
            self.confirm_password,
            password
        ) 
    def click_save(self):

        self.click(
            self.save_button
        )
    def click_cancel(self):

        self.click(
            self.cancel_button
        )
    def select_user_role(self,user_role):
        self.click(self.user_role)
        self.click(self.user_role_option(user_role))

    def select_status(self,status):
        self.click(self.status)
        self.click(self.status_option(status))
