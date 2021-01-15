from selenium import webdriver

PATH = "/Users/bigvdhopte/Documents/Vedant/Python/ShoeWebScraper/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://sneakernews.com/release-dates/")
print(driver.title)
driver.close()