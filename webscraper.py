# from selenium import webdriver
import requests
import urllib.request


# from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# PATH = "/Users/bigvdhopte/Documents/Vedant/Python/ShoeWebScraper/chromedriver"
# driver = webdriver.Chrome(PATH)
soleCollector = "https://solecollector.com/sneaker-release-dates/all-release-dates/"

response = requests.get(soleCollector)

sole_soup = soup(response.content, "html.parser")



# uClient = uReq(soleCollector)
# sole_html = uClient.read()
# uClient.close()

# sole_soup = soup(sole_html, "html.parser")
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

    # driver.get("https://stockx.com/")

    # search = driver.find_element_by_name("q")

    
    # search.send_keys(januaryShoes[0][0])
    # search.send_keys(Keys.RETURN)

    # time.sleep(5)


    # image = driver.find_element_by_class_name("tile browse-tile updated")
    # image = image.find_element_by_tag_name("img")
    # image = image.get_attribute("src")




    # driver.quit()


query = januaryShoes[0][0]
query = query.split(" ")

url = "https://stockx.com/search/sneakers?s="

for i in range(len(query)):
    url += query[i]
    if i != len(query) - 1:
        url += "20"


response = requests.get(url)
stockx_soup = soup(response.content, "html.parser")

images = stockx_soup.find_all("img")

print(len(images))



