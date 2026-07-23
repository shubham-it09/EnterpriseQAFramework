###########################This is the one method##################################

# from playwright.sync_api import Page

# from pages.base_page import BasePage
# from resources.constants import Menu


# class Sidebar(BasePage):

#     def __init__(self, page: Page, logger):

#         super().__init__(page, logger)

#         self.admin = page.get_by_role(
#             "link",
#             name=Menu.ADMIN
#         )

#         self.pim = page.get_by_role(
#             "link",
#             name=Menu.PIM
#         )

#         self.leave = page.get_by_role(
#             "link",
#             name=Menu.LEAVE
#         )

#         self.time = page.get_by_role(
#             "link",
#             name=Menu.TIME
#         )

#         self.recruitment = page.get_by_role(
#             "link",
#             name=Menu.RECRUITMENT
#         )

#         self.my_info = page.get_by_role(
#             "link",
#             name=Menu.MY_INFO
#         )

#         self.performance = page.get_by_role(
#             "link",
#             name=Menu.PERFORMANCE
#         )

#         self.dashboard = page.get_by_role(
#             "link",
#             name=Menu.DASHBOARD
#         )

#         self.directory = page.get_by_role(
#             "link",
#             name=Menu.DIRECTORY
#         )

#         self.maintenance = page.get_by_role(
#             "link",
#             name=Menu.MAINTENANCE
#         )

#         self.claim = page.get_by_role(
#             "link",
#             name=Menu.CLAIM
#         )

#         self.buzz = page.get_by_role(
#             "link",
#             name=Menu.BUZZ
#         )

#         self.menu_locator=self.page.get_by_role("link",menu_name)

#         self.menu_map = {
#         Menu.ADMIN: self.admin,
#         Menu.PIM: self.pim,
#         Menu.LEAVE: self.leave,
#         Menu.TIME: self.time,
#         Menu.RECRUITMENT: self.recruitment,
#         Menu.MY_INFO: self.my_info,
#         Menu.PERFORMANCE: self.performance,
#         Menu.DASHBOARD: self.dashboard,
#         Menu.DIRECTORY: self.directory,
#         Menu.MAINTENANCE: self.maintenance,
#         Menu.CLAIM: self.claim,
#         Menu.BUZZ: self.buzz
#     }
    

#     def navigate(self, menu_name):
#         if menu_name not in self.menu_map:
#             raise ValueError(f"Invalid menu: {menu_name}")

#         self.click(self.menu_map[menu_name])


###########################Another very short method##################################



from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from resources.constants import Menu


class Sidebar(BasePage):

    def __init__(self, page: Page, logger):

        super().__init__(page, logger)

    def _menu_locator(self, menu_name: str) -> Locator:
        """
        Returns Playwright Locator for the given sidebar menu.
        """

        return self.page.get_by_role(
            "link",
            name=menu_name
        )

    def navigate(self, menu_name: str):
        if not menu_name:
            raise ValueError("Menu name cannot be empty.")

        self.click(self._menu_locator(menu_name))

    # def open_dashboard(self):
    #     self.navigate(Menu.DASHBOARD)

    # def open_admin(self):
    #     self.navigate(Menu.ADMIN)

    # def open_pim(self):
    #     self.navigate(Menu.PIM)

    # def open_leave(self):
    #     self.navigate(Menu.LEAVE)

    # def open_time(self):
    #     self.navigate(Menu.TIME)

    # def open_recruitment(self):
    #     self.navigate(Menu.RECRUITMENT)

    # def open_my_info(self):
    #     self.navigate(Menu.MY_INFO)

    # def open_performance(self):
    #     self.navigate(Menu.PERFORMANCE)

    # def open_directory(self):
    #     self.navigate(Menu.DIRECTORY)

    # def open_maintenance(self):
    #     self.navigate(Menu.MAINTENANCE)

    # def open_claim(self):
    #     self.navigate(Menu.CLAIM)

    # def open_buzz(self):
    #     self.navigate(Menu.BUZZ)