import sys
import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Add the project root directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.google_finance_page import GoogleFinancePage

@pytest.fixture
def driver():
    chrome_driver_path = ChromeDriverManager().install()
    service = webdriver.ChromeService(chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=old')
    driver = webdriver.Chrome(options=options, service=service)
    yield driver
    driver.quit()

@pytest.fixture
def finance_page(driver):
    return GoogleFinancePage(driver)

def test_load_google_finance_page(finance_page):
    # Parts 1 & 2 - Load the Google Finance page
    finance_page.load()
    assert finance_page.is_loaded(), "Google Finance page did not load correctly."

def test_get_stock_symbols(finance_page):
    # Part 3 - Load the Google Finance page and get stock symbols
    finance_page.load()
    assert finance_page.is_loaded(), "Google Finance page did not load correctly."

    stock_symbols = finance_page.get_stock_symbols()
    print(f"Stock symbols on the page:\n{stock_symbols}")
    assert stock_symbols, "No stock symbols found on the Google Finance page."

def test_print_symbols_not_in_test_data(finance_page):
    # Part 4 - Get stock symbols, and compare with test data
    test_data = ["NFLX", "MSFT", "TSLA"]
    finance_page.load()
    assert finance_page.is_loaded(), "Google Finance page did not load correctly."

    stock_symbols = finance_page.get_stock_symbols()

    # Part 5 - Print all stock symbols on the page that are not in the test data
    symbols_not_in_test_data = [symbol for symbol in stock_symbols if symbol not in test_data]
    print(f"Stock symbols on the page that are not in the test data symbols:\n{symbols_not_in_test_data}")

def test_print_test_data_not_in_symbols(finance_page):
    # Part 4 - Get stock symbols, and compare with test data
    test_data = ["NFLX", "MSFT", "TSLA"]
    finance_page.load()
    assert finance_page.is_loaded(), "Google Finance page did not load correctly."

    stock_symbols = finance_page.get_stock_symbols()

    # Part 6 - Print all stock symbols in the test data that are not on the page
    test_data_not_in_symbols = [symbol for symbol in test_data if symbol not in stock_symbols]
    print(f"Test data symbols that are not in the stock symbols on the page:\n{test_data_not_in_symbols}")
