from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe",options=options)
browser.maximize_window()

# 페이지 이동
url = "https://recruit.navercorp.com/naver/job/list/developer?searchSysComCd=&entTypeCd=001&searchTxt="
browser.get(url)

browser.get_screenshot_as_file("naver_recruit.png")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

recruits = soup.find_all("span", attrs={"class":"list_con"})

print("\n\nnaver career recruit 신입/개발 직군")
print("링크 : ", url)
print("\n")
for recruit in recruits:
    print("-" * 100)
    print(recruit.strong.get_text())
    print(recruit.em.get_text())

    # print(f"제목 : {title}")
    # print(f"할인 전 금액 : {original_price}")
    # print(f"할인 후 금액 : {price}")
    # print("링크 : ", "https://play.google.com" + link)
    print()


browser.quit()
