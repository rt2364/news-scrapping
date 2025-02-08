from bs4 import BeautifulSoup
import requests
URL="https://www.bbc.com/news"
r=requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')# html.parser for data.text
#print(soup.prettify())
items = soup.find_all('h2', attrs={"data-testid": 'card-headline'})
#print(items)
for item in items:
  print(item.text)