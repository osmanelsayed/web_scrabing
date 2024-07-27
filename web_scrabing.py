import requests
from bs4 import BeautifulSoup
import time

start_time = time.time()
responde = requests.get("https://books.toscrape.com/")

data = BeautifulSoup(responde.content,"html.parser")

articles = data.find_all("article")

for article in articles:
    titles= article.h3.a["title"]
    price = article.find(class_="price_color").text
    rate = article.p["class"][1]
    print (f"the title of book is {titles} and price is  {price} and rate is {rate}")
end_time = time.time()
print("الطريقة الأولى: وقت التنفيذ =", end_time - start_time)