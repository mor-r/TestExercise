from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")

driver.find_element_by_id("kw").send_keys("张艺兴")
driver.find_element_by_id("su").submit()
# time.sleep(10)
driver.implicitly_wait(10)
driver.find_element_by_link_text("张艺兴_百度百科").click()

time.sleep(6)
driver.quit()