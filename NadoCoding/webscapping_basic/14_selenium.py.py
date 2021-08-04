from selenium import webdriver

browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.back()
browser.forward()
browser.refresh()
browser.back()

elem = browser.find_element_by_id("query")

from selenium.webdriver.common.keys import Keys

elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

elem = browser.find_elements_by_tag_name("a")

for e in elem:
    e.get_attribute("href")

browser.get("http://daum.net")
elem = browser.find_element_by_name("q")

elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
browser.back()

elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')
elem.click()

browser.close()
browser.quit()