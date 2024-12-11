<!-- TOC -->
* [SauceDemo Automation Test Plan](#saucedemo-automation-test-plan)
* [Objective](#objective)
* [Scope](#scope)
* [Test Environment](#test-environment)
* [Test Scenarios](#test-scenarios)
  * [1. Login Tests](#1-login-tests)
    * [1.1 Valid Login](#11-valid-login)
    * [1.2 Invalid Login](#12-invalid-login)
  * [2. Product Search Tests](#2-product-search-tests)
    * [2.1 Search for a Product](#21-search-for-a-product)
  * [3. Item Filtering Tests](#3-item-filtering-tests)
    * [3.1  Filter Items by Price (Low to High)](#31--filter-items-by-price-low-to-high)
  * [4. Reset App State](#4-reset-app-state)
* [Out of Scope](#out-of-scope)
* [Test Data](#test-data)
* [Assumptions](#assumptions)
<!-- TOC -->

---

# SauceDemo Automation Test Plan

Objective
=========

The purpose of this test plan is to outline the testing strategy, test scenarios, and expected outcomes for automating the testing of SauceDemo's core functionalities.


Scope
=====
This test plan focuses on the following key functionalities of SauceDemo:

1. User login (both valid and invalid credentials).
2. Searching for products on the product search page.
3. Filtering items based on predefined categories.
4. Resetting the application state.

Test Environment
================
Application Under Test (AUT): SauceDemo (https://www.saucedemo.com)

Browser: Google Chrome

Automation Tool: Selenium with Python.

Test Framework: Pytest.


Test Scenarios
==============

## 1. Login Tests

### 1.1 Valid Login
**Description**: Verify the user can log in with valid credentials and lands on the homepage.

**Steps**:

1. Navigate to the login page.
2. Enter valid username and password.
3. Click the "Login" button.
4. Verify that the user is redirected to the inventory page.

**Expected Result**: User lands on the inventory page (/inventory.html).


### 1.2 Invalid Login
**Description**: Verify the system displays an error message when logging in with an invalid password.

**Steps**:

1. Navigate to the login page.
2. Enter a valid username and an invalid password..
3. Click the "Login" button.
4. Verify that an error message appears.

**Expected Result**: Error message is displayed.

---
## 2. Item Sorting Tests

### 2.1  Sort Items by Price (Low to High)

**Description**: Verify that the Sort functionality arranges items correctly by price (Low to High).

**Steps**:
1. Log in with valid credentials.
2. Use the sort dropdown to select "Price (low to high)".
3. Verify the items are sorted by price in ascending order.

**Expected Result**: Items appear in ascending order of price.

### 2.2  Sort Items by Price (High to Low)

**Description**: Verify that the Sort functionality arranges items correctly by price (High to Low).

**Steps**:
1. Log in with valid credentials.
2. Use the sort dropdown to select "Price (high to low)".
3. Verify the items are sorted by price in descending order.

**Expected Result**: Items appear in descending order of price.

### 2.3  Sort Items by Name (A to Z)

**Description**: Verify that the Sort functionality arranges items correctly by Name (A to Z).

**Steps**:
1. Log in with valid credentials.
2. Use the sort dropdown to select "Name (A to Z)".
3. Verify the items are sorted by name in ascending order.

**Expected Result**: Items appear in ascending order of name.

### 2.4  Sort Items by Name (Z to A)

**Description**: Verify that the Sort functionality arranges items correctly by Name (Z to A).

**Steps**:
1. Log in with valid credentials.
2. Use the sort dropdown to select "Name (Z to A)".
3. Verify the items are sorted by name in descending order.

**Expected Result**: Items appear in descending order of name.

---
## 3. Reset App State

**Description**: Verify that resetting the app state clears all changes made during the session.

**Steps**:

1. Log in with valid credentials.
2. Add an item to the cart.
3. Use the menu to reset the app state.
4. Verify that the cart is empty and any session-specific data is cleared.

**Expected Result**: The cart is cleared, and the state of the app is reset to the default.

---
## 4. User-Specific Behavior Tests

### 4.1 Verify Product Images for Users
**Description**: Check that the product images are displayed correctly for each user.  
**Steps**:
1. Log in with each user type (`standard_user`, `problem_user`, `locked_out_user`, etc.).
2. Navigate to the inventory page.
3. Verify that all product images are unique and displayed correctly.  
**Expected Result**: Product images should not repeat unless intended and should correspond to the correct products.


### 4.2 Verify Adding Items to Cart
**Description**: Check that users can add multiple items to the cart without issues.  
**Steps**:
1. Log in with each user type.  
2. Attempt to add multiple items (more than 3) to the cart.  
3. Verify that the cart updates correctly with the added items.  
**Expected Result**: The user should be able to add any number of items to the cart (within the expected functionality).


### 4.3 Verify Removing Items from Cart
**Description**: Ensure that users can remove items from the cart.  
**Steps**:
1. Log in with each user type.  
2. Add items to the cart.  
3. Attempt to remove items from the cart.  
**Expected Result**: The cart should update correctly and reflect the removed items.


### 4.4 Verify Checkout Functionality
**Description**: Ensure that all users can complete the checkout process without errors.  
**Steps**:
1. Log in with each user type.  
2. Add items to the cart.  
3. Proceed to the checkout page and attempt to complete all required fields.  
4. Verify that the checkout process completes successfully.  
**Expected Result**: Checkout should work without errors for all users.


### 4.5 Verify Button Placement
**Description**: Check that all buttons (e.g., "Add to Cart," "Remove," "Checkout") are displayed in consistent locations across user types.  
**Steps**:
1. Log in with each user type.  
2. Verify the placement and functionality of buttons on the inventory and cart pages.  
**Expected Result**: Buttons should be in the same location and perform the expected action for all users.


### 4.6 Verify Page Load Time
**Description**: Test the performance of the application for the `performance_glitch_user` account.  
**Steps**:
1. Log in with the `performance_glitch_user`.  
2. Measure the time it takes for pages (e.g., inventory, cart) to load.  
**Expected Result**: Page load time should be reasonable and consistent with other users.


### 4.7 Verify Visual Alignment and Layout
**Description**: Ensure that the layout and alignment of elements are consistent across user types.  
**Steps**:
1. Log in with each user type, including `visual_user`.  
2. Navigate through the application and verify that all elements (buttons, text fields, etc.) are aligned and accessible.  
**Expected Result**: The layout should remain consistent across all user accounts.

---
Out of Scope
============
Testing non-functional requirements such as performance or security.
Testing advanced user scenarios like bulk operations or extended session testing.

Test Data
=========

* Valid Credentials:
  * Username: `standard_user`
  * Password: `secret_sauce`
* Invalid Credentials:
  * Username: `standard_user`
  * Password: `wrong_password`

Assumptions
===========
* SauceDemo is available and functional throughout the testing process.
* Browser and Selenium WebDriver are properly configured.
* Tests are executed in a local environment.

Execution Plan
==============
* Write individual scripts for each scenario and validate them.
* Execute tests using Pytest.
* Record results and log any issues found.


Expected Deliverables
=====================
* Automated test scripts for the defined scenarios.
* README file with setup and execution instructions.
* Test results report generated by Pytest.
