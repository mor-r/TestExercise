from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")

driver.find_element_by_link_text("hao123").click()
driver.implicitly_wait(10)
t = driver.title
print(t)

url=driver.current_url
print(url)


time.sleep(6)
driver.quit()