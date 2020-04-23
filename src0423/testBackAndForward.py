from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")

driver.find_element_by_link_text("hao123").click()
time.sleep(5)

driver.back()
time.sleep(5)

driver.forward()
time.sleep(5)

t = driver.title
print(t)

url = driver.current_url
print(url)


time.sleep(6)
driver.quit()