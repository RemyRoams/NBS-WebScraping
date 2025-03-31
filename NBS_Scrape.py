import pandas as pd
import requests
from bs4 import BeautifulSoup

book_list = []

for i in range(1,25):
   url = f'https://www.nationalbookstore.com/13-books?page={i}'
   html = requests.get(url)
   soup = BeautifulSoup(html.text, 'html.parser')

   books = soup.find_all('div', {'class' : 'product-description'})

   for book in books:
      book_name = book.find('h2', {'class':"h3 product-title"}).text

      book_price = book.find('span', {"class":"price"}).text
      book_price = book_price.replace(' ', "")
      book_price = book_price.replace(',', "")
      book_price = book_price[1:-2]

      book_list.append([book_name, book_price])

# print(book_list)

df = pd.DataFrame(book_list, columns = ["Title", "Price"])
print(df.head())

df.to_csv("NSB_Book_Price.csv", index = False)