from selenium import webdriver

path = "/home/tejas/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=path)
# url = "https://demoqa.com/webtables"
driver.get("https://demoqa.com/webtables")
driver.maximize_window()

webtable = driver.find_element_by_xpath("//div[contains(@class,'ReactTable')]")
table_rows_data = webtable.find_elements_by_xpath(".//div[contains(@class,'rt-td') and text()]/ancestor::div[contains("
                                               "@class,'rt-tr-group')]")

print("Table Data is: ")
for i in range(0, len(table_rows_data)):
    table_column_data = table_rows_data[i].find_elements_by_xpath(".//div[@class='rt-td'][text()]")
    for j in range(0, len(table_column_data)):
        print(table_column_data[j].text)
driver.quit()

