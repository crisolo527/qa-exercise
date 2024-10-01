from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleFinancePage:
    URL = "https://www.google.com/finance"
    TITLE = "Google Finance - Stock Market Prices, Real-time Quotes & Business News"

    LOCATORS = {
        "stock_symbols": (By.XPATH, "//section[@aria-labelledby='smart-watchlist-title']//li//div[@class='COaKTb']")
    }

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        return self.TITLE in self.driver.title

    def get_stock_symbols(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.LOCATORS["stock_symbols"])
        )
        elements = self.driver.find_elements(*self.LOCATORS["stock_symbols"])
        return [element.text for element in elements]
