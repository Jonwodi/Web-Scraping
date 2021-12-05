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

# deal name
deal_name = browser1.find_elements(By.CLASS_NAME, "size-unit",)
print("_________")
print("Deal name")
print("_________")
for name in deal_name:
    print(name.text + " " + "deal\n")

# deal price
deal_price = browser1.find_elements(By.CLASS_NAME, "price",)
print("__________")
print("Deal price")
print("__________")
for price in deal_price:
    print(price.text + " " + "per month\n")


# deal speed & setup cost
deal_speed_and_setup = browser1.find_elements(
    By.CLASS_NAME, "flat-text-bellow-price-wr",
)
print("_______________________")
print("Deal speed & setup cost")
print("_______________________")
for speed_and_cost in deal_speed_and_setup:
    print(speed_and_cost.text + "\n")


# deal contract length
deal_contract_length = browser1.find_elements(
    By.XPATH, '//*[@id="block_61711b89d05de"]/div/div[3]/div/div[2]/div[1]/label[1]'
)
print("____________________")
print("Deal contract length")
print("____________________")
for contract_length in deal_contract_length:
    e = 1
    while e <= 4:
        print(contract_length.text + "\n")
        e += 1

