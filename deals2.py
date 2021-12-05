from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser2 = webdriver.Chrome(service=service)
browser2.get("https://www.bt.com/products/broadband/deals")

browser2.implicitly_wait(30)

browser2.send_keys()
browser2.send_keys(Keys)

# accept_cookies = browser2.find_element(
#     By.XPATH, "/html/body/div[8]/div[1]/div/div[3]/a[1]"
# )

accept_cookies = browser2.find_elements(By.LINK_TEXT, "Accept all cookies")
# print(accept_cookies.text)
# accept_cookies.click()


# deal name
# deal price
# deal speed
# deal setup cost
# deal contract length
