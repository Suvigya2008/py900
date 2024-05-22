import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com/"
html = requests.get(url).content

soup = BeautifulSoup(html,"html.parser")
book_html = soup.find_all("h3")
book = [item.text for item in book_html]
price_html = soup.find_all(class_="price_color")
price = [i.text for i in price_html]
availability_html = soup.find_all(class_="instock availability")
availability = [k.text for k in availability_html]
dictionary = {
    "book":book,"price":price,"availability":availability
}
df = pd.DataFrame(dictionary)
print(df)