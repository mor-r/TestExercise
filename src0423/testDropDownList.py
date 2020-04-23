from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("D:\\rui\\bit\\测试\\testPractice\\SeleniumPractice\\drop_down.html")
driver.get(file_path)
ship = driver.find_element_by_id("ShippingMethod")
ship.find_element_by_xpath("//*[@id='ShippingMethod']").click()
time.sleep(5)
driver.quit()
