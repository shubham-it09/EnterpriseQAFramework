from resources.constants import Menu

from pages.admin.admin_page import AdminPage
from pages.admin.add_user_page import AddUserPage
from models import UserData


class AdminBusiness:

    def __init__(self,
                 page,
                 logger):

        self.admin_page = AdminPage(
            page,
            logger
        )

        self.add_user_page = AddUserPage(
            page,
            logger
        )
    def open_admin(self):
        self.admin_page.sidebar.navigate(Menu.ADMIN)
    
    def add_user(
        self,
        user: UserData
        ):

        self.admin_page.click_add()

        self.add_user_page.select_user_role(
            user.role
        )

        self.add_user_page.enter_employee_name(
            user.employee_name
        )

        # self.add_user_page.select_status(
        #     user.status
        # )

        self.add_user_page.enter_username(
            user.username
        )

        self.add_user_page.enter_password(
            user.password
        )

        self.add_user_page.enter_confirm_password(
            user.password
        )

        self.add_user_page.click_save()