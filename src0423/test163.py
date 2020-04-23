from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://mail.163.com/")
# driver.find_element_by_id("switchAccountLogin").submit()
# driver.implicitly_wait(10)
# driver.find_element_by_id("auto-id-1587625326332").send_keys("heruichn@163.com")
# time.sleep(5)
# driver.find_element_by_id("auto-id-1587625326335").send_keys("zyx")
# time.sleep(5)
# driver.find_element_by_id("dologin").submit()
time.sleep(5)
driver.quit()
