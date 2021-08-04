from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("chromedriver_win32/chromedriver.exe")

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. ID 입력
elem = browser.find_element_by_id("id")
elem.send_keys("gildong")

# 4. PW 입력
elem = browser.find_element_by_id("pw")
elem.send_keys("******")

# 5. Enter
elem.send_keys(Keys.ENTER)
    
# 6. 입력 창 청소
browser.find_element_by_id("id").clear()

# 7. html 정보 출력
print(browser.page_source)

# 8. 브라우저 종료
# browser.close() # 탭 종료
browser.quit() # 크롬 종료
