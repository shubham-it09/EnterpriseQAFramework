# from config.config_manager import config
# from playwright.sync_api import Page,Locator

# class BasePage:
#     def __init__(self,page: Page,logger):

#         self.page = page

#         self.logger = logger

#         self.timeout = config.timeout

#     def navigate_to_url(self, url: str):

#         self.page.goto(url)


#     def _get_locator(self, locator: str | Locator) -> Locator:
#         """
#         Converts string locator into Playwright Locator.

#         If Locator is already supplied, return it directly.
#         """
#         if isinstance(locator,Locator):
#             return locator
#         return self.page.locator(locator)
    
#     def _log(self, message: str):
#         if self.logger:
#             self.logger.info(message)

#     def _log_action(
#         self,
#         action: str,
#         locator: str | Locator | None = None,
#         value: str | None = None
#     ):
#         """
#         Logs framework actions.
#         """

#         if not self.logger:
#             return

#         message = f"\nACTION  : {action}"

#         if locator is not None:
#             message += f"\nLOCATOR : {locator}"

#         if value is not None:
#             message += f"\nVALUE   : {value}"

#         self.logger.info(message)

#     def click(self, locator: str | Locator):
#         self._log_action(f"Click : {locator}")
#         self._get_locator(locator).click()

#     def fill(self,locator: str | Locator,value: str):
#         self._log_action("FILL",locator,value)
#         self._get_locator(locator).fill(value)

#     def clear(self, locator: str | Locator):
#         self._log_action("CLEAR",locator)
#         self._get_locator(locator).clear()
    
#     def type(self,locator: str | Locator,value: str,delay: int = 50):
#         self._log_action("TYPE",locator,value)
#         self._get_locator(locator).press_sequentially(
#             value,
#             delay=delay
#         )

#     def hover(self,locator: str | Locator):
#         self._log_action("Hovering",locator)
#         self._get_locator(locator).hover()


#     def double_click(self,locator: str | Locator):
#         self._log_action("DOUBLE CLICK",locator)
#         self._get_locator(locator).dblclick()
    
#     def right_click(self,locator: str | Locator):

#             self._log_action("RIGHT CLICK",locator)

#             self._get_locator(locator).click(
#                 button="right"
#             )
#     def check(self,locator: str | Locator):
#         self._log_action("CHECK",locator)
#         self._get_locator(locator).check()
    
#     def uncheck(self,locator: str | Locator):
#         self._log_action("Uncheck",locator)
#         self._get_locator(locator).uncheck()
        
#     def select_option(
#             self,
#             locator: str | Locator,
#             value: str):

#         self._log_action("SELECT OPTION",locator,value)
#         self._get_locator(locator).select_option(value)
    
#     def upload_file(self,locator: str | Locator,file_path: str):

#         self._log_action("UPLOAD FILE",locator,file_path)

#         self._get_locator(locator).set_input_files(file_path)
    
#     def drag_and_drop(
#             self,
#             source: str | Locator,
#             target: str | Locator):

#         self._log_action("DRAG AND DROP",source,    str(target))

#         self._get_locator(source).drag_to(
#             self._get_locator(target)
#         )
#     def press(
#             self,
#             locator: str | Locator,
#             key: str):

#         self._log(f"Pressing : {key}")

#         self._get_locator(locator).press(key)
    
#     def is_visible(self, locator: str | Locator) -> bool:
#         """
#         Returns True if element is visible.
#         """

#         self._log(f"Checking visibility : {locator}")

#         return self._get_locator(locator).is_visible()

#     def is_hidden(self, locator: str | Locator) -> bool:
#         """
#         Returns True if element is hidden.
#         """

#         self._log(f"Checking hidden state : {locator}")

#         return self._get_locator(locator).is_hidden()
    
#     def is_enabled(self, locator: str | Locator) -> bool:
#         """
#         Returns True if element is enabled.
#         """

#         self._log(f"Checking enabled state : {locator}")

#         return self._get_locator(locator).is_enabled()
    
#     def is_disabled(self, locator: str | Locator) -> bool:
#         """
#         Returns True if element is disabled.
#         """

#         self._log(f"Checking disabled state : {locator}")

#         return self._get_locator(locator).is_disabled()
    
#     def is_checked(self, locator: str | Locator) -> bool:
#         """
#         Returns True if checkbox is checked.
#         """

#         self._log(f"Checking checkbox state : {locator}")

#         return self._get_locator(locator).is_checked()
    
#     def is_editable(self, locator: str | Locator) -> bool:
#         """
#         Returns True if element is editable.
#         """

#         self._log(f"Checking editable state : {locator}")

#         return self._get_locator(locator).is_editable()
    
#     def wait_for(
#     self,
#     locator: str | Locator,
#     state: str = "visible",
#     timeout: int = 30000
#     ):
#         """
#         Waits until element reaches expected state.
#         """

#         self._log(f"Waiting for '{state}' : {locator}")

#         self._get_locator(locator).wait_for(
#             state=state,
#             timeout=timeout
#         )
#     def wait_for_visible(
#     self,
#     locator: str | Locator,
#     timeout: int = 30000
#     ):
#         """
#         Wait until element becomes visible.
#         """

#         self.wait_for(locator, "visible", timeout)
#     def wait_for_enabled(
#     self,
#     locator: str | Locator,
#     timeout: int = 30000
#     ):
#         """
#         Wait until element becomes enabled.
#         """

#         self._log(f"Waiting for enabled : {locator}")

#         self.page.wait_for_function(
#             """
#             element => !element.disabled
#             """,
#             arg=self._get_locator(locator).element_handle(),
#             timeout=timeout
#         )
    
#     def wait_for_url(
#     self,
#     url: str,
#     timeout: int = 30000
#     ):
#         """
#         Wait until URL matches.
#         """

#         self._log(f"Waiting for URL : {url}")

#         self.page.wait_for_url(
#             url,
#             timeout=timeout
#         )
    
#     def wait_for_load_state(
#     self,
#     state: str = "load"
#     ):
#         """
#         Wait for page load state.
#         """

#         self._log(f"Waiting for page load : {state}")

#         self.page.wait_for_load_state(state)
    
#     def get_title(self) -> str:
#         """
#         Returns page title.
#         """

#         return self.page.title()
#     def get_url(self) -> str:
#         """
#         Returns current URL.
#         """

#         return self.page.url
    
#     def get_text(
#     self,
#     locator: str | Locator
#     ) -> str:
#         """
#         Returns inner text.
#         """

#         return self._get_locator(locator).inner_text()
    
#     def get_attribute(
#     self,
#     locator: str | Locator,
#     attribute: str
#     ) -> str | None:
#         """
#         Returns attribute value.
#         """

#         return self._get_locator(locator).get_attribute(attribute)
    
#     def get_input_value(
#     self,
#     locator: str | Locator
#     ) -> str:
#         """
#         Returns input value.
#         """

#         return self._get_locator(locator).input_value()
    
#     def count(
#     self,
#     locator: str | Locator
#     ) -> int:
#         """
#         Returns total matching elements.
#         """

#         return self._get_locator(locator).count()
    
#     def all_text_contents(
#     self,
#     locator: str | Locator
#     ) -> list[str]:
#         """
#         Returns all matching text values.
#         """

#         return self._get_locator(locator).all_inner_texts()

#     def scroll_into_view(
#     self,
#     locator: str | Locator
#     ):

#         self._log("Scrolling element into view")

#         self._get_locator(locator).scroll_into_view_if_needed()


#     def scroll_to_top(self):

#         self._log("Scrolling to page top")

#         self.page.evaluate(
#             "window.scrollTo(0,0)"
#         )

#     def scroll_to_bottom(self):

#         self._log("Scrolling to page bottom")

#         self.page.evaluate(
#             "window.scrollTo(0,document.body.scrollHeight)"
#         )


#     def focus(
#         self,
#         locator: str | Locator
#     ):

#         self._log("Setting focus")

#         self._get_locator(locator).focus()

#     def take_screenshot(
#     self,
#     locator: str | Locator,
#     path: str
#     ):

#         self._log("Taking element screenshot")

#         self._get_locator(locator).screenshot(
#             path=path
#         )
#     def js_click(
#     self,
#     locator: str | Locator
#     ):

#         self._log("JavaScript Click")

#         self.page.evaluate(
#             "(element)=>element.click()",
#             self._get_locator(locator)
#         )

#     def highlight_element(self,locator: str | Locator):
#             self.page.evaluate(
#                 """
#                 element=>{
#                     element.style.border='3px solid red';
#                 }
#                 """,
#                 self._get_locator(locator)
#             )
#     def press_key(self,key: str):
#         self.page.keyboard.press(key)
    
#     def type_text(self,text: str,delay: int = 30):
#         self.page.keyboard.type(
#             text,
#             delay=delay
#         )
#     def select_all(self):
#         self.page.keyboard.press("Control+A")
    
#     def accept_dialog(self):

#         self.page.once(
#             "dialog",
#             lambda dialog: dialog.accept()
#         )
    
#     def dismiss_dialog(self):

#         self.page.once(
#             "dialog",
#             lambda dialog: dialog.dismiss()
#         )
    
#     def accept_prompt(
#     self,
#     text: str
#     ):

#         self.page.once(
#             "dialog",
#             lambda dialog: dialog.accept(text)
#         )

#     def expect_download(self):

#         return self.page.expect_download()
    
#     def expect_popup(self):

#         return self.page.expect_popup()


from config.config_manager import config
from playwright.sync_api import Page,Locator

class BasePage:
    def __init__(self,page: Page,logger):

        self.page = page

        self.logger = logger

        self.timeout = config.timeout

    def navigate_to_url(self, url: str):

        self.page.goto(url)


    def _get_locator(self, locator: str | Locator) -> Locator:
        """
        Converts string locator into Playwright Locator.

        If Locator is already supplied, return it directly.
        """
        if isinstance(locator,Locator):
            return locator
        return self.page.locator(locator)
    
    def _log(self, message: str):
        if self.logger:
            self.logger.info(message)

    def _log_action(
        self,
        action: str,
        locator: str | Locator | None = None,
        value: str | None = None
    ):
        """
        Logs framework actions.
        """

        if not self.logger:
            return

        message = f"\nACTION  : {action}"

        if locator is not None:
            message += f"\nLOCATOR : {locator}"

        if value is not None:
            message += f"\nVALUE   : {value}"

        self.logger.info(message)

    def click(self, locator: str | Locator):
        self._log_action("CLICK", locator)
        self._get_locator(locator).click()

    def fill(self,locator: str | Locator,value: str):
        self._log_action("FILL",locator,value)
        self._get_locator(locator).fill(value)

    def clear(self, locator: str | Locator):
        self._log_action("CLEAR",locator)
        self._get_locator(locator).clear()
    
    def type(self,locator: str | Locator,value: str,delay: int = 50):
        self._log_action("TYPE",locator,value)
        self._get_locator(locator).press_sequentially(
            value,
            delay=delay
        )

    def hover(self,locator: str | Locator):
        self._log_action("HOVER", locator)
        self._get_locator(locator).hover()


    def double_click(self,locator: str | Locator):
        self._log_action("DOUBLE CLICK",locator)
        self._get_locator(locator).dblclick()
    
    def right_click(self,locator: str | Locator):

            self._log_action("RIGHT CLICK",locator)

            self._get_locator(locator).click(
                button="right"
            )
    def check(self,locator: str | Locator):
        self._log_action("CHECK",locator)
        self._get_locator(locator).check()
    
    def uncheck(self,locator: str | Locator):
        self._log_action("UNCHECK", locator)
        self._get_locator(locator).uncheck()
        
    def select_option(
            self,
            locator: str | Locator,
            value: str):

        self._log_action("SELECT OPTION",locator,value)
        self._get_locator(locator).select_option(value)
    
    def upload_file(self,locator: str | Locator,file_path: str):

        self._log_action("UPLOAD FILE",locator,file_path)

        self._get_locator(locator).set_input_files(file_path)
    
    def drag_and_drop(
            self,
            source: str | Locator,
            target: str | Locator):

        self._log_action("DRAG AND DROP",source,    str(target))

        self._get_locator(source).drag_to(
            self._get_locator(target)
        )
    def press(
            self,
            locator: str | Locator,
            key: str):

        self._log_action("PRESS KEY", locator, key)

        self._get_locator(locator).press(key)
    
    def is_visible(self, locator: str | Locator) -> bool:
        """
        Returns True if element is visible.
        """

        self._log_action("CHECK VISIBILITY", locator)

        return self._get_locator(locator).is_visible()

    def is_hidden(self, locator: str | Locator) -> bool:
        """
        Returns True if element is hidden.
        """

        self._log_action("CHECK HIDDEN", locator)

        return self._get_locator(locator).is_hidden()
    
    def is_enabled(self, locator: str | Locator) -> bool:
        """
        Returns True if element is enabled.
        """

        self._log_action("CHECK ENABLED", locator)

        return self._get_locator(locator).is_enabled()
    
    def is_disabled(self, locator: str | Locator) -> bool:
        """
        Returns True if element is disabled.
        """

        self._log_action("CHECK DISABLED", locator)

        return self._get_locator(locator).is_disabled()
    
    def is_checked(self, locator: str | Locator) -> bool:
        """
        Returns True if checkbox is checked.
        """

        self._log_action("CHECK CHECKED", locator)

        return self._get_locator(locator).is_checked()
    
    def is_editable(self, locator: str | Locator) -> bool:
        """
        Returns True if element is editable.
        """

        self._log_action("CHECK EDITABLE", locator)

        return self._get_locator(locator).is_editable()
    
    def wait_for(
    self,
    locator: str | Locator,
    state: str = "visible",
    timeout: int | None = None
    ):
        """
        Waits until element reaches expected state.
        """

        timeout = timeout or self.timeout

        self._log_action("WAIT", locator, state)

        self._get_locator(locator).wait_for(
            state=state,
            timeout=timeout
        )
    def wait_for_visible(
    self,
    locator: str | Locator,
    timeout: int | None = None
    ):
        """
        Wait until element becomes visible.
        """

        self.wait_for(locator, "visible", timeout)
    def wait_for_enabled(
    self,
    locator: str | Locator,
    timeout: int | None = None
    ):
        """
        Wait until element becomes enabled.
        """

        timeout = timeout or self.timeout

        self._log_action("WAIT ENABLED", locator)

        self.page.wait_for_function(
            """
            element => !element.disabled
            """,
            arg=self._get_locator(locator).element_handle(),
            timeout=timeout
        )
    
    def wait_for_url(
    self,
    url: str,
    timeout: int | None = None
    ):
        """
        Wait until URL matches.
        """

        timeout = timeout or self.timeout

        self._log_action("WAIT URL", value=url)

        self.page.wait_for_url(
            url,
            timeout=timeout
        )
    
    def wait_for_load_state(
    self,
    state: str = "load"
    ):
        """
        Wait for page load state.
        """

        self._log_action("WAIT PAGE LOAD", value=state)

        self.page.wait_for_load_state(state)
    
    def get_title(self) -> str:
        """
        Returns page title.
        """

        return self.page.title()
    def get_url(self) -> str:
        """
        Returns current URL.
        """

        return self.page.url
    
    def get_text(
    self,
    locator: str | Locator
    ) -> str:
        """
        Returns inner text.
        """

        return self._get_locator(locator).inner_text()
    
    def get_attribute(
    self,
    locator: str | Locator,
    attribute: str
    ) -> str | None:
        """
        Returns attribute value.
        """

        return self._get_locator(locator).get_attribute(attribute)
    
    def get_input_value(
    self,
    locator: str | Locator
    ) -> str:
        """
        Returns input value.
        """

        return self._get_locator(locator).input_value()
    
    def count(
    self,
    locator: str | Locator
    ) -> int:
        """
        Returns total matching elements.
        """

        return self._get_locator(locator).count()
    
    def all_text_contents(
    self,
    locator: str | Locator
    ) -> list[str]:
        """
        Returns all matching text values.
        """

        return self._get_locator(locator).all_inner_texts()

    def scroll_into_view(
    self,
    locator: str | Locator
    ):

        self._log_action("SCROLL INTO VIEW", locator)

        self._get_locator(locator).scroll_into_view_if_needed()


    def scroll_to_top(self):

        self._log_action("SCROLL TOP")

        self.page.evaluate(
            "window.scrollTo(0,0)"
        )

    def scroll_to_bottom(self):

        self._log_action("SCROLL BOTTOM")

        self.page.evaluate(
            "window.scrollTo(0,document.body.scrollHeight)"
        )


    def focus(
        self,
        locator: str | Locator
    ):

        self._log_action("FOCUS", locator)

        self._get_locator(locator).focus()

    def take_screenshot(
    self,
    locator: str | Locator,
    path: str
    ):

        self._log_action("ELEMENT SCREENSHOT", locator, path)

        self._get_locator(locator).screenshot(
            path=path
        )
    def js_click(
    self,
    locator: str | Locator
    ):

        self._log_action("JS CLICK", locator)

        self.page.evaluate(
            "(element)=>element.click()",
            self._get_locator(locator)
        )

    def highlight_element(self,locator: str | Locator):
            self._log_action("HIGHLIGHT", locator)
            self.page.evaluate(
                """
                element=>{
                    element.style.border='3px solid red';
                }
                """,
                self._get_locator(locator)
            )
    def press_key(self,key: str):
        self._log_action("KEYBOARD PRESS", value=key)
        self.page.keyboard.press(key)
    
    def type_text(self,text: str,delay: int = 30):
        self._log_action("KEYBOARD TYPE", value=text)
        self.page.keyboard.type(
            text,
            delay=delay
        )
    def select_all(self):
        self._log_action("SELECT ALL")
        self.page.keyboard.press("Control+A")
    
    def accept_dialog(self):

        self._log_action("ACCEPT DIALOG")

        self._log_action("ACCEPT PROMPT")

        self.page.once(
            lambda dialog: dialog.accept()
        )
    
    def dismiss_dialog(self):

        self._log_action("DISMISS DIALOG")

        self.page.once(
            "dialog",
            lambda dialog: dialog.dismiss()
        )
    
    def accept_prompt(
    self,
    text: str
    ):

        self.page.once(
            "dialog",
            lambda dialog: dialog.accept(text)
        )

    def expect_download(self):

        self._log_action("EXPECT DOWNLOAD")

        return self.page.expect_download()
    
    def expect_popup(self):

        self._log_action("EXPECT POPUP")

        return self.page.expect_popup()