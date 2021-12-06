import pprint

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser2 = webdriver.Chrome(service=service)
browser2.get("https://www.bt.com/products/broadband/deals")

# code used to switch from current_url into iframe element that contains accept cookies link
WebDriverWait(browser2, 10).until(
    EC.frame_to_be_available_and_switch_to_it(
        (By.XPATH, "/html/body/div[3]/div/iframe")
    )
)

# code used to click on accept cookies link that is within iframe element
WebDriverWait(browser2, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div[1]/div/div[3]/a[1]"))
).click()

# code used to exit iframe element to main body html element
browser2.switch_to.default_content()


# code used to locate postcode search input box
form_postcode_input = browser2.find_element(
    By.XPATH,
    "/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div/form/div/div/input",
)

# code used to enter postcode
form_postcode_input.send_keys("SE18 1EH")

# code used to find form submit button
form_btn = browser2.find_element(
    By.XPATH,
    "/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div/form/div/button",
)

# code used to click on postcode form submit button
form_btn.click()


# problem not resolved
# dropdown_select = browser2.find_element(By.CLASS_NAME, "jss1970")
dropdown_select = WebDriverWait(browser2, 10).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/form/div[1]/div/select",
        )
    )
)
dropdown_select = Select(dropdown_select)
dropdown_select.select_by_visible_text("101 Brookdene Road, Woolwich, London, SE18 1EH")

WebDriverWait(browser2, 20).until(
    EC.invisibility_of_element((By.CSS_SELECTOR, "div.loadingWhiteBox"))
)

select_form_btn = WebDriverWait(browser2, 10).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "/html/body/div[1]/div[2]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/form/div[2]/button",
        )
    )
)
# select_form_btn.click()
# select_form_btn.send_keys(Keys.RETURN)


deals2 = []

# deal name
deal_name2 = browser2.find_element(By.LINK_TEXT, "Fibre Essential ",)
for name2 in deal_name2:
    print(name2.text)
# for name2 in deal_name2:
#     deals2.append({"deal name": name2.text})

# deal price
# deal_prices = browser2.find_elements(By.CLASS_NAME, "price",)
# for index, price in enumerate(deal_prices):
#     deals2[index]["deal price"] = price.text


# deal speed & setup cost
# deal_speed_and_setup = browser2.find_elements(
#     By.CLASS_NAME, "flat-text-bellow-price-wr",
# )

# for index, speed_and_cost in enumerate(deal_speed_and_setup):
#     deals2[index]["deal speed"] = speed_and_cost.text.splitlines()[1]
#     deals2[index]["deal setup cost"] = speed_and_cost.text.splitlines()[3]


# deal contract length
# deal_contract_length = browser2.find_elements(
#     By.CLASS_NAME, "bold-text-bellow-price-wr"
# )
# print("_____")
# print("Deals")
# print("_____")
# for index, contract in enumerate(deal_contract_length):
#     deals2[index]["deal contract"] = contract.text

# deal_speed2 = browser2.find_elements(
#     By.XPATH,
#     "/html/body/div[1]/div[2]/div[4]/div[2]/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]/div/div/span",
# )
# for index, speed2 in enumerate(deal_speed2):
#     deals2[index]["deal speed"] = speed2.text

pp = pprint.PrettyPrinter(indent=5)
pp.pprint(deals2)
# browser2.quit()

browser2.implicitly_wait(10)

