class DashboardPage:

    def __init__(self, page):
        self.page = page

    def wait_until_loaded(self):
        self.page.wait_for_selector(".tab-dashboard")

    def apply_filter(self, filter_name, value):
        self.page.click(f"text={filter_name}")
        self.page.click(f"text={value}")

    def get_kpi_value(self):
        return self.page.locator(".mark-label").first.inner_text()