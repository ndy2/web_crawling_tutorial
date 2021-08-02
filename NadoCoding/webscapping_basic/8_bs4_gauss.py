import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

#네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("td",attrs={"class" : "title"})

#class 속성이 title인 모든 "a" element 반환
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com"+ cartoon.a["href"]
    rating = " "+cartoon.find_next_sibling("td").div.find("strong").get_text()
    print(title + link +rating)