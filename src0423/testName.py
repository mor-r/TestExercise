from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)
driver.find_element_by_name("wd").send_keys("张艺兴")
driver.find_element_by_id("su").click()
time.sleep(6)
driver.quit()