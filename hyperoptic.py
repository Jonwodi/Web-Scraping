import pprint

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

SERVICE = Service(ChromeDriverManager().install())
browser1 = webdriver.Chrome(service=SERVICE)

# get website url
browser1.get("https://www.hyperoptic.com/offer/")

# locate accept cookies button
accept_cookies = browser1.find_element(
    By.XPATH, '//*[@id="cookiePolicyModal"]/div/div/div[3]/button[1]'
)

# click on accept cookies button
accept_cookies.click()

# time in seconds given for the search or poll document object model of html page before a element is found or an error is returned
browser1.implicitly_wait(30)

# empty list where all data, scraped from the url is appended into
deals = []

# deal name
# for loop used to append deal names from url into deals list
deal_name = browser1.find_elements(By.CLASS_NAME, "size-unit",)
for name in deal_name:
    deals.append({"deal name": name.text})

# deal price
# for loop used to append deal prices from url into deals list using index position to match it to other key data e.g. deal name
deal_prices = browser1.find_elements(By.CLASS_NAME, "price",)
for index, price in enumerate(deal_prices):
    deals[index]["deal price"] = price.text


# deal speed & setup cost
deal_speed_and_setup = browser1.find_elements(
    By.CLASS_NAME, "flat-text-bellow-price-wr",
)
for index, speed_and_cost in enumerate(deal_speed_and_setup):
    deals[index]["deal speed"] = speed_and_cost.text.splitlines()[1]
    deals[index]["deal setup cost"] = speed_and_cost.text.splitlines()[3]


# print heading for deals
print("__________________________")
print("Hyperoptic Broadband deals")
print("__________________________")

# deal contract length
deal_contract_length = browser1.find_elements(
    By.CLASS_NAME, "bold-text-bellow-price-wr"
)
for index, contract in enumerate(deal_contract_length):
    deals[index]["deal contract"] = contract.text

# return deals list data into the terminal in JSON like structure
pp = pprint.PrettyPrinter(indent=5)
pp.pprint(deals)
print("\n")

# returns data in pandas DataFrame structure
df = pd.DataFrame(deals)
pp.pprint(df)

# quit chrome web browser
browser1.quit()

