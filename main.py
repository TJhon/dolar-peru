from PDolar.S_dolar import driver
from PDolar.selenium_config.types_selenium import *
from PDolar.exchange_house.scrapper import dolar_house_exchange
from PDolar.banks.scrapper import dolar_bank_exchange

exchange_house = dolar_house_exchange(driver)
banks = dolar_bank_exchange(driver)
print(exchange_house)
print(banks)
