import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.get('https://naver.com')

try:
    selector = '#__next > div > div.CommerceView_commerce_area__zStN3 > div.HotItem_commerce_five_column__Ff0HZ > ul > li:nth-child(5) > div > div > a > div:nth-child(1)'
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(By.CSS_SELECTOR, selector))
    drivers = driver.find_element_by_id(selector)
    drivers.click()
except:
    print('예외 발생, 예외 처리 코드 실행하기')
print('엘리먼트 로딩 끝')
print('다음 코드 실행')
input()

#driver.get('https://www.naver.com')
#time.sleep(1)
#driver.get('https://google.com')
#
#driver.back()
#time.sleep(2)
#
#driver.forward()
#time.sleep(2)
#
#driver.refresh()
#time.sleep(2)
#print('동작끝')
#input()
# driver.get('https://www.naver.com')
# time.sleep(1)

# title = driver.title
# print(title, '가 타이틀이다')

# now_addrese = driver.current_url
# print(now_addrese, '가 현재주소다')
# input()



css_selector = "#right-content-area > div.Layout-module__right_top___h3g3v > div.Layout-module__content_area___b_3TU.Layout-module__type_issue___Ynxkj > div > div > div > div > div > a > span.IssueBanner-module__issue_text___KBlrG"

group_navi = driver.find_element(By.CSS_SELECTOR, css_selector)
#print(group_navi.text)
group_navi.click()
input()