import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

SERVICE = Service(ChromeDriverManager().install())
browser1 = webdriver.Chrome(service=SERVICE)

# getting url of website being scraped
browser1.get("https://www.hyperoptic.com/offer/")

# code used to find accept cookies button using xpath
accept_cookies = browser1.find_element(
    By.XPATH, '//*[@id="cookiePolicyModal"]/div/div/div[3]/button[1]'
)

# click function used to click on accept cookies button
accept_cookies.click()

# code used to allow webdriver to allow continue search for elements in seconds before element is found or  a NoSuchElementException error is thrown.
browser1.implicitly_wait(30)

# empty list where all data, scraped from the web is added into
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


# deal contract length
deal_contract_length = browser1.find_elements(
    By.CLASS_NAME, "bold-text-bellow-price-wr"
)


print("_____")
print("Deals")
print("_____")
for index, contract in enumerate(deal_contract_length):
    deals[index]["deal contract"] = contract.text

# code used to print the deals list and its data in more json like structure
pp = pprint.PrettyPrinter(indent=5)
pp.pprint(deals)

# code used to quit browser / close chrome web browser
browser1.quit()
