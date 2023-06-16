import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # Added to prevent closing of browser
driver = webdriver.Chrome(options=options)  # Creating object

driver.get('https://www.linkedin.com/jobs/search')

signin_button = driver.find_element(By.LINK_TEXT, 'Sign in')
signin_button.click()

email = driver.find_element(By.NAME, 'session_key')
email.send_keys(os.environ.get('EMAIL'))  # Typing
email.send_keys(Keys.TAB)
password = driver.find_element(By.NAME, 'session_password')
password.send_keys(os.environ.get('PASSWORD'))
signin = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
signin.click()

time.sleep(2)  # Sleep added to give time for searching elements, else we might have NoSuchElementException

all_jobs = driver.find_element(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in all_jobs:
    time.sleep(2)
    job.click()

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(os.environ.get('PHONE'))

        time.sleep(5)
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        submit_button.click()

        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("Button element not found.")
        continue

driver.quit()

