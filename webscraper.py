from selenium import webdriver

PATH = "/Users/bigvdhopte/Documents/Vedant/Python/ShoeWebScraper/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://solecollector.com/sneaker-release-dates/all-release-dates/")

#dates = driver.find_elements_by_class_name("sneaker-release__date")
shoes = driver.find_elements_by_class_name("row")

print(len(shoes))

for shoe in shoes:
    print(shoe.text)
    print("---------------------------------------------------------------------------------------")



#driver.get("https://stockx.com/")

driver.quit()



