from playwright.sync_api import sync_playwright

def test_dashboard_load_time():
    """Test dashboard load time using Playwright"""
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Navigate to Tableau Share Link
        page.goto("https://your-tableau-server.com/views/Sales/Regional")
        
        # Wait for the 'bootstrap' of the VizQL engine
        # In Tableau, look for the 'glass-pane' or the canvas element
        viz_canvas = page.wait_for_selector(".tabCanvas", timeout=30000)
        
        assert viz_canvas.is_visible()
        print("Dashboard loaded successfully.")
        browser.close()
