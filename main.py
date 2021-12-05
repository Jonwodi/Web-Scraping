import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

SERVICE = Service(ChromeDriverManager().install())
browser1 = webdriver.Chrome(service=SERVICE)
browser1.get("https://www.hyperoptic.com/offer/")


accept_cookies = browser1.find_element(
    By.XPATH, '//*[@id="cookiePolicyModal"]/div/div/div[3]/button[1]'
)
accept_cookies.click()

browser1.implicitly_wait(30)

deals = []
# deal name
deal_name = browser1.find_elements(By.CLASS_NAME, "size-unit",)
for name in deal_name:
    deals.append({"name": name.text})

# deal price
deal_prices = browser1.find_elements(By.CLASS_NAME, "price",)
for index, price in enumerate(deal_prices):
    deals[index]["price"] = price.text


# deal speed & setup cost
deal_speed_and_setup = browser1.find_elements(
    By.CLASS_NAME, "flat-text-bellow-price-wr",
)

for index, speed_and_cost in enumerate(deal_speed_and_setup):
    deals[index]["speed"] = speed_and_cost.text.splitlines()[1]
    deals[index]["setup cost"] = speed_and_cost.text.splitlines()[3]


# deal contract length
deal_contract_length = browser1.find_elements(
    By.CLASS_NAME, "bold-text-bellow-price-wr"
)
print("_____")
print("Deals")
print("_____")
for index, contract in enumerate(deal_contract_length):
    deals[index]["contract"] = contract.text


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(deals)
