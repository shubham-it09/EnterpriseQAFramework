from playwright.sync_api import Page,Locator
from pages.dashboard_page import DashboardPage

class AdminPage(DashboardPage):
    def __init__(self,
                 page: Page,
                 logger):

        super().__init__(page, logger)
        
        # Admin Page Elements

        self.username = page.get_by_placeholder(
            "Username"
        )

        self.user_role = page.locator("div:has(> label:has-text('User Role')) .oxd-select-text-input")

        self.employee_name = page.get_by_placeholder(
            "Type for hints..."
        )

        self.status =page.locator("div:has(> label:has-text('Status')) .oxd-select-text-input")

        self.search_button = page.get_by_role(
            "button",
            name="Search"
        )

        self.reset_button = page.get_by_role(
            "button",
            name="Reset"
        )

        self.add_button = page.get_by_role(
            "button",
            name="Add"
        )
    
    def _user_row(self, username: str) -> Locator:
        """
        Returns locator of user row.
        """

        return self.page.locator(
            f"//div[@role='row'][.//*[text()='{username}']]"
        )
    def _edit_button(self, username: str) -> Locator:
        """
        Returns Edit button for given user.
        """

        return self._user_row(username).locator("button").first
    
    def _delete_button(self, username: str) -> Locator:
        """
        Returns Delete button for given user.
        """

        return self._user_row(username).locator("button").last


    def enter_username(self, username: str):

        self.fill(self.username, username)


    def enter_employee_name(self, employee_name: str):

        self.fill(self.employee_name, employee_name)


    def click_search(self):

        self.click(self.search_button)


    def click_reset(self):

        self.click(self.reset_button)

    
    
    def click_add(self):
         self.click(self.add_button)
    

    def click_edit(self, username: str):

        self.click(
            self._edit_button(username)
        )


    def click_delete(self, username: str):

        self.click(
            self._delete_button(username)
        )
    def is_user_present(self, username: str) -> bool:
        """
        Returns True if the user is present in the search results.
        """

        return self.is_visible(
            self._user_row(username)
        )