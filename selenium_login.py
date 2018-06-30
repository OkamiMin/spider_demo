from  selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.sxt.cn/index/login/login')

user = driver.find_element_by_name('user')
password = driver.find_element_by_name('password')
submit = driver.find_element_by_id('submitD')

user.send_keys('18895689552')
password.send_keys('liang2531wen')
submit.click()

time.sleep(3)
driver.save_screenshot('sxt.png')
print(driver.page_source)
driver.close()