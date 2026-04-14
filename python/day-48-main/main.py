from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

times = driver.find_elements(By.CSS_SELECTOR, value=".last .menu time")
names = driver.find_elements(By.CSS_SELECTOR, value=".last .menu a")
for item in names:
    name = [item.text for item in names[9:14]]

# GOT HELP FOR MAKING THIS NESTED DICTIONARY
events = {}

for n in range(len(times)):
    events[n] = {
        "time": times[n].text,
        "name": name[n],
}
print(events)


driver.quit()