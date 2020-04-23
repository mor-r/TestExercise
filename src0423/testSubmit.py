from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)

# submit() 和 click() 作用相同
driver.find_element_by_id("kw").send_keys("我是唱作人2")
driver.find_element_by_id("su").submit()

time.sleep(6)
driver.quit()