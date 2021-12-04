from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser1 = webdriver.Chrome(service=service)
browser1.get("https://www.hyperoptic.com/offer/")


accept_cookies = browser1.find_element(
    By.XPATH, '//*[@id="cookiePolicyModal"]/div/div/div[3]/button[1]'
)

accept_cookies.click()

# browser1.find_elements(By.CLASS_NAME, "no-bottom-borders").click()
# browser1.find_elements(
#     By.XPATH, '//*[@id="block_61711b89d05de"]/div/div[6]/div[1]/div/div/div[2]/div[2]/i'
# ).click()


browser1.implicitly_wait(10)

# deal name
deal_name = browser1.find_elements(By.CLASS_NAME, "size-unit",)
print("Deal name")
print("_________")
for name in deal_name:
    print(name.text + " " + "deal")

# deal price
deal_price = browser1.find_elements(By.CLASS_NAME, "price",)
print("Deal price")
print("_________")
for price in deal_price:
    print(price.text + " " + "per month")


# deal speed
deal_speed = browser1.find_elements(By.CLASS_NAME, "font-f-museo-500",)
print("Deal speed")
print("_________")
for speed in deal_speed:
    print(speed.text)

# print(deal_name[0].get_attribute("value"))


# deal setup cost
deal_setup_cost = browser1.find_elements(By.CLASS_NAME, "font-f-museo-500",)
print("Deal setup cost")
print("_________")
for cost in deal_setup_cost:
    print(cost.text)
# deal contract length


# deals = [
#     [browser1.find_elements(By.CLASS_NAME, "size-unit",)],
#     [browser1.find_elements(By.CLASS_NAME, "price",)],
# ]
# for deal in deals:
#     print(deal.text)
