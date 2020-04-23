from selenium import webdriver
import time
# 引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("张艺兴")
su = driver.find_element_by_id("su")
# context_click()——右击
# ActionChains(driver).context_click(su).perform()

# double_click()——双击
ActionChains(driver).double_click(su).perform()

# drag_and_drop(a,b)——拖拽

# move_to_element()——移动

time.sleep(6)
driver.quit()