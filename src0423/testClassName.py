from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)
# driver.find_element_by_class_name("s_ipt").send_keys("张艺兴")
# driver.find_element_by_class_name("bg s_btn").click()
# time.sleep(6)
driver.quit()