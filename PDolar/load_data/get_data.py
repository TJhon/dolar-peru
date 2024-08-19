# raw data sample
# https://raw.githubusercontent.com/TJhon/dolar-peru/main/data/19-08-2024_he.csv

types_data = ['bank', #banks and other
          'he' # house exchange
         ]


from datetime import datetime as dt, timedelta
import pandas as pd
import itertools

MIN_DATE = dt(2024, 8, 15)

MAX_DATE = dt.now()

def get_url_data(date, type, PREV = 'https://raw.githubusercontent.com/TJhon/dolar-peru/main/data/{date}_{type}.csv'):
    date = format_date(date)
    url = PREV.format(date=date, type=type)
    return url

def format_date(date):
    return date.strftime("%d-%m-%Y")



def dates_between(min_date, max_date):

    if min_date < MIN_DATE:
        print("The start of scraping for this project was the date 08/15/2024, replacing...")
        min_date = MIN_DATE
    if max_date < MAX_DATE:
        print("The start of scraping for this project was the date 08/15/2024, replacing...")
        max_date = MAX_DATE

    dates_btwn = []
    date_eval = min_date
    while date_eval <= max_date:
        dates_btwn.append(date_eval)
        date_eval += timedelta(days=1)
    return dates_btwn

def read_multiple_dates(urls: list):
    data = []
    for url in urls:
        try:
            data_read = pd.read_csv(url)
            data.append(data_read)
        except:
          print('Failed to read data')
    data_db = pd.concat(data, ignore_index=True)
    return data_db

def load_data(min_date, max_date, types: list = types_data):
    dates_btw = dates_between(min_date, max_date)
    cbm_iter = itertools.product(types, dates_btw)
    combinations = list(cbm_iter)

    urls_type = [(get_url_data(date, type), type) for type, date in combinations]
    collect = {}
    for type in types:
        filter_url = [url[0] for url in urls_type if url [1] == type]
        collect[type] = read_multiple_dates(filter_url)

    return collect


def last_days_data(max_date= MAX_DATE, days = 7, types=types_data):
    min_date = max_date - timedelta(days=days)
    return load_data(min_date, max_date, types)


