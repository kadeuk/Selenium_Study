import urllib.request
from bs4 import BeautifulSoup

url = 
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
