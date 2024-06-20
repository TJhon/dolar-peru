from selenium import webdriver
import time, pandas as pd, numpy as np, os
from selenium.webdriver.common.by import By

from dotenv import load_dotenv

load_dotenv()


local = os.environ.get("RUN")
print(local)

from local import options


MAIN_URL  = 'https://cuantoestaeldolar.pe'


if local == 'local':
    driver = webdriver.Chrome()
else:
    driver = webdriver.Chrome(options=options)

driver.get(MAIN_URL)

# sunat

a = driver.find_element(By.XPATH, '//*[@id="converter"]/div/div[2]/div[1]')

print(a.text)
# firsm

# b = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[5]/div/div[1]/div[26]/div[1]')
# c = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[5]/div/div[1]/div[27]/div[1]')
# d = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[3]/div[5]/div/div[2]/div[13]/div[1]')
# print(b.text, d.text) 