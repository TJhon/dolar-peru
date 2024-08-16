from PDolar.utils import today_csv, get_last_id, update_ids

from PDolar.api import PeruDolar
import time


try:
    id = get_last_id()
    today = PeruDolar(id=id)
    banks = today.bank
    houses = today.houses

except:
    from PDolar.S_dolar import driver

    time.sleep(5)
    script = """
    return window['__NEXT_DATA__']
    """
    result = driver.execute_script(script)
    id = result["buildId"]
    update_ids(id)
    today = PeruDolar(id=id)
    banks = today.bank
    houses = today.houses


today_csv(houses, banks)
