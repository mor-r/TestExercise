from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)
driver.find_element_by_id("kw").send_keys("张艺兴")
driver.find_element_by_id("su").click()
time.sleep(5)

# 将滚动条滑到最底端
js = "var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(5)

# 将滚动条滑到最顶端
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(5)

driver.quit()