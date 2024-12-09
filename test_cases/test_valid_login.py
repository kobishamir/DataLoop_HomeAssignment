import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginUsers:
    driver = None

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self):
        TestLoginUsers.driver = webdriver.Chrome()  # Initialize the WebDriver
        TestLoginUsers.driver.implicitly_wait(10)
        TestLoginUsers.driver.get("https://www.saucedemo.com/")
        yield
        TestLoginUsers.driver.quit()

    def test_login_standard_user(self):
        username = "standard_user"
        password = "secret_sauce"

        self._login(username, password)

        # Assert successful login
        assert "inventory.html" in self.driver.current_url, "Standard user login failed."

    def test_login_locked_out_user(self):
        username = "locked_out_user"
        password = "secret_sauce"

        self._login(username, password)

        # Assert error message
        error_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Sorry, this user has been locked out." in error_message, "Locked-out user error message is incorrect."

    def test_login_problem_user(self):
        username = "problem_user"
        password = "secret_sauce"

        self._login(username, password)

        # Assert successful login
        assert "inventory.html" in self.driver.current_url, "Problem user login failed."

    def test_login_performance_glitch_user(self):
        username = "performance_glitch_user"
        password = "secret_sauce"

        self._login(username, password)

        # Assert successful login
        assert "inventory.html" in self.driver.current_url, "Performance glitch user login failed."

    def _login(self, username, password):
        """Helper method to perform login."""
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()