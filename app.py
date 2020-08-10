from selenium import webdriver
import time

browser = webdriver.Chrome()
url = "http://google.com"

browser.get(url)
time.sleep(2)
search_el = browser.find_element_by_name("q")
search_el.send_keys("fairo.pk")