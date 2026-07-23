from pages.base_page import BasePage
from playwright.sync_api import Page

class Header(BasePage):
    
    def __init__(self,page:Page,logger):
        super().__init__(page,logger)
        self.search_box=page.get_by_placeholder("Search")
        self.logged_in_user=page.locator(".oxd-userdropdown-name")

    def search(self, text: str):

        self.fill(
            self.search_box,
            text
        )

    def get_logged_in_username(self) -> str:

        return self.get_text(
            self.logged_in_user
        )

