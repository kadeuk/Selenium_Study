import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

driver.get('https://www.naver.com')
time.sleep(3)

css_selector = "#right-content-area > div.Layout-module__right_top___h3g3v > div.Layout-module__content_area___b_3TU.Layout-module__type_issue___Ynxkj > div > div > div > div > div > a > span.IssueBanner-module__issue_text___KBlrG"

group_navi = driver.find_element(By.CSS_SELECTOR, css_selector)
#print(group_navi.text)
group_navi.click()
input()