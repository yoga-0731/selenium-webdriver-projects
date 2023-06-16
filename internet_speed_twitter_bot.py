import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

OFFERED_UPLOAD_SPEED = 0.5
OFFERED_DOWNLOAD_SPEED = 2
TWITTER_USERNAME = os.environ.get('TWITTER_USERNAME')
TWITTER_PASSWORD = os.environ.get('PASSWORD')


class InternetSpeedTwitterBot:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.maximize_window()
        self.upload_speed = 0
        self.download_speed = 0

    def check_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        test_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a .start-text")
        test_button.click()
        time.sleep(90)
        self.download_speed = float(self.driver.find_element(By.CSS_SELECTOR, ".result-container-data .result-item-download .result-data span").text)
        self.upload_speed = float(self.driver.find_element(By.CSS_SELECTOR, ".result-container-data .result-item-upload .result-data span").text)
        # print(self.download_speed, self.upload_speed)

    def tweet_internet_provider(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(5)
        self.login_to_twitter()
        if self.download_speed < OFFERED_DOWNLOAD_SPEED or self.upload_speed < OFFERED_UPLOAD_SPEED:
            tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweet_field.click()
            text = f"Hello, Internet Service Provider! The internet speed is slower than the agreed speed of {OFFERED_UPLOAD_SPEED} and {OFFERED_DOWNLOAD_SPEED}."
            tweet_field.send_keys(text)
            time.sleep(5)
            tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div')
            tweet_button.click()

    def login_to_twitter(self):
        time.sleep(5)
        username = self.driver.find_element(By.NAME, 'text')
        username.click()
        username.send_keys(TWITTER_USERNAME)
        time.sleep(10)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next_button.click()
        time.sleep(10)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(TWITTER_USERNAME)
        time.sleep(10)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        next_button.click()
        time.sleep(10)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(10)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        login_button.click()
