from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


class LoginBusiness:

    def __init__(self,
                 page,
                 logger):

        self.login_page = LoginPage(
            page,
            logger
        )

        self.dashboard_page = DashboardPage(
            page,
            logger
        )
    def login(self,username: str,password: str):
        
        self.login_page.open()

        self.login_page.enter_credentials(username,password)

        self.login_page.click_login()

        
    def login_as_admin(self):

        self.login(
            "Admin",
            "admin123"
    )