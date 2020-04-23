from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)
# 和id一样，也可以唯一定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys("张艺兴")
driver.find_element_by_xpath("//*[@id='su']").click()

time.sleep(6)
driver.quit()