from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from utils import get_prices, get_names


@pytest.fixture(scope="class")
def setup_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield driver
    driver.quit()


class TestSorting:

    def test_sort_by_price_low_to_high(self, setup_driver):
        driver = setup_driver
        sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("lohi")
        prices = get_prices(driver)
        assert prices == sorted(prices), f"Items not sorted by price (Low to High): {prices}"

    def test_sort_by_price_high_to_low(self, setup_driver):
        driver = setup_driver
        sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("hilo")
        prices = get_prices(driver)
        assert prices == sorted(prices, reverse=True), f"Items not sorted by price (High to Low): {prices}"

    def test_sort_by_name_a_to_z(self, setup_driver):
        driver = setup_driver
        sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("az")
        names = get_names(driver)
        assert names == sorted(names), f"Items not sorted by name (A to Z): {names}"

    def test_sort_by_name_z_to_a(self, setup_driver):
        driver = setup_driver
        sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        sort_dropdown.select_by_value("za")
        names = get_names(driver)
        assert names == sorted(names, reverse=True), f"Items not sorted by name (Z to A): {names}"
