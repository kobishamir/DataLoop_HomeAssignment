from selenium.webdriver.common.by import By

def get_prices(driver):
    """Fetches the prices of items displayed on the page."""
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    return [float(price.text.replace("$", "")) for price in prices]

def get_names(driver):
    """Fetches the names of items displayed on the page."""
    names = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    return [name.text for name in names]

def login(driver, username, password):
    """Perform login."""
    driver.find_element(By.ID, "user-name").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def add_items_to_cart(driver, num_items=1):
    """Adds a specified number of items to the cart."""
    add_buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for button in add_buttons[:num_items]:
        button.click()

def reset_app_state(driver):
    """Resets the app state via the sidebar menu."""
    driver.find_element(By.ID, "react-burger-menu-btn").click()  # Open the sidebar menu
    driver.find_element(By.ID, "reset_sidebar_link").click()  # Click reset app state
    driver.find_element(By.ID, "react-burger-cross-btn").click()  # Close the sidebar menu
