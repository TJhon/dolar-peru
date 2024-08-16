from selenium import webdriver
import time, pandas as pd, numpy as np, os
from selenium.webdriver.common.by import By


from dotenv import load_dotenv

load_dotenv()


local = os.environ.get("RUN")
print(local)

from PDolar.selenium_config.s_config import options


MAIN_URL = "https://cuantoestaeldolar.pe"


if local == "local":
    driver = webdriver.Chrome()
else:
    driver = webdriver.Chrome(options=options)

driver.get(MAIN_URL)
print("----")
from selenium.webdriver.common.keys import Keys

html = driver.find_element(By.TAG_NAME, "html")
n = 0
while n < 3:
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    n += 1
