from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)
# 部分内容
driver.find_element_by_partial_link_text("肺炎").click()

time.sleep(6)
driver.quit()