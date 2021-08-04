from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


## NAVER 
# 페이지 이동
def NAVER(browser) : 
    url = "https://recruit.navercorp.com/naver/job/list/developer?searchSysComCd=&entTypeCd=001&searchTxt="
    browser.get(url)

    soup = BeautifulSoup(browser.page_source, "lxml")
    recruits = soup.find_all("span", attrs={"class":"list_con"})

    print("\n\nnaver career recruit 신입/개발 직군")
    print("링크 : ", url)
    print("\n")
    for recruit in recruits:
        print("-" * 100)
        print(recruit.strong.get_text())
        print(recruit.em.get_text())
        print()


def SKKU(browser) : 
    url = "https://job.skku.edu/login.aspx?redir=/loginproc.aspx%3fredir2%3d%2fdefault.aspx%3f"
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="user_id"]').send_keys("ididididid")
    browser.find_element_by_xpath('//*[@id="user_pw"]').send_keys("******")
    browser.find_element_by_class_name("loginButton").click()
    browser.find_element_by_xpath('//*[@id="interestFrm"]/div[2]/button').click()

    time.sleep(1)
    elem = browser.find_element_by_xpath('//*[@id="interestJobList"]')
    # elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="interestJobList"]')))

    print(elem.text)


import time

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")
    options.add_argument("window-size=1920x1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36" )
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe",options=options)
    browser.maximize_window()
    
    NAVER(browser)
    time.sleep(1)
    SKKU(browser)
    browser.quit()
