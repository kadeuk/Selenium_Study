import requests
from bs4 import BeautifulSoup
import pandas as pd 
from fake_useragent import UserAgent

# 이 코드를 어떻게 활용할 것인가? 
def getSoup(com_code):
    url = 'https://finance.naver.com/item/sise_day.naver?code=005930&page=' + com_code
    ua = UserAgent()
    
    # 기존 user-agent와 원리는 같음. 다만, 이런 라이브러리가 존재한다! 정도로만 확인해주세요!
    headers = {'user-agent' : ua.ie} 
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    return soup 

def getPrice(com_code):
    soup = getSoup(com_code)
    시세 = soup.find_all("table.type2") # print(no_today)
    컬럼 = 시세.find_all("th").get_text()
    
    return 컬럼

# def main():
#     com_codes = ["030200", "005930", "035720"]
#     com_names = ["KT", "삼성전자", "카카오"]

#     prices = []
#     for code in com_codes:
#         price = getPrice(code)
#         prices.append(price)
    
#     df = pd.DataFrame({"종목코드":com_codes, "상장회사":com_names, "주가":prices})
#     print(df)
#     df['날짜'] = "오늘날짜"
#     print(df)
        
# if __name__ == "__main__":
#     main()