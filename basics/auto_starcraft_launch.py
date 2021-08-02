import pyautogui as pg
from time import sleep

img_dir = "C:/Users/1/Desktop/web_crawling_tutorial/Images"

button5location = pg.locateOnScreen(img_dir + "/Icon/starcraft.jpg",confidence = 0.9) # 이미지가 있는 위치를 가져옵니다.
if button5location == None :
    print("Find Icon")
    exit(-1)
pg.moveTo(button5location)
pg.doubleClick()

button5Opengame = None
while button5Opengame == None:
    sleep(10)
    button5Opengame = pg.locateOnScreen(img_dir+'/Icon/play.JPG',confidence = 0.9)
pg.moveTo(button5Opengame)
pg.doubleClick()

sleep(30)
pg.press('enter') # enter key를 입력합니다.

pg.press('m') # m key를 입력합니다.
pg.press('e') # e key를 입력합니다.
pg.press('enter') # enter key를 입력합니다.
pg.press('enter') # enter key를 입력합니다.


