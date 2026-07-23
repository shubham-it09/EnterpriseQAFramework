from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class UserDropdown(BasePage):

    def __init__(self, page: Page, logger):

        super().__init__(page, logger)

        self.user_dropdown = page.locator(".oxd-userdropdown")

    def _user_dropdown_locator(self, option: str) -> Locator:
        """
        Returns locator for a user dropdown option.
        """

        return self.page.get_by_role(
            "menuitem",
            name=option
        )

    def _open_dropdown(self):
        """
        Opens the user dropdown.
        """

        self.click(self.user_dropdown)

    def select_option(self, option: str):

        if not option:
            raise ValueError("Dropdown option cannot be empty.")

        self._open_dropdown()

        self.click(self._user_dropdown_locator(option))