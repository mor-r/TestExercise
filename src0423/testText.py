from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(3)

# text——获取元素的文本信息
data = driver.find_element_by_name("tj_trnews").text
print(data)

time.sleep(6)
driver.quit()