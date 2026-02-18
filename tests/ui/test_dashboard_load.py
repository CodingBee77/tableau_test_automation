from pages.dashboard_page import DashboardPage


def test_dashboard_title(page):

    dashboard = DashboardPage(page)

    title = dashboard.get_title()

    assert "Sales Dashboard" in title
