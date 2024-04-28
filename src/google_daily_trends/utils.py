import json
import time

import requests
from selenium import webdriver
from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.google_daily_trends.trends_locator import Trends


class Utils(Trends):
    def __init__(self):

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.driver.get(self.get_location())
        self.wait = WebDriverWait(self.driver, 5)
        Trends.__init__(self)

    @staticmethod
    def get_location():
        url = 'https://ipinfo.io/json'
        response = requests.get(url)
        data = json.loads(response.text)
        country_code = data['country']
        return f"https://trends.google.com/trends/trendingsearches/daily?geo={country_code}&hl=cs"

    def start_of_the_script(self):
        self.fill_trends()

    def driver_close(self):
        self.driver.close()

    def wait_for_element(self, located_by, path, clickable=None, send_text=None, clearable=None, wait_time=None):

        force_click_element = self.wait.until(EC.presence_of_element_located((located_by, path)))
        try:
            unhidden_element = self.wait.until(EC.presence_of_element_located((located_by, path)))
            if clickable:
                unhidden_element.click()
            if clearable:
                unhidden_element.clear()
            if send_text:
                if wait_time:
                    time.sleep(wait_time)
                unhidden_element.send_keys(send_text)
            if wait_time:
                time.sleep(wait_time)
        except TimeoutException:
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", force_click_element)
        except WebDriverException:
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", force_click_element)

    @staticmethod
    def is_element_present(web_driver, located_by, path, timeout=2):
        try:
            WebDriverWait(web_driver, timeout).until(EC.presence_of_element_located((located_by, path)))
            return True
        except TimeoutException:
            return False
