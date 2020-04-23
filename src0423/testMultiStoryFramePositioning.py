from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///'+os.path.abspath("D:\\rui\\bit\\测试\\testPractice\\SeleniumPractice\\frame.html")
driver.get(file_path)

# 如果是多层框架结构，必须先进入f1,再进入f2（直接进入f2是不可以的）
# driver.switch_to_frame("f1")
# driver.switch_to_frame("f2")

# 上面两个方法被新的方法替代了，推荐使用新方法
driver.switch_to.frame("f1")
driver.switch_to.frame("f2")
driver.find_element_by_id("kw").send_keys("张艺兴")
driver.find_element_by_id("su").click()
time.sleep(5)

# driver.switch_to_default_content()
# driver.find_element_by_xpath("/html/body/div/div/a").click()
# time.sleep(5)

driver.quit()