
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.academis.eu")
    page.is_visible('#headline')
    html = page.inner_html('#headline')
    print(html[:190])
