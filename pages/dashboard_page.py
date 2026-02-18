from pages.base_page import BasePage


class DashboardPage(BasePage):

    def wait_until_loaded(self):
        self.page.wait_for_selector(".tab-dashboard")

    def get_title(self):
        return self.get_text(".dashboard-title")

    def apply_filter(self, filter_name, value):
        self.page.click(f"text={filter_name}")
        self.page.click(f"text={value}")
