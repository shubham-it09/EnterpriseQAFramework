from playwright.sync_api import Page

from components.header import Header
from components.sidebar import Sidebar
from components.user_dropdown import UserDropdown
from pages.base_page import BasePage


class DashboardPage(BasePage):

    def __init__(self, page: Page, logger):

        super().__init__(page, logger)

        self.sidebar = Sidebar(
            page,
            logger
        )

        self.header = Header(
            page,
            logger
        )

        self.user_dropdown = UserDropdown(
            page,
            logger
        )