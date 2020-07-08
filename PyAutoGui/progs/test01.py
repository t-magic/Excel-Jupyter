import pyautogui
import time
from selenium import webdriver

'''
browser.get('https://automatetheboringstuff.com')
#elm = browser.find_element_by_css_selector('.entry-content > ol:nth-child(15) > li:nth-child(1) > a:nth-child(1)')
elm = browser.find_element_by_css_selector('.entry-content')
elm.test
elm.click()
browser.quit()
'''

# P283 boring book
browser = webdriver.Firefox()
print(type(browser))
browser.get('http://inventwithpython.com/')

'''
try:
    elm = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
# browser.quit()
'''

linkElem = browser.find_element_by_link_text("See what's new in the second edition.")
print(type(linkElem))
linkElem.click()







