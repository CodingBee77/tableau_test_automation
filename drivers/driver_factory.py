from playwright.sync_api import sync_playwright


class DriverFactory:
    def __init__(self, browser="chromium"):
        self.browser_name = browser

    def launch(self):

        self.playwright = sync_playwright().start()

        if self.browser_name == "chromium":
            self.browser = self.playwright.chromium.launch(headless=False)

        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        return self.page

    def close(self):
        self.browser.close()
        self.playwright.stop()
