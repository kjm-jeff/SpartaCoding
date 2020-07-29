import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################

movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
movies_data = []
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div> a')
    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        title = movie.select_one('td.title > div > a').text
        point = movie.select_one('td.point').text
        print(rank, title, point)
        data = {'rank': rank, 'point': point, 'title': title}
        movies_data.append(data)

print(movies_data)

#db.movies.delete_many({})
db.movies.insert_many(movies_data)
"""
for movie in movies:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('td.title > div > a')
    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt']  # img 태그의 alt 속성값을 가져오기
        title = a_tag.text  # a 태그 사이의 텍스트를 가져오기
        star = movie.select_one('td.point').text  # td 태그 사이의 텍스트를 가져오기
        print(rank, title, star)
"""