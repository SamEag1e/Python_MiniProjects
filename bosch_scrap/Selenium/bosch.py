"""This module gets data from the given BOSCH url"""

from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.common.exceptions import NoSuchElementException

url = "https://www.bosch-repair-service.com/en/productsearch/NaN-NaN?product_search=026"

browser = webdriver.Chrome()
browser.get(url)


while True:
    h4s = browser.find_elements(
        By.CSS_SELECTOR, "h4.violet-blue-gradient-text"
    )
    names = [name.text for name in h4s]
    next_ = browser.find_elements(
        By.CSS_SELECTOR, "div.text-center > ul > li > a"
    )
    # print(names)
    # buttons = [h.text for h in next_]
    # print(hello[-2])
    clickable = next_[-2]
    clickable.click()
