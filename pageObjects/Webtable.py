from selenium.webdriver.common.by import By
from selenium import webdriver


class Webtable:
    def __init__(self, driver):
        self.driver = driver

    webtable = (By.XPATH, "//div[contains(@class,'ReactTable')]")
    table_rows_data = (By.XPATH, ".//div[contains(@class,'rt-td') and text()]/ancestor::div[contains("
                                 "@class,'rt-tr-group')]")
    table_column_data = (By.XPATH, ".//div[@class='rt-td'][text()]")

    def table(self):
        return self.driver.find_element(*Webtable.webtable)

    def rows_data(self):
        return self.driver.find_elements(*Webtable.table_rows_data)

    def column_data(self):
        return self.driver.find_elements(*Webtable.column_data())
