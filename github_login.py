from  selenium import webdriver
import time
driver = webdriver.Chrome()
url = "https://github.com/login"
driver.get(url)
#获取元素
user = driver.find_element_by_id('login_field')
password = driver.find_element_by_id('password')
submit = driver.find_element_by_name('commit')

#操作
user.send_keys('OkamiMin')
password.send_keys('liang2531wen')
submit.click()
#等待
time.sleep(3)
driver.save_screenshot('github.png')
print(driver.page_source)
driver.close()