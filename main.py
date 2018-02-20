from selenium import webdriver
import wget

with open('allit.html') as fp:
    browser = webdriver.Safari();

    browser.get("http://www.allitebooks.com")
    main_content = browser.find_element_by_id('main-content')
    element_list = main_content.find_elements_by_tag_name('article')


    for x in range(0, len(element_list)):
        browser.get(element_list[x].find_element_by_class_name('entry-thumbnail hover-thumb').find_element_by_css_selector('a').get_attribute('href'))
        elem = browser.find_elements_by_class_name("download-links")[0]
        print(elem.find_element_by_css_selector('a').get_attribute('href'))
        wget.download(elem.find_element_by_css_selector('a').get_attribute('href'))
        browser.get("http://www.allitebooks.com")
        main_content = browser.find_element_by_id('main-content')
        element_list = main_content.find_elements_by_tag_name('article')

    #How to get a single books from a pre-known webpage
    #browser.get("http://allitebooks.com/illustrated-c-7-5th-edition")

    #elem = browser.find_elements_by_class_name("download-links")[0]
    #wget.download(elem.find_element_by_css_selector('a').get_attribute('href'))

    
    
