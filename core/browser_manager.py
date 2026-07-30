from playwright.sync_api import sync_playwright

from config.config_manager import config


class BrowserManager:

    def __init__(self):

        self.playwright = None
        self.browser = None

    def launch_browser(self):

        self.playwright = sync_playwright().start()

        browser_name = config.browser.lower()

        match browser_name:

            case "chromium":
                print("Chromium option matched")
                print("***** INSIDE DOCKER *****")
                print("=" * 60)
                print("Running inside BrowserManager")
                print("config.headless :", config.headless, type(config.headless))
                print("config.browser  :", config.browser)
                print("config.base_url :", config.base_url)
                print("=" * 60)
                self.browser = self.playwright.chromium.launch(
                    headless=config.headless,
                    slow_mo=config.slow_mo
                )

            case "firefox":
                self.browser = self.playwright.firefox.launch(
                    headless=config.headless,
                    slow_mo=config.slow_mo
                )

            case "webkit":
                self.browser = self.playwright.webkit.launch(
                    headless=config.headless,
                    slow_mo=config.slow_mo
                )

            case _:
                raise ValueError(
                    f"Unsupported browser: {browser_name}"
                )

        return self.browser

    def close_browser(self):

        if self.browser:
            print("close browser")
            self.browser.close()

        if self.playwright:
            print("close close playwright")
            self.playwright.stop()