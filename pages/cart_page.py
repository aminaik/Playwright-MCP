from playwright.sync_api import Locator, Page


class CartPage:
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.checkout_button = page.locator('[data-test="checkout"]')

    def item(self, name: str) -> Locator:
        return self.page.get_by_text(name, exact=True)

    def start_checkout(self) -> None:
        self.checkout_button.click()
