import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assuming you have downloaded the appropriate WebDriver for your browser
# and placed it in the system PATH or provided the path to the executable.
driver = webdriver.Chrome()

# Open the TikTok signup page
driver.get('https://www.tiktok.com/signup')

# Find the element by its text
target_text = "Use phone or email"
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{target_text}')]"))
)

# Capture the text before clicking
element_text = element.text.strip()

# Click on the element
element.click()

# Wait for the element to be present in the DOM
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{target_text}')]")))

# Find the 'DivAgeSelector' based on the presence of the text "Month"
print("Finding the DivAgeSelector")
div_age_selector = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Month')]/ancestor::div[contains(@class, 'DivAgeSelector')]"))
)

# Click on the month element
print("Clicking on the month element")
month_element = div_age_selector.find_element(By.XPATH, ".//div[contains(text(), 'Month')]")
month_element.click()

# Wait for the list box to be present
list_box_month = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, ".//*[@role='listbox']"))
)

# Get all available options in the list box
options_month = list_box_month.find_elements(By.XPATH, ".//div[@role='option']")

# Select a random option for the month
random_option_month = random.choice(options_month)
random_option_month.click()

# Click on the day element
print("Clicking on the day element")
day_element = div_age_selector.find_element(By.XPATH, ".//div[contains(text(), 'Day')]")
day_element.click()

# Wait for the day options to be present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[starts-with(@id, 'Day-options-item-')]")))

# Get all available options in the list box for the day
options_day = driver.find_elements(By.XPATH, ".//*[starts-with(@id, 'Day-options-item-')]")  # Adjust the XPath

# Select a random option for the day
random_option_day = random.choice(options_day)
random_option_day.click()

# Click on the year element
print("Clicking on the year element")
year_element = div_age_selector.find_element(By.XPATH, ".//div[contains(text(), 'Year')]")
year_element.click()

# Wait for the year options to be present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//*[starts-with(@id, 'Year-options-item-')]")))

# Get all available options in the list box for the year
options_year = driver.find_elements(By.XPATH, ".//*[starts-with(@id, 'Year-options-item-')]")  # Adjust the XPath

# Select a random year between 1960 and 2004 (inclusive)
random_year = random.randint(1960, 2004)
year_xpath = f".//*[starts-with(@id, 'Year-options-item-{2022 - random_year}')]"
random_option_year = driver.find_element(By.XPATH, year_xpath)
random_option_year.click()


# Click on the "Sign up with email" link
print("Clicking on the 'Sign up with email' link")
signup_with_email_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign up with email')]"))
)
signup_with_email_link.click()


# Wait for the email input to be present
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='email' and @placeholder='Email address']"))
)

# Replace 'your_email@gmail.com' with the desired email
email_input.send_keys('test_mail@anyhost.com')

# Wait for the password input to be present
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
)

# Replace 'your_password' with the desired password
password_input.send_keys('Password!')


# Locate and click the "Send code" button
send_code_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@data-e2e='send-code-button']"))
)
send_code_button.click()

# Wait for the input field for the 6-digit code to be present
code_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter 6-digit code']"))
)

# Simulate a delay to allow time for the code to be received (replace this with your actual waiting logic)
time.sleep(10)

# Replace 'your_6_digit_code' with the actual 6-digit code received in the email
received_code = 'your_6_digit_code'
code_input.send_keys(received_code)

# Continue with the next steps

# Display a waiting message
print("Waiting for a while...")
time.sleep(120)  # Wait for 60 seconds (adjust the duration as needed)

# Close the browser window
driver.quit()
