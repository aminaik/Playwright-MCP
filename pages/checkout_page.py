from playwright.sync_api import Locator, Page


class CheckoutInfoPage:
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.title = page.get_by_text("Checkout: Your Information", exact=True)
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')

    def fill_details(self, first: str, last: str, postal: str) -> None:
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)

    def continue_to_overview(self) -> None:
        self.continue_button.click()


class CheckoutOverviewPage:
    URL = "https://www.saucedemo.com/checkout-step-two.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.finish_button = page.locator('[data-test="finish"]')

    def item(self, name: str) -> Locator:
        return self.page.get_by_text(name, exact=True)

    def total(self, text: str) -> Locator:
        return self.page.get_by_text(text, exact=True)

    def finish(self) -> None:
        self.finish_button.click()


class CheckoutCompletePage:
    URL = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.get_by_role("heading", name="Thank you for your order!")
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def message(self, text: str) -> Locator:
        return self.page.get_by_text(text, exact=True)
