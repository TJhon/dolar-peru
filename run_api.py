from PDolar.utils import today_csv, get_last_id

from PDolar.api import PeruDolar

id = get_last_id()
today = PeruDolar(id=id)
banks = today.bank
houses = today.houses


today_csv(houses, banks)
