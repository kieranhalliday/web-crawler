from bs4 import BeautifulSoup
from selenium import webdriver
import wget

with open('allit.html') as fp:
    browser = webdriver.Safari();
    browser.get("http://allitebooks.com/illustrated-c-7-5th-edition")

    elem = browser.find_elements_by_class_name("download-links")[0]
    wget.download(elem.find_element_by_css_selector('a').get_attribute('href'))

    
    
