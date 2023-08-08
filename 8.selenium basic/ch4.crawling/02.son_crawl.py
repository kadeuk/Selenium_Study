import requests
from bs4 import BeautifulSoup

base_url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query='
keyword = input('검색어를 입력하세요: ')
url = base_url + keyword

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

req = requests.get(url, headers=headers)

html = req.text

soup = BeautifulSoup(html, 'html.parser')

total_area = soup.select('._list_base')

for area in total_area:
    print(area)

# for result in results:
#     href = result.get('href')
#     print(href)
#     print(result)
#     print()
