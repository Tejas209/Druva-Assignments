from selenium import webdriver
from pageObjects.Webtable import Webtable

path = "/home/tejas/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()


def test_webtable_data(self):
    web_table = Webtable(self.driver)
    tab = web_table.table()
    webtable = driver.find_element_by_xpath("//div[contains(@class,'ReactTable')]")


