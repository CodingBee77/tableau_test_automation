from pages.login_page import LoginPage


def test_public_tableau_landing_page_loads(page, base_url):
    """
    Basic smoke check that a public Tableau landing page is reachable.
    Does not require authentication.
    """
    login_page = LoginPage(page)

    login_page.navigate(base_url)
    login_page.wait_for_load_state("networkidle")

    # Very light assertion: page title should contain 'Tableau'
    assert "tableau" in page.title().lower()
