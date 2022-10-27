from selenium.webdriver.support.ui import Select


select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("ALGERIA") # ищем элемент с текстом "ALGERIA"