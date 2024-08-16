from PDolar.S_dolar import driver
from PDolar.selenium_config.types_selenium import *
from PDolar.exchange_house.scrapper import dolar_house_exchange
from PDolar.banks.scrapper import dolar_bank_exchange

from PDolar.utils import today_csv

# print(today_csv)


exchange_house = dolar_house_exchange(driver)
banks = dolar_bank_exchange(driver)

today_csv(exchange_house, banks)
