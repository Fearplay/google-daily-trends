import json

import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from src.google_daily_trends.trends_locator import Trends


class Utils(Trends):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.get_location())
        self.wait = WebDriverWait(self.driver, 10)
        Trends.__init__(self)

    def get_location(self):
        url = 'http://ipinfo.io/json'
        response = requests.get(url)
        data = json.loads(response.text)
        country_code = data['country']
        return f"https://trends.google.com/trends/trendingsearches/daily?geo={country_code}&hl=cs"

    def start_of_the_script(self):
        self.haha()
        self.driver_close()

    def driver_close(self):
        self.driver.close()
