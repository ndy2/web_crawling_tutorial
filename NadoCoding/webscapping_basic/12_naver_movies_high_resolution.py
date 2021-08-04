import requests
from bs4 import BeautifulSoup
import re

# link = "https://movie-phinf.pstatic.net/20210617_272/1623906098516QjpeS_JPEG/movie_image.jpg"
# images_res = requests.get(link)
# images_res.raise_for_status()

# with open("NadoCoding\webscapping_basic\scapped_images\Black_Widow.jpg","wb") as f:
#     f.write(images_res.content) 

p = re.compile("code=\d\d\d\d\d\d")

for year in range(2019,2022) :
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}년 영화순위".format(year)
    print(year , "년 상위 3개 영화 순위")
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all("div", attrs= {"class" : "thumb"})

    for idx, image in enumerate(images):
        if idx>2 :
            break
        name = image.img["alt"]
        print(f"제목 : {name}")
        movie_query_url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}".format(name)
        
        res_movie = requests.get(movie_query_url)
        res_movie.raise_for_status()
        soup_movie = BeautifulSoup(res_movie.text,"lxml")

        naver_movie_url = soup_movie.find("a",attrs={"class" : "area_text_title"})["href"]
        print(f"네이버 영화 링크 : {naver_movie_url}")
        
        code_idx = p.search(naver_movie_url).span()[0]+5
        code = naver_movie_url[code_idx:code_idx+6]

        print(f"네이버 영화 코드 : {code}")
        image_url = "https://movie.naver.com/movie/bi/mi/photoViewPopup.naver?movieCode={}".format(code)
        res_image = requests.get(image_url)
        res_image.raise_for_status()
        soup_image = BeautifulSoup(res_image.text,"lxml")
        
        image_save_url = soup_image.find("a").img["src"]
        print(f"이미지 저장 주소 : {image_save_url}")
        res_image_save = requests.get(image_save_url)
        res_image_save.raise_for_status()
        
        with open("NadoCoding\webscapping_basic\scapped_images\{}_{}_{}.jpg".format(year,idx+1,name),"wb") as f:
            f.write(res_image_save.content)
    
        print("-"*100)
    print("="*100)
