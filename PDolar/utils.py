import pytz, os
import datetime as dt, pandas as pd

gmt5 = pytz.timezone("Etc/GMT+5")


today = dt.datetime.now(gmt5).strftime("%d-%m-%Y")  # 01-12-20xx | Peru
now = dt.datetime.now(gmt5).strftime("%H:%M:%S")


def exist_and_save_now(data: pd.DataFrame, csv_path: str):
    data = data.assign(time=now)
    if os.path.exists(csv_path):
        data_last = pd.read_csv(csv_path)
        new_data = pd.concat((data_last, data))
        new_data.to_csv(csv_path, index=False)
    else:
        data.to_csv(csv_path, index=False)


def today_csv(house: pd.DataFrame, bank: pd.DataFrame):
    house_csv = f"data/{today}_he.csv"  # house_exchange
    bank_csv = f"data/{today}_bank.csv"
    exist_and_save_now(house, house_csv)
    exist_and_save_now(bank, bank_csv)


nextid = "log/buildID_next.csv"


def read_ids() -> pd.DataFrame:
    return pd.read_csv(nextid)


def get_last_id() -> str:
    last_id = read_ids().sort_values("date", ascending=False)["id"].values[0]
    return last_id


def now_time():
    return dt.datetime.now(gmt5)


def update_ids(id):
    last_log = read_ids()
    df = pd.DataFrame({"date": [now_time()], "id": [id]})
    final = pd.concat((last_log, df))
    final.to_csv(nextid, index=False)
