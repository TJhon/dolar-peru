from PDolar.utils import update_ids
import time

from PDolar.S_dolar import driver

time.sleep(5)
script = """
return window['__NEXT_DATA__']
"""
result = driver.execute_script(script)
id = result["buildId"]
update_ids(id)
