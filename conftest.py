import json
from pathlib import Path

import pytest

from pages.cart_page import CartPage
from pages.checkout_page import (
    CheckoutCompletePage,
    CheckoutInfoPage,
    CheckoutOverviewPage,
)
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture
def checkout_data() -> dict:
    return json.loads((DATA_DIR / "checkout_data.json").read_text())


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_info_page(page):
    return CheckoutInfoPage(page)


@pytest.fixture
def checkout_overview_page(page):
    return CheckoutOverviewPage(page)


@pytest.fixture
def checkout_complete_page(page):
    return CheckoutCompletePage(page)
