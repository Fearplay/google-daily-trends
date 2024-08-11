import re

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from src.google_daily_trends.bar_charts import BarData


class Trends(BarData):
    def __init__(self):
        BarData.__init__(self)
        self.event_name = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.mZ3RIc')))
        self.event_views = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.lqv0Cb')))
        self.WARNING = '\033[93m'
        self.END_COLOR = '\033[0m'
        self.name_of_the_trends = []
        self.numbers_of_the_trends = []
        self.urls_of_the_trends = []
        self.list_with_trends = []
        self.today_trends = []
        self.watcher = []
        self.duplicate_trends_list = []
        self.position_number = 0
        self.end_of_the_numbers_of_trends = 10

    def split_trend_views(self):
        for trend in self.watcher:
            splitter_of_the_views = re.split('[ .+]+', trend)
            splitter_of_the_views.pop(-1)
            print(splitter_of_the_views)
            if "tis" in splitter_of_the_views[-1]:
                splitter_of_the_views = splitter_of_the_views[0] + splitter_of_the_views[-1].replace(splitter_of_the_views[-1], f'000+')
            elif "mil" in splitter_of_the_views[-1]:
                splitter_of_the_views = splitter_of_the_views[0] + splitter_of_the_views[-1].replace(splitter_of_the_views[-1], f'000000+')
                print(splitter_of_the_views)
            else:
                splitter_of_the_views = splitter_of_the_views[0] + "+"
            self.numbers_of_the_trends.append(splitter_of_the_views)

    def trend_if_not_timeout_error(self):
        for trend_name in self.name_of_the_trends:
            if not self.get_daily_trends(self.position_number):
                break
            self.get_trend_event_info(self.urls_of_the_trends)
            self.split_trend_views()
            self.duplicate_trends_list.append(trend_name)
        self.driver.quit()
        self.visualize_data_with_urls(self.name_of_the_trends, self.numbers_of_the_trends, self.urls_of_the_trends)

    def trend_if_timeout_error(self):
        for trend_name in self.name_of_the_trends:
            if trend_name not in self.duplicate_trends_list:
                if not self.get_daily_trends(self.position_number):
                    break
                self.split_trend_views()
        self.driver.quit()
        self.visualize_data_without_urls(self.name_of_the_trends, self.numbers_of_the_trends)

    def fill_trends(self):
        try:
            for name, watcher in zip(self.event_name, self.event_views):
                if len(self.name_of_the_trends) < self.end_of_the_numbers_of_trends:
                    self.watcher.append(watcher.text)
                    self.name_of_the_trends.append(name.text)
            self.trend_if_not_timeout_error()
        except TimeoutException:
            self.trend_if_timeout_error()

    def get_daily_trends(self, count_number):
        if count_number < self.end_of_the_numbers_of_trends:
            return True
        else:
            return False

    def get_trend_event_info(self, list_with_trend_info):
        for name in self.name_of_the_trends:
            if not self.get_daily_trends(self.position_number):
                break
            print(f'{self.WARNING}Please wait generating info about events!{self.END_COLOR}')
            self.driver.switch_to.new_window()
            self.driver.get('https://www.google.com/')
            if self.is_element_present(web_driver=self.driver, located_by=By.ID, path="W0wltc"):
                self.wait_for_element(located_by=By.ID, path="W0wltc", clickable=True)
            self.wait_for_element(located_by=By.CSS_SELECTOR, path=".gLFyf", clickable=True, send_text=(f"{name}", Keys.RETURN))
            self.wait_for_element(located_by=By.XPATH, path='//a[contains(@href, "/search") and contains(@href, "tbm=nws")]', clickable=True)
            list_with_trend_info.append(self.driver.current_url)
            self.position_number += 1
        return list_with_trend_info
