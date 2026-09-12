from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto("file:///tmp/proto-render/index.html")
    time.sleep(0.3)
    # Screenshot 1: login screen
    page.screenshot(path="/tmp/proto-render/tela-login.png")

    # Log in as admin
    page.select_option("#role", "admin")
    page.click("#loginForm button")
    time.sleep(0.3)
    # Screenshot 2: admin dashboard
    page.screenshot(path="/tmp/proto-render/tela-dashboard-admin.png")

    # Navigate to Usuarios page
    page.click("button.nav[data-p='users']")
    time.sleep(0.3)
    page.screenshot(path="/tmp/proto-render/tela-usuarios.png")

    browser.close()
print("done")
