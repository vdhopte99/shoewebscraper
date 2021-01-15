from selenium import webdriver

PATH = "/Users/bigvdhopte/Documents/Vedant/Python/ShoeWebScraper/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://sneakernews.com/release-dates/")

shoes = driver.find_elements_by_class_name("image-box")

print(len(shoes))

for shoe in shoes:
    print(shoe.text)
    print("---------------------------------------------------------------------------------------")

driver.quit()


