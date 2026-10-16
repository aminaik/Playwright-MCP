from playwright.sync_api import Page


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_form = page.get_by_role("form", name="Login")
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')

    def open(self) -> None:
        self.page.goto(self.URL)

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
