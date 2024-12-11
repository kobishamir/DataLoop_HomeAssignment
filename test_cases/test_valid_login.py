import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils import login

@pytest.fixture(scope="class")
def setup_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

class TestLoginUsers:


    def test_login_standard_user(self, setup_driver):
        driver = setup_driver
        username = "standard_user"
        password = "secret_sauce"

        login(driver, username, password)

        assert "inventory.html" in driver.current_url, "Standard user login failed."

    def test_login_locked_out_user(self, setup_driver):
        driver = setup_driver
        username = "locked_out_user"
        password = "secret_sauce"

        login(driver, username, password)

        error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Sorry, this user has been locked out." in error_message, "Locked-out user error message is incorrect."

    def test_login_problem_user(self, setup_driver):
        driver = setup_driver
        username = "problem_user"
        password = "secret_sauce"

        login(driver, username, password)

        assert "inventory.html" in driver.current_url, "Problem user login failed."

    def test_login_performance_glitch_user(self, setup_driver):
        driver = setup_driver
        username = "performance_glitch_user"
        password = "secret_sauce"

        login(driver, username, password)

        assert "inventory.html" in driver.current_url, "Performance glitch user login failed."
