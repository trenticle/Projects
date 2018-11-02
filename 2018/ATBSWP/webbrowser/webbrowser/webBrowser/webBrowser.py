from selenium import webdriver
browser = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')
elems = browser.find_element_by_css_selector('.search-field')
searchElem = browser.find_element_by_css_selector('.gLFyf')
searchElem.send_keys('your keys?')
searchElem.submit()
