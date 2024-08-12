import pandas as pd

N_banks = 5
from ..exchange_house.constants import PREV_XPATH
from ..exchange_house.scrapper import gen_dolar_values, gen_url_imagen, gen_img

PREV_XPATH


def gen_divs_bank(n=N_banks):
    divs_bank = [
        PREV_XPATH + f"div[9]/div/div[2]/div[{_n}]/div[1]" for _n in range(1, n + 1)
    ]
    return divs_bank


def bank_name(url):
    try:
        parts = url.split("/")
        name = parts[-1].split(".")[0]
    except:
        name = "None"
    return name


def dolar_bank_exchange(driver):

    banks_xpaths = gen_divs_bank()
    dolar_values = [gen_dolar_values(bank, driver=driver) for bank in banks_xpaths]

    bank_imgs = [
        gen_url_imagen(gen_img(bank, bank=True), driver=driver) for bank in banks_xpaths
    ]
    banks_data = [dolar + [img] for dolar, img in zip(dolar_values, bank_imgs)]
    banks_data = pd.DataFrame(banks_data, columns=["compra", "venta", "img_url"])
    banks_data["companny_name"] = banks_data["img_url"].apply(bank_name)
    return banks_data
