import requests
from bs4 import BeautifulSoup
import pandas as pd

dataDict = {
    "Names": [],
    "NewPrice": [],
    "OldPrice": [],
    "Descriptions": [],

}


url = ["https://www.techlandbd.com/shop-laptop-computer/brand-laptops/apple-macbook?sort=p.price&order=ASC&limit=100"]

req = requests.get(url[0])

soup = BeautifulSoup(req.text, "lxml")

allNames = soup.find_all("div", class_="name")
allDescriptions = soup.find_all("div", class_="description")
allPrice = soup.find_all('div', class_='price')



for index, (name, desc, price) in enumerate(zip(allNames, allDescriptions, allPrice)):
    pass




# for index, (name, item, p1, p2) in enumerate(zip(allNames, allDescriptions,newPrices, oldPrices)):
#     dataDict["Names"].append(name.text)
#     dataDict["NewPrice"].append(p1.text)
#     dataDict["OldPrice"].append(p2.text)
#     dataDict["Descriptions"].append(item.text)
    
    
# df = pd.DataFrame(dataDict)
# print(df)
# df.describe()
# print(len(dataDict["Names"]))
# print(len(dataDict["Descriptions"]))

# df.to_excel('techlandprice.xlsx', sheet_name="NamePrice")
# print(len(dataDict["Names"]))