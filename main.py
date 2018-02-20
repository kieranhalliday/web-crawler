from selenium import webdriver
import wget
import re

with open('allit.html') as fp:
    browser = webdriver.Safari();
    nextURL = "http://www.allitebooks.com/web-development/"
    browser.get(nextURL)
    
    main_content = browser.find_element_by_id('main-content')
    main_element_list = main_content.find_elements_by_tag_name('article')
        
    side_content = browser.find_element_by_id('side-content')
    side_element_list = side_content.find_elements_by_tag_name('li')


    for z in range(0,len(side_element_list)):
        pageList = browser.find_element_by_class_name('pagination clearfix')
        print (pageList.text)
        numberOfPages = re.findall(r'\d{2,3}',pageList.text)
        print numberOfPages[0]
        for y in range (2,int(numberOfPages[0])):
            for x in range(0, len(main_element_list)):
                # Get books from current page
                browser.get(main_element_list[x].find_element_by_class_name('entry-thumbnail hover-thumb').find_element_by_css_selector('a').get_attribute('href'))
                elem = browser.find_elements_by_class_name("download-links")[0]
                print(elem.find_element_by_css_selector('a').get_attribute('href'))
                wget.download(elem.find_element_by_css_selector('a').get_attribute('href'))

                # Reset loop variables
                browser.get(nextURL)
                main_content = browser.find_element_by_id('main-content')
                main_element_list = main_content.find_elements_by_tag_name('article')

            nextURL = nextURL.rstrip('page/' + str(y-1) + '/')
            nextURL = nextURL + "/page/" + str(y) + "/"
            print(nextURL)
        # Go to next sidebar
        side_content = browser.find_element_by_id('side-content')
        side_element_list = side_content.find_elements_by_tag_name('li')
        nextURL = side_element_list[z].find_element_by_css_selector('a').get_attribute('href')
        browser.get(nextURL)
        print(nextURL)
    
    
