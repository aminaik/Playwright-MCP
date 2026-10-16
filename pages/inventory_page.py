from playwright.sync_api import Locator, Page


class InventoryPage:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.get_by_text("Products", exact=True)
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link = page.locator('[data-test="shopping-cart-link"]')

    def add_button(self, slug: str) -> Locator:
        return self.page.locator(f'[data-test="add-to-cart-{slug}"]')

    def remove_button(self, slug: str) -> Locator:
        return self.page.locator(f'[data-test="remove-{slug}"]')

    def add_to_cart(self, slug: str) -> None:
        self.add_button(slug).click()

    def open_cart(self) -> None:
        self.cart_link.click()
