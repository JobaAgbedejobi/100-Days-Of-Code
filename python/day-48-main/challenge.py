from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://secure-retreat-92358.herokuapp.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

fname.send_keys("Joba", Keys.ENTER)
lname.send_keys("Agbedejobi", Keys.ENTER)
email.send_keys("your-email@example.com", Keys.ENTER)

sign_up_button = driver.find_element(By.CLASS_NAME, value="btn-block")
# OR
# sign_up_button = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up_button.click()