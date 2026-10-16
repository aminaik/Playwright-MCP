from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutInfoPage, CheckoutOverviewPage
from pages.checkout_page import CheckoutCompletePage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_standard_user_completes_backpack_checkout(
    page: Page,
    checkout_data: dict,
    login_page: LoginPage,
    inventory_page: InventoryPage,
    cart_page: CartPage,
    checkout_info_page: CheckoutInfoPage,
    checkout_overview_page: CheckoutOverviewPage,
    checkout_complete_page: CheckoutCompletePage,
) -> None:
    user = checkout_data["user"]
    product = checkout_data["product"]
    customer = checkout_data["customer"]
    expected = checkout_data["expected"]

    login_page.open()
    expect(page).to_have_title("Swag Labs")
    expect(login_page.login_form).to_be_visible()

    login_page.login(user["username"], user["password"])
    expect(page).to_have_url(InventoryPage.URL)
    expect(inventory_page.title).to_be_visible()

    inventory_page.add_to_cart(product["slug"])
    expect(inventory_page.remove_button(product["slug"])).to_be_visible()
    expect(inventory_page.cart_badge).to_have_text("1")

    inventory_page.open_cart()
    expect(page).to_have_url(CartPage.URL)
    expect(cart_page.item(product["name"])).to_be_visible()

    cart_page.start_checkout()
    expect(page).to_have_url(CheckoutInfoPage.URL)
    expect(checkout_info_page.title).to_be_visible()

    checkout_info_page.fill_details(
        customer["first_name"], customer["last_name"], customer["postal_code"]
    )
    checkout_info_page.continue_to_overview()
    expect(page).to_have_url(CheckoutOverviewPage.URL)
    expect(checkout_overview_page.item(product["name"])).to_be_visible()
    expect(checkout_overview_page.total(expected["total"])).to_be_visible()

    checkout_overview_page.finish()
    expect(page).to_have_url(CheckoutCompletePage.URL)
    expect(checkout_complete_page.heading).to_be_visible()
    expect(checkout_complete_page.message(expected["confirmation"])).to_be_visible()
    expect(checkout_complete_page.cart_badge).to_have_count(0)
