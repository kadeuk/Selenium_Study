import urllib.request
from bs4 import BeautifulSoup
import requests


url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

css_selector = 'a.api_txt_lines.total_tit'

elements = soup.select(css_selector)
for element in elements:
    text = element.text
    url = element['href']
    print(len(text))
    print(len(url))