# SauceDemo Automation Test Suite

## Project Overview
This project contains an automated testing suite for the SauceDemo web application, focusing on key functionalities such as user login, product sorting, and application state management.

## Test Scenarios Covered
- User Login (Valid and Invalid Credentials)
- Product Sorting (by Price and Name)
- Application State Reset

## Prerequisites
Before running the tests, ensure you have the following installed:
- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/kobishamir/DataLoop_HomeAssignment.git
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running Tests

### Execute All Tests
```bash
pytest test_cases/
```

### Run Specific Test Modules
```bash
# Run login tests
pytest test_cases/test_valid_login.py
pytest test_cases/test_invalid_login.py

# Run sorting tests
pytest test_cases/test_sorting.py

# Run app state reset test
pytest test_cases/test_reset_app_state.py
```

### Run a Specific Test (for example)
```bash
# Run a single test from a test file
pytest test_cases/test_valid_login.py::test_login_standard_user
```

## Project Structure
```
.
├── utils.py                # Reusable helper functions
├── test_cases/
│   ├── test_valid_login.py
│   ├── test_invalid_login.py
│   ├── test_sorting.py
│   └── test_reset_app_state.py
├── README.md
├── TestPlan.md
└── requirements.txt
```

## Test Environment Details
- **Application**: SauceDemo (https://www.saucedemo.com)
- **Browser**: Google Chrome
- **Automation Tool**: Selenium with Python
- **Test Framework**: Pytest
