from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("D:\\rui\\bit\\测试\\testPractice\\SeleniumPractice\\level_locate.html")
driver.get(file_path)
# driver.implicitly_wait(10)
WebDriverWait(driver, 5).until(lambda driver : driver.find_element_by_link_text('Link1'))

driver.find_element_by_link_text("Link1").click()
driver.implicitly_wait(10)

list = driver.find_element_by_id("dropdown1").find_elements_by_link_text("Action")
webdriver.ActionChains(driver).move_to_element(list[0]).perform()
time.sleep(5)

driver.quit()