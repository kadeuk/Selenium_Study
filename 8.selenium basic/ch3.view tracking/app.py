import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# searchq ='파이썬 셀레니움'
# target_blog_link = 'https://www.sagein.net/708'

searchqs = ['파이썬 셀레니움', '파이썬 플라스크']
target_blog_links =['https://www.sagein.net/708', 'https://yeko90.tistory.com/252']

for searchq, target_blog_link in zip(searchqs, target_blog_links):
    search_link=f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={searchq}'
    driver.get(search_link)
    time.sleep(2)

    link_selector = f'a[href^="{target_blog_link}"]'

    nowlank = -1

    # element = driver.find_element(By.CSS_SELECTOR, link_selector)

    #예외처리
    BLOG_FOUND = False
    for _ in range(7):
        try:
            element = driver.find_element(By.CSS_SELECTOR, link_selector)
            while True:
                new_element = element.find_element(By.XPATH, "./..")
                nowlank = new_element.get_attribute("data-cr-rank")
                if nowlank != None:
                    # print('현재랭크 찾음:', nowlank)
                    BLOG_FOUND = True
                    break
                # print('현재랭크 찾음')
                element = new_element
            if BLOG_FOUND:
                break
        except:
            print('타겟 블로그를 못찾음 --> 스크롤 하겠습니다.')
            driver.execute_script('window.scrollBy(0, 10000);')
            time.sleep(3)
    
    print(f'{searchq} / {nowlank} : 타켓 블로그의 랭크를 찾았습니다.')

# print(f'{searchq}: 타겟 블로그의 랭크를 찾았습니다.')

input()