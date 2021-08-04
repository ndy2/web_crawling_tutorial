from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys



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

    soup = BeautifulSoup(browser.page_source, "lxml")
    login = soup.find("div", attrs={"class" : "user_id tar"})
    pw = soup.find("div", attrs={"class" : "user_pw tar"})

    browser.find_element_by_tag_name("div", attrs={"class" : "user_id tar"}).send_keys
    

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("window-size=1920x1080")

    browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe",options=options)
    browser.maximize_window()

    # NAVER(browser)
    SKKU(browser)
    browser.quit()
