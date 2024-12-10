from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup_driver():

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


class TestInvalidLogin:

    def test_login_invalid_password(self, setup_driver):
        driver = setup_driver
        username = "standard_user"
        password = "wrong_password"

        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        # Assert error message
        error_message = driver.find_element(By.CSS_SELECTOR, ".error-message-container").text
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        assert error_message == expected_message, f"Unexpected error message: {error_message}"
