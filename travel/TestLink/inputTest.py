#导包
from time import sleep
from selenium import webdriver
#创建浏览器对象
driver=webdriver.Firefox
#获取项目的链接
url="G:\javaWeb_travel\travel\src\main\webapp\login.html"
driver.get(url)
#使用CSS定义id
driver.find_element_by_css_selector("#user").send_keys("admin")
driver.find_element_by_css_selector("password").send_keys("123456")
driver.find_element_by_css_selector(".tel").send_keys("132645646655")
driver.find_element_by_css_selector("email").send_keys("1018487750@qq.com")
driver.find_element_by_css_selector("name").send_keys("张三")
driver.find_element_by_css_selector("gender").send_keys("男")

sleep(3)
#关闭浏览器d
driver.quit()