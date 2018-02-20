from selenium import webdriver
import wget

with open('allit.html') as fp:
    browser = webdriver.Safari();
    nextURL = "http://www.allitebooks.com"
    browser.get(nextURL)
    
    main_content = browser.find_element_by_id('main-content')
    main_element_list = main_content.find_elements_by_tag_name('article')
        
    side_content = browser.find_element_by_id('side-content')
    side_element_list = side_content.find_elements_by_tag_name('li')


    for y in range(0,len(side_element_list)):
        for x in range(0, len(main_element_list)):
            browser.get(main_element_list[x].find_element_by_class_name('entry-thumbnail hover-thumb').find_element_by_css_selector('a').get_attribute('href'))
            elem = browser.find_elements_by_class_name("download-links")[0]
            print(elem.find_element_by_css_selector('a').get_attribute('href'))
            wget.download(elem.find_element_by_css_selector('a').get_attribute('href'))

            # Reset loop variables
            browser.get(nextURL)
            main_content = browser.find_element_by_id('main-content')
            main_element_list = main_content.find_elements_by_tag_name('article')
            
        side_content = browser.find_element_by_id('side-content')
        side_element_list = side_content.find_elements_by_tag_name('li')
        nextURL = side_element_list[y].find_element_by_css_selector('a').get_attribute('href')
        print(nextURL)
    
    
