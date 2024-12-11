import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils import login, add_items_to_cart, reset_app_state

@pytest.fixture(scope="class")
def setup_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


class TestResetAppState:

    def test_reset_app_state(self, setup_driver):
        driver = setup_driver
        username = "standard_user"
        password = "secret_sauce"

        login(driver, username, password)

        # Add items to the cart
        number_of_items = 2
        add_items_to_cart(driver, num_items=number_of_items)

        # Verify items are in the cart
        cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_badge == str(number_of_items), f"Expected 2 items in the cart, but found {cart_badge}"

        # Reset app state
        reset_app_state(driver)

        # Verify cart is empty
        cart_badge_elements = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(cart_badge_elements) == 0, "Cart is not empty after resetting app state"