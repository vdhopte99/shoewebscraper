import requests
import urllib.request
import sys
from bs4 import BeautifulSoup as soup
import random
import time

def returnDrops(month):
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

    if month == "January":
        month = "01"
    if month == "February":
        month = "02"
    if month == "March":
        month = "03"
    if month == "April":
        month = "04"
    if month == "May":
        month = "05"
    if month == "June":
        month = "06"
    if month == "July":
        month = "07"
    if month == "August":
        month = "08"
    if month == "September":
        month = "09"
    if month == "October":
        month = "10"
    if month == "November":
        month = "11"
    if month == "December":
        month = "12"

    soleCollector = "https://solecollector.com/sneaker-release-dates/all-release-dates/2021/" + month
    response = requests.get(soleCollector, headers=headers)
    sole_soup = soup(response.content, "html.parser")
    releaseDates = sole_soup.findAll("div", {"class": "release-group__container"})
    drops = []

    for date in releaseDates:
        day = date.text.replace("\n", " ")
        day = day.split(" ")
        day = day[3]

        shoes = date.findAll("div", {"class": "row"})
        for shoe in shoes:
            image = shoe.find("img")
            image = image["src"]
            shoe = shoe.text
            shoe = shoe.split("$")
        
            name = shoe[0]
            name = name.replace("\n", "")
            name = name.strip()

            if (len(shoe) < 2):
                price = 0
            else:
                price = shoe[1]
                price = price.replace("\n", "")
                price = price.strip()
                price = int(price)
            
            drops.append((name, price, image, day))

    dropList = []
    for shoe in drops:
        query = shoe[0]
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
        print(link)

        if link.find("stockx") == -1:
            dropList.append({"name": shoe[0], "retail": shoe[1], "image": shoe[2], "resale": 0, "profit": 0, "date": shoe[3]})
            continue

        response = requests.get(link, headers=headers)
        stockx_soup = soup(response.content, "html.parser")
        resale = stockx_soup.find_all("div", {"class": "stats"})
        
        if resale is None or len(resale) == 0:
            dropList.append({"name": shoe[0], "retail": shoe[1], "image": shoe[2], "resale": 0, "profit": 0, "date": shoe[3]})
            continue

        resale = resale[0].text
        resale = resale.split("L")
        resale = resale[0]

        if resale == "--":
            dropList.append({"name": shoe[0], "retail": shoe[1], "image": shoe[2], "resale": 0, "profit": 0, "date": shoe[3]})
            continue

        temp = ""
        for char in resale:
            try:
                digit = int(char)
                temp += char
            except:
                continue
        resale = int(temp)
        
        if shoe[1] != 0:
            dropList.append({"name": shoe[0], "retail": shoe[1], "image": shoe[2], "resale": resale, "profit": (resale - shoe[1]), "date": shoe[3]})
        else:
            dropList.append({"name": shoe[0], "retail": shoe[1], "image": shoe[2], "resale": resale, "profit": 0, "date": shoe[3]})

    return dropList

# headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
# link = "https://stockx.com/air-jordan-5-retro-white-stealth-2021-ps"
# response = requests.get(link, headers=headers)
# stockx_soup = soup(response.content, "html.parser")
# resale = stockx_soup.find_all("div", {"class": "stats"})

# print(len(resale))
# resale = resale[0].text
# resale = resale.split("L")
# resale = resale[0]
# if resale == "--":
#     print("JJ")
# print(resale)