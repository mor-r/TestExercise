from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)
# id、name等都属于css selector，但注意前面要加特定元素，如 #
driver.find_element_by_css_selector("#kw").send_keys("张艺兴")
driver.find_element_by_css_selector("#su").click()

time.sleep(6)
driver.quit()