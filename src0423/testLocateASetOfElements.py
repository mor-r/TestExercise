from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("D:\\rui\\bit\\测试\\testPractice\\SeleniumPractice\\checkbox.html")
driver.get(file_path)
inputs = driver.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute('type') == "checkbox":
        input.click()
time.sleep(5)
driver.quit()