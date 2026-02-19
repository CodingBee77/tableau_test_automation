from pages.dashboard_page import DashboardPage


def test_dashboard_title_contains_sales(page, base_url):
    """
    Example check against a public dashboard.
    Assumes base_url points directly to a Sales Dashboard view.
    """
    dashboard = DashboardPage(page)

    dashboard.navigate(base_url)
    dashboard.wait_for_load_state("networkidle")

    title = dashboard.get_title()

    assert "Sales Dashboard" in title
