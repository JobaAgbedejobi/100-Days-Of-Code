from selenium import webdriver
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# STEP 1: SETUP, CHROME PROFILE, AND BASIC NAVIGATION
ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

# Configure Selenium to stay open using the Chrome option:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Give Selenium it's own user profile. Have your script create a directory in your
# project folder to store your Chrome Profile information with:
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

# Tell your Chrome Driver to use the directory you specified to store a "profile". That
# way every time you quit Chrome and re-run your Selenium script, it keeps all the
# preferences and settings from your profile.
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

# Run Selenium and have it navigate to the gym website:
driver.get(GYM_URL)

# STEP 2: AUTOMATED LOGIN

# WebDriverWait is a class in the Selenium Python package that allows you to wait for
# a certain condition to be met before proceeding with the execution of your test or
# script. It is used to implement explicit waits, which are more efficient and reliable
# than implicit waits or hardcoded delays.
wait = WebDriverWait(driver, timeout=2)

# To use WebDriverWait, you need to create an instance of it, passing in the driver
# object and a timeout value (in seconds). You can then use the until() method to wait
# for a specific condition to be met.
# element = wait.until(EC.presence_of_element_located((By.ID, "my_element")))

join_button = driver.find_element(By.CLASS_NAME, "Home_heroButton__3eeI3")
join_button.click()
# Check if you're at the page to input your credentials
input_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input")))
if input_element.is_displayed() and input_element.is_enabled():

    email = driver.find_element(By.NAME, "email")
    password = driver.find_element(By.NAME, "password")

    email.send_keys(ACCOUNT_EMAIL)
    password.send_keys(ACCOUNT_PASSWORD)

    submit = driver.find_element(By.ID, "submit-button")
    submit.click()

wait.until(EC.presence_of_element_located((By.CLASS_NAME,
                                           "Schedule_scheduleTitle__zfZxg")))

# STEP 5: ADD COUNTERS
classes_booked = 0
waitlists_joined = 0
already_booked = 0

processed_list = []
# STEP 7: VERIFY CLASS BOOKINGS ON THE "MY BOOKINGS" PAGE
verified_list = []

# STEP 3: BOOK THE UPCOMING TUESDAY CLASS
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
for card in class_cards:
    day_group = card.find_element(By.XPATH,
                                  "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

# EXPLAINING THE XPATH:

# . :
# This represents the current element, which is the card element in this case.

# ancestor:: :
# This is an axis that navigates to the ancestors (parents) of the current element.
# The double colon :: is used to specify the axis.

# div :
# This is the element type that we're looking for. We're looking for a div element that
# is an ancestor of the card element.

# contains(@id, 'day-group-') :
# This is a predicate that filters the elements based on their id attribute. We're
# looking for a div element whose id attribute contains the string 'day-group-'. So,
# when we put it all together, ./ancestor::div[contains(@id, 'day-group-')] is saying:
# "Start from the current element (card), navigate up the DOM tree to find the nearest
# ancestor that is a div element and has an id attribute containing the string
# 'day-group-', and return that element."

    # Check if this is a Wednesday (I'm doing this part of code on a Tuesday past 6pm)
    # STEP 6: BOOK ALL WEDNESDAY AND FRIDAY 7PM SESSIONS (added 'or "Fri"')
    if "Wed" in day_title or "Fri" in day_title:
        # Check if this is a 7pm class
        time_text = (card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']")
                     .text)
        if "7:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.TAG_NAME, "h3").text
            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR,
                                       "button[id^='book-button-']")
            class_info = f"{class_name}: {day_title}"
            # STEP 4: CHECK IF A CLASS IS ALREADY BOOKED
            if button.text == "Booked":
                print(f"✅ Already Booked: {class_name}: {day_title}")
                already_booked += 1
                processed_list.append(f"[Booked] {class_info}")

            elif button.text == "Waitlisted":
                print(f"✅ Already on Waitlist: {class_name}: {day_title}")
                already_booked += 1
                processed_list.append(f"[Waitlisted] {class_info}")

            elif button.text == "Book Class":
                button.click()
                print(f"✅ Booked: {class_name}: {day_title}")
                classes_booked += 1
                processed_list.append(f"[New Booking] {class_info}")
                time.sleep(0.5)

            elif button.text == "Join Waitlist":
                button.click()
                print(f"✅ Joined Waitlist: {class_name}: {day_title}")
                waitlists_joined += 1
                processed_list.append(f"[New Waitlist] {class_info}")
                time.sleep(0.5)


# print("\n--- BOOKING SUMMARY ---"
#       f"\nClasses Booked: {classes_booked}"
#       f"\nWaitlists Joined: {waitlists_joined}"
#       f"\nAlready Booked/ Waitlisted: {already_booked}"
#       f"\nTotal 7pm Wednesday and Friday Classes Processed: "
#       f"{classes_booked + waitlists_joined + already_booked}")
#
# print("\n--- DETAILED CLASS LIST ---")
# for item in processed_list:
#     print(f"    ‣ {item}")

            bookings_section = driver.find_element(By.CSS_SELECTOR,
                                                   "#my-bookings-link")
            bookings_section.click()
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                       "confirmed-bookings-title"))
                       )

            # verified_bookings = len(driver.find_elements(By.CSS_SELECTOR,
            # "button[id^='cancel-booking-booking-]"))
            # verified_waitlists = len(driver.find_elements(By.CSS_SELECTOR,
            # "button[id^='leave-waitlist-waitlist-]"))

# verified_bookings = len(driver.find_elements(By.TAG_NAME, "button"))-1
            cancel_booking_btn = driver.find_element(By.CSS_SELECTOR,
                                                "button[id^='cancel-booking-']")
            cancel_waitlist_btn = driver.find_element(By.CSS_SELECTOR,
                                                "button[id^='leave-waitlist-']")
            if cancel_booking_btn.text == "Cancel Booking":
                verified_list.append(f"[Verified] {class_name}")

            elif cancel_waitlist_btn == "Leave Waitlist":
                verified_list.append(f"[Verified] {class_name} (Waitlist)")

print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
for item in verified_list:
    print(f" ✔️ {item}")

print("\n--- VERIFICATION RESULT ---"
      # f"\nExpected: {already_booked + waitlists_joined + classes_booked}"
      f"\nExpected: {len(processed_list)}"
      f"\nFound: {len(verified_list)}")
if len(processed_list) == len(verified_list):
    print("\n✅ SUCCESS: All bookings verified!")
else:
    print(f"\n❌ MISMATCH: Missing {len(processed_list)-len(verified_list)} bookings")
