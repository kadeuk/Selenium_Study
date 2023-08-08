from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
nate_list_1st = []
nate_list_2nd = []
for i in range(2):
    URL='https://www.nate.com'
    driver.get(url=URL) 
    rank_results = driver.find_elements(By.CSS_SELECTOR,'#olLiveIssueKeyword > li > span.num_rank')
    nate_results = driver.find_elements(By.CSS_SELECTOR,'#olLiveIssueKeyword > li > a > span.txt_rank')
    for rank, keyword in zip(rank_results, nate_results):
        if i == 0: # 첫번째 화면
            nate_list_1st.append(f'{rank.text}_{keyword.text}')
        elif i == 1: # 두번째 화면
            nate_list_2nd.append(f'{rank.text}_{keyword.text}')
    time.sleep(5)
    driver.refresh() # driver 재시동
result = nate_list_1st + nate_list_2nd

print(result)
driver.quit()