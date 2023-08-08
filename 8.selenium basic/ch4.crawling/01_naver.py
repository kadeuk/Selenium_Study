import requests
from bs4 import BeautifulSoup

url = "https://naver.com"



headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
req = requests.get(url, headers=headers)
print(req.request.headers)
# html = req.text
# soup = BeautifulSoup(html, "html.parser")

# logo = soup.find_all(".blind").text
# print(logo)

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
# url = "https://naver.com"

# req = requests.get(url)

# html = req.text
# soup = BeautifulSoup(html, "html.parser")

# logo_element = soup.find("a", class_=".blind")  # 클래스 이름만 사용하여 찾기
# if logo_element:
#     logo_text = logo_element.text.strip()  # 텍스트를 가져오고 앞뒤 공백 제거
#     print(logo_text)
# else:
#     print("NAVER 로고를 찾을 수 없습니다.")

#special-input-logo > a.link_naver.type_motion_n.is_fadein