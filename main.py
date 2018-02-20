from bs4 import BeautifulSoup
from selenium import webdriver

with open('allit.html') as fp:
    soup = BeautifulSoup(fp, 'lxml')

    browser = webdriver.Safari();

    browser.get("http://allitebooks.com/illustrated-c-7-5th-edition")

    print(browser.find_elements_by_class_name('download-links'))


    browser.find_elements_by_class_name("download-links")[1].click()
    
