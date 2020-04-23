from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")

driver.maximize_window()
time.sleep(5)

driver.set_window_size(400,800)

time.sleep(5)
driver.quit()