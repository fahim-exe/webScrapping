import requests
from bs4 import BeautifulSoup
import pandas as pd

dataDict = {
    "Names": [],
    "CurrentPrice": [],
    "RegularPrice": [],
    "Descriptions": [],

}


url = ["https://www.techlandbd.com/shop-laptop-computer/brand-laptops/apple-macbook?sort=p.price&order=ASC&limit=100"]

req = requests.get(url[0])

soup = BeautifulSoup(req.text, "lxml")

product_cards = soup.find_all('div', class_='product-thumb')


for i in range(len(product_cards)):
    name = product_cards[i].find('div', class_='name').text
    desc = product_cards[i].find('div', class_='description').text

    if product_cards[i].find('span', class_='price-new'):
        crnt_price = product_cards[i].find('span', class_='price-new')
        rglr_price = product_cards[i].find('span', class_='price-old')
        

    if product_cards[i].find('span', class_='price-normal'):
        crnt_price = product_cards[i].find('span', class_='price-normal')
        rglr_price = product_cards[i].find('span', class_='price-normal')
        

    dataDict["Names"].append(name)
    dataDict["CurrentPrice"].append(crnt_price)
    dataDict["RegularPrice"].append(rglr_price)
    dataDict["Descriptions"].append(desc)



# print(dataDict)