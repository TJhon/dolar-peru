import numpy as np, itertools, pandas as pd
from .constants import *
from ..selenium_config.utils import value_element_xpath
from .utils import extract_domain


def gen_divs(n, left=True, prev_ndiv=PREV_XPATH, n_div_tbl_location=6, after="div[1]"):
    values_divs = range_right
    div_col = 2
    if left:
        values_divs = range_left
        div_col = 1

    n_value = values_divs[n]

    div_location = f"div[{n_div_tbl_location}]/div/"
    div_column = f"div[{div_col}]/"
    div_row = f"div[{n_value}]/{after}"
    div = prev_ndiv + div_location + div_column + div_row
    return div


def gen_img(div, after="/div[1]/div[1]/span/img", bank=False):
    if bank:
        after = "/div[1]/span/img"

    return div + after


def gen_href(div, after="/div[3]/a"):
    return div + after


def xpaths_divs(total=N_rows):
    left_right = [True, False]
    combinations = list(itertools.product(list(range(total)), left_right))
    xpaths_base = [gen_divs(n_row, col) for n_row, col in combinations]
    xpath_img = [gen_img(xpath) for xpath in xpaths_base]
    xpath_a = [gen_href(xpath) for xpath in xpaths_base]

    sorted_xpath = [
        [base, img, a] for base, img, a in zip(xpaths_base, xpath_img, xpath_a)
    ]

    return sorted_xpath


def gen_dolar_values(div, driver):
    try:
        dolar = value_element_xpath(div, driver).text.split("\n")
    except:
        dolar = ["dummy", "Cambiar", np.nan, np.nan, np.nan, np.nan]
    return dolar


def gen_url_imagen(div, driver):
    try:
        return value_element_xpath(div, driver).get_attribute("src")

    except:
        return ""
    # return


def gen_url_companny(div, driver):
    try:
        return value_element_xpath(div, driver).get_attribute("href")
    except:
        return ""


def get_values_dolar(srt_values, driver):
    base, img, companny = srt_values

    dolar = gen_dolar_values(base, driver)
    img_url = gen_url_imagen(img, driver)
    companny_url = gen_url_companny(companny, driver)

    return dolar + [img_url, companny_url]


def dolar_house_exchange(driver, names=COLUMNS_NAMES):
    xpaths = xpaths_divs()
    result = [get_values_dolar(xpath, driver) for xpath in xpaths]
    data_dolar = pd.DataFrame(result)
    data_dolar.columns = names
    data_dolar["companny_name"] = data_dolar["companny_url"].apply(extract_domain)
    return data_dolar
