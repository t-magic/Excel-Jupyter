import pyautogui
import time
from selenium import webdriver

# boring stuff book
browser = webdriver.Firefox()
#print(type(browser))
browser.get('http://gmai.com')
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('not_my_real_email@gmail.com')

# これを実行すると、詐欺の電話番号に電話させるメッセージがでる。
# その場合はリブートする。
#passwordElem = browser.find_element_by_id('Passwd')
#passwordElem.send_keys('12345')
#passwordElem.submit()
