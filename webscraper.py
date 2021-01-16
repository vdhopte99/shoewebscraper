import requests
import urllib.request
import sys
from bs4 import BeautifulSoup as soup

headers={"User-Agent": 
"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

soleCollector = "https://solecollector.com/sneaker-release-dates/all-release-dates/"
response = requests.get(soleCollector)
sole_soup = soup(response.content, "html.parser")
shoes = sole_soup.findAll("div", {"class": "row"})
januaryShoes = []

for shoe in shoes:
    shoe = shoe.text
    shoe = shoe.split("$")
    
    name = shoe[0]
    name = name.replace("\n", "")
    name = name.strip()

    if (len(shoe) < 2):
        price = None
    else:
        price = shoe[1]
        price = price.replace("\n", "")
        price = price.strip()
        price = int(price)

    januaryShoes.append((name, price))



query = januaryShoes[0][0]
query = query.split(" ")

url = "https://www.google.com/search?sxsrf=ALeKk03vlxoCHnl3qL59fhmKl08krVu-Mg%3A1610822395327&ei=-zIDYL24E5il5NoP48Sg2Ak&q="

for i in range(len(query)):
    url += query[i] + "+"

url += "stockx&oq=Adidas+Harden+Vol.+5+Crystal+White%2FCloud+White%2FRoyal+Blue+stockx&gs_lcp=CgZwc3ktYWIQAzoECCMQJzoHCCMQrgIQJzoFCCEQoAE6BAghEApQ7RhYiR9gwx9oAHAAeACAAXqIAd8FkgEDNi4ymAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab&ved=0ahUKEwj9oa2FjaHuAhWYElkFHWMiCJsQ4dUDCA0&uact=5"

response = requests.get(url, headers=headers)
google_soup = soup(response.content, "html.parser")

link = google_soup.find('div', {"class": "g"})
link = link.find('a', href=True)
link = link["href"]

response = requests.get(link, headers=headers)
stockx_soup = soup(response.content, "html.parser")

price = stockx_soup.find("div", {"class": "stats"})

print(price.text)



