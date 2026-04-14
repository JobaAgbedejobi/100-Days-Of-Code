from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://ozh.github.io/cookieclicker/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.ID, value="bigCookie")
cookie.click()

interval = 5.0
next_print = time.monotonic() + interval # first print will happen ~5s from now
end_min = 60
end_time = 5
END = end_min*end_time
start = time.monotonic()

# INITIAL TRY AT TRYING TO GET THE PRODUCT NAMES AND PRICES INTO A DICTIONARY
# for n in range(0,11):
#     item_name = [(driver.find_element(By.CSS_SELECTOR, value=f"#product{n} .title").
#     text
#                  .strip())]
#     item_price = [(driver.find_element(By.CSS_SELECTOR, value=f"#product{n} .price")
#     .text
#                   .strip())]
# print(item_name)
# print(item_price)
#     shop_dict = {
#         item_name[n]: item_price[n]
#     }
#
# print(shop_dict)


# window_running = True
# while window_running:
#     cookie.click() # keep clicking as fast as possible
#     now = time.monotonic() # current monotonic time (wall-clock style, steady)
#     if time.monotonic() >= next_print:
#         # Read the counter text like "1,234 cookies"
#         cookies_amount = driver.find_element(By.ID, value="cookies").text.strip()
#         # Extract the number part and strip thousands separators
#         amount = int(cookies_amount.split()[0].replace(",",""))
#
#         all_shop_item_names = driver.find_elements(By.CSS_SELECTOR, value="#products .title")
#         all_shop_item_prices = driver.find_elements(By.CSS_SELECTOR, value="#products .price")
#
#         product_names_list = [item.text for item in all_shop_item_names]
#         product_price_list = [int(item.text.replace(",", "")) for item in
#                               all_shop_item_prices]
#
#         shop_dict = {
#             "Products": product_names_list,
#             "Prices": product_price_list
#         }
#
#         for n in range(len(shop_dict["Prices"])-1, -1, -1):
#             price = shop_dict["Prices"][n]
#             if amount >= price:
#                 all_shop_item_names[n].click()
#                 print(f"I bought {product_names_list[n]}!")
#                 break

# HERE IS THE RESPONSE MY OWN WORK PRODUCED:
# I bought Cursor!
# I bought 4!
# I bought 5!
# I bought 6!
# I bought 7!
# I bought 8!
# I bought 9!
# I bought 10!

# I GAVE UP, HERE IS THE SOLUTION CODE BASED ON MY WORK UP UNTIL NOW:
while True:
    cookie.click()

    now = time.monotonic()
    if now >= next_print:
        # Find products that are currently buyable (enabled)
        products = driver.find_elements(By.CSS_SELECTOR, "#products .product")
        enabled = [p for p in products if "enabled" in p.get_attribute("class")]

        if enabled:
            # The last enabled product is the most expensive currently affordable
            candidate = enabled[-1]
            name = candidate.find_element(By.CSS_SELECTOR, ".title").text
            price_text = candidate.find_element(By.CSS_SELECTOR, ".price").text
            candidate.click()
            print(f"Bought {name} for {price_text}")
        missed = int((now - next_print) // interval) + 1
        next_print += missed * interval

    if now >= END:
        cookies = driver.find_element(By.CSS_SELECTOR, value="#cookies")
        cookies_text = cookies.text.split()[5]
        print(f"Session ended. Cookies/Second: {cookies_text}")
        driver.quit()


# What the variable 'missed' does (Although strictly unnecessary):
# When the loop runs late, more than one 5-second interval might have passed since
# next_print.
# delta = now - next_print is how late we are (in seconds).
# Adding 1 moves next_print to the first tick strictly after now, keeping a steady
# cadence.
# Example: interval=5
    # If we’re 0.2s late: delta=0.2 → 0.2 // 5 = 0 → missed = 1 → advance by 5s.
    # If we’re 7.4s late: delta=7.4 → 7.4 // 5 = 1 → missed = 2 → advance by 10s.
