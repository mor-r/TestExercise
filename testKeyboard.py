from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
# driver.get("http://127.0.0.1:8088/biz/user-login-L2Jpei8=.html")
# driver.implicitly_wait(10)

# driver.find_element_by_id("account").send_keys("admin")
# 只能用 “键盘快捷键” 这种方式跳转到密码框，并不能在此基础之上继续输入密码
# driver.find_element_by_id("account").send_keys(Keys.TAB)
# driver.find_element_by_name("password").send_keys("")
# driver.find_element_by_name("password").send_keys(Keys.ENTER)
# time.sleep(10)

driver.quit()