from playwright.sync_api import sync_playwright

def test_nadpis_example_com():
    with sync_playwright() as p:
        # Spustí Chrome (headless=False = uvidíš okno)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Otvor stránku
        page.goto("https://example.com")
        
        # Skontroluj nadpis
        assert page.title() == "Example Domain"
        
        # Zatvor prehliadač
        browser.close()
