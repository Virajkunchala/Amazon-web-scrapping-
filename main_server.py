from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selectorlib import Extractor
import json



chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
#for headless browser 
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

# assign your website to scrape
web = 'https://www.amazon.in'

driver.get(web)
driver.implicitly_wait(5)
# getting the user input
keyword = input("Please enter the product name: ")
search = driver.find_element(By.XPATH, '//*[(@id = "twotabsearchtextbox")]')
search.send_keys(keyword)
# click search button
search_button = driver.find_element(By.ID,'nav-search-submit-button')
search_button.click()

driver.implicitly_wait(10)

product_asin = []
product_name = []
product_price = []

data=[]

items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "s-result-item s-asin")]')))
for item in items:
    # find product name
    name = item.find_element(By.XPATH,'.//span[@class="a-size-medium a-color-base a-text-normal"]')
    data.append(name.text)

    # find ASIN number 
    data_asin = item.get_attribute("data-asin")
    data.append(data_asin)

    # find the price
    total_price = item.find_element(By.XPATH,'.//span[@class="a-price-whole"]')
    
    data.append(total_price.text)
driver.quit()

#to check the scrapped data 
# print(item)
# print(type(data))
JsonData=json.dumps(data)
print(JsonData)
# print(product_name)
# print(product_asin)
# print(product_price)
