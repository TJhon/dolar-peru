from .types_selenium import *


def value_element_xpath(xpath: str, driver: WebDriver):
    return driver.find_element(By.XPATH, xpath)
    # try:
    #     element = WebDriverWait(driver, 10).until(
    #         EC.invisibility_of_element((By.XPATH, xpath))
    #     )
    #     return element
    # finally:
    #     print("An exception occurred")
