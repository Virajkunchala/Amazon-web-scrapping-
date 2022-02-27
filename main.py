from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import json

s = Service('/Users/Y520/Downloads/chromedriver_win32/chromedriver.exe')
# assign your website to scrape
web = 'https://www.amazon.in'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--log-level=1')

# create a driver object using driver_path as a parameter
driver = webdriver.Chrome(options=options, service=s)



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