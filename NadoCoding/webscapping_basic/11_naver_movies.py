import requests
from bs4 import BeautifulSoup
import time


for year in range(2018,2022) :
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
    print(year , "년 상위 5개 영화 순위")
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all("div", attrs= {"class" : "thumb"})

    name1  = images[1].img["alt"]
    link1 = images[1].img["src"]

    print(f"제목 : {name1}")
    print(f"이미지 링크 : {link1}")

    for idx, image in enumerate(images):
        if idx>4 :
            break
        name = image.img["alt"]
        link = image.img["src"]
        print(f"제목 : {name}")
        print(f"이미지 링크 : {link}")

        images_res = requests.get(link)
        images_res.raise_for_status()

        with open("NadoCoding\webscapping_basic\scapped_images\{}_{}.jpg".format(year,idx+1),"wb") as f:
            f.write(images_res.content) 
    
        print("-"*100)
    print("="*100)
