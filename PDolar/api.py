import requests, pandas as pd
from .utils import get_last_id

def value_extrar_dict(ref: dict):
    buy = ref["buy"]
    sale = ref["sale"]
    cost = "cost"
    variation = "variation"
    buy_cost = buy[cost]
    buy_var = buy[variation]

    sale_cost = sale[cost]
    sale_var = sale[variation]
    return pd.Series([buy_cost, buy_var, sale_cost, sale_var])


class PeruDolar:
    def __init__(
        self,
        base_url="https://cuantoestaeldolar.pe/_next/data/{}/cambio-de-dolar-online.json",
        id="PelW_tB5ARYtZktu7nOSo",
        data_key="pageProps",
        banks_key="exchangeBanks",
        house_key="onlineExchangeHouses",
        columns_name_values=[
            "buy_cost",
            "buy_variation",
            "sale_cost",
            "sale_variation",
        ],
    ) -> None:
        if id is None:
            id = get_last_id()
        url = base_url.format(id)
        self.url = url
        self.data_key = data_key
        self.bank_key = banks_key
        self.house_key = house_key
        self.columns_dolar = columns_name_values
        self.extract_data()
        bank_data = self.banks_data()
        house_data = self.house_data()
        sunat_exchange = self.sunat_data()
        self.bank = bank_data
        self.houses = house_data
        self.sunat = sunat_exchange

    def extract_data(self) -> None:
        url = self.url

        response = requests.get(url).json()
        self.response = response
        self.data = response[self.data_key]

    def banks_data(self, sort_by=["type", "buy_cost", "name"]) -> pd.DataFrame:
        banks = self.data[self.bank_key]
        cols = self.columns_dolar
        results = []
        real_banks = ["Interbank", "nacion", "bbva", "scotiabank", "bcp"]

        for bank in list(banks.keys()):
            ref_bank = banks[bank]
            type = "bank" if bank in real_banks else "currency"
            buy_cost, buy_var, sale_cost, sale_var = value_extrar_dict(ref_bank)
            result = {
                "name": bank,
                "type": type,
                cols[0]: buy_cost,
                cols[1]: buy_var,
                cols[2]: sale_cost,
                cols[3]: sale_var,
            }
            results.append(result)
        return pd.DataFrame(results).sort_values(sort_by)

    def house_data(
        self,
        reference_json={
            "title": "companny_name",
            "img": "img",
            "site": "companny_url",
            "bank": "banks",
            "schedule": "days_open",
            "updated_at": "last_updated",
            "rates": "buy_sale",
        },
        rate="rates",
        drop_col=["buy_sale"],
    ) -> pd.DataFrame:
        cols_ = self.columns_dolar
        exchange_house = self.data[self.house_key]

        data_ref = pd.DataFrame(exchange_house)[list(reference_json.keys())]
        data_ref[cols_] = data_ref[rate].apply(value_extrar_dict)
        new_cols = list(reference_json.values()) + cols_
        data_ref.columns = new_cols
        # return data_ref
        return data_ref.drop(columns=drop_col)

    def sunat_data(self, key="exchangeSunat"):

        ref = self.data[key]

        return value_extrar_dict(ref)
