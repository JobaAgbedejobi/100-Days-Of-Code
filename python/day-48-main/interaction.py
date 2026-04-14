from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# To get "7,043,093" articles in English from the wiki homepage, could use this method,
# but could also use XPATH
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount")
print(article_count.text.split()[3])

all_portals = driver.find_element(By.LINK_TEXT, value="Content Portals")
all_portals.click()

search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)

driver.quit()