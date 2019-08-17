from time import sleep
from selenium.webdriver.remote.webdriver import WebElement
from selenium import webdriver
dirver=webdriver.Firefox
dirver.get("G:\javaWeb_travel\travel\src\main\webapp\index.html")
length=len(dirver.find_elements_by_link_text("a"))
for i in range(0,length):
    links=dirver.find_elements_by_link_text("a")
    link=links[i]
    if not ("_blank" in link.get_attribute("target" or "http" in links.append("href"))):
        link.click()
        dirver.back()
