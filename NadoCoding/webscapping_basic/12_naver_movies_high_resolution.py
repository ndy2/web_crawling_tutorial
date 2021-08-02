import requests
from bs4 import BeautifulSoup

link = "https://movie-phinf.pstatic.net/20210617_272/1623906098516QjpeS_JPEG/movie_image.jpg"
images_res = requests.get(link)
images_res.raise_for_status()

with open("NadoCoding\webscapping_basic\scapped_images\Black_Widow.jpg","wb") as f:
    f.write(images_res.content) 
