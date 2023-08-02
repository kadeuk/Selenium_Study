import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()