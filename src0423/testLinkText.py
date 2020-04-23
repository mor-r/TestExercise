from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)

driver.find_element_by_link_text("抗击肺炎").click()

time.sleep(6)
driver.quit()