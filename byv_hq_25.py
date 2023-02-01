import requests
from bs4 import BeautifulSoup
import time
from random import random
# from product import Product

URL = "https:///"

time.sleep(3 + random() * 4)
resp = requests.get(URL)
resp.encoding = "UTF8"
with open("index.html", "w") as f:
    f.write(resp.text)
# print(resp.text)

soup = BeautifulSoup(resp.text, "html.parser")
table = soup.select("#js-partslist-primary > tbody > tr")
with open("price.log", "w", encoding="utf") as f:
    for row in table:
        product = Product()
        product.maker = row.select('[data-type |= "maker"]')[0].text
        product.price = row.select('[data-type |= "price"]')[0].text
        print(product)
        f.write(str(product) + "\n")
