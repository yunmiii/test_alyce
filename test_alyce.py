from selenium import webdriver

try:
	browser = webdriver.Chrome()
	browser.get('http://hrtest.alycedev.com/')

	button = browser.find_element_by_class_name('btn').click()
	button1 = browser.find_element_by_xpath('//li[2]/div[1]/span/button').click()

finally:
    time.sleep(30)
    browser.quit()
