import pprint

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser2 = webdriver.Chrome(service=service)

# get website url
browser2.get("https://www.bt.com/products/broadband/deals")

# switch from main document body into iframe document body
iframe = WebDriverWait(browser2, 10).until(
    EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, "/html/body/div[3]/div/iframe")
    )
)

# locate accept cookies link that is within iframe element and click on it
accept_cookies = (
    WebDriverWait(browser2, 10)
    .until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[8]/div[1]/div/div[3]/a[1]")
        )
    )
    .click()
)

# exit iframe document body into orginal website document body
browser2.switch_to.default_content()


# locate postcode search input field box
form_postcode_input = browser2.find_element(
    By.XPATH,
    "/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div/form/div/div/input",
)

# enter postcode into search input field box
form_postcode_input.send_keys("SE18 1EH")

# locate postcode search submit button
postcode_form_btn = browser2.find_element(
    By.XPATH,
    "/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div/form/div/button",
)

# submit postcode form / click postcode search button
postcode_form_btn.click()


dropdown_select = WebDriverWait(browser2, 20).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/form/div[1]/div/select",
        )
    )
)

# select address dropdown
dropdown_select = Select(dropdown_select)

# click on / select this address
dropdown_select.select_by_visible_text("101 Brookdene Road, Woolwich, London, SE18 1EH")


# locate address submit form button
select_form_btn = WebDriverWait(browser2, 20).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/form/div[2]/button",
        )
    )
)

# submit address form
select_form_btn.click()


browser2.implicitly_wait(10)

# locate pop up box
# close_popup = WebDriverWait(browser2, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "closeChatInvite",))
# )

# close pop box
# close_popup.click()

browser2.implicitly_wait(40)

# empty list used to add deal data
deals2 = []

# deal name
deal_name2 = browser2.find_elements(By.ID, "product-name",)
for name2 in deal_name2:
    deals2.append({"deal name": name2.text})


# deal price
deal_prices = browser2.find_elements(By.ID, "product-price",)
for index, price in enumerate(deal_prices):
    deals2[index]["deal price"] = price.text


# deal setup cost
deal_setup_cost = browser2.find_elements(By.ID, "upfront-cost",)
for index, setup in enumerate(deal_setup_cost):
    deals2[0]["deal setup cost"] = setup.text
deal_setup_cost2 = browser2.find_elements(By.ID, "upfront-section",)
for index, setup in enumerate(deal_setup_cost2):
    deals2[1]["deal setup cost"] = setup.text


# deal contract length
deal_contract_length = browser2.find_elements(By.ID, "contract-length")
for index, contract in enumerate(deal_contract_length):
    deals2[index]["deal contract"] = contract.text

print("_______________________")
print("BT Broadband only deals")
print("_______________________")

# deal speed
deal_speed1 = browser2.find_elements(By.CLASS_NAME, "jss896",)
for index, speed1 in enumerate(deal_speed1):
    deals2[index]["deal speed"] = speed1.text


pp = pprint.PrettyPrinter(indent=5)
pp.pprint(deals2)
print("\n")
df = pd.DataFrame(deals2)
pp.pprint(df)
browser2.quit()
