import requests
res = requests.get("http://naver.com")
# res = requests.get("http://nadocoding.tistory.com")
print("응답 코드 : ", res.status_code) #200이면 정상
res.raise_for_status()

print(len(res.text))
# print(res.text)

with open("mynaver.html","w",encoding="utf8") as f:
    f.write(res.text)