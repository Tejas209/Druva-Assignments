import pytest
from selenium import webdriver

"""fixture to invoke browser"""
@pytest.fixture(scope="class")
def setup(request):
    path = "/home/tejas/Downloads/chromedriver_linux64/chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()