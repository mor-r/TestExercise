from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)
# 无法找到
# driver.find_element_by_tag_name("input").send_keys("张艺兴")
time.sleep(6)
driver.quit()