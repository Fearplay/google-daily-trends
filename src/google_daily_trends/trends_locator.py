from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from src.google_daily_trends.bar_charts import BarData


class Trends(BarData):
    def __init__(self):
        BarData.__init__(self)
        self.element = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details-wrapper.no-news')))
        self.date = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.content-header-title')))
        self.WARNING = '\033[93m'
        self.END_COLOR = '\033[0m'

    def fill_trends(self):
        position_number = 0
        list_with_trends = []
        today_trends = []
        name_of_the_trends = []
        numbers_of_the_trends = []
        urls_of_the_trends = []
        for ele in self.element:
            list_with_trends.append(ele.text.split('\n'))
        for trend in list_with_trends:
            trend.pop(-1)
            if "tis" in trend[-1]:
                trend[-1] = trend[-1].split(' ')
                trend[-1] = trend[-1][0].replace(trend[-1][0], f'{trend[-1][0]}000+')
            elif "mil" in trend[-1]:
                trend[-1] = trend[-1].split(' ')
                trend[-1] = trend[-1][0].replace(trend[-1][0], f'{trend[-1][0]}000000+')
            if not self.get_daily_trends(trend, position_number, today_trends):
                break
            self.get_trend_name(trend, name_of_the_trends)
            self.get_trend_search_number(trend, numbers_of_the_trends)
            self.get_trend_event_info(trend, urls_of_the_trends)
            position_number += 1
        self.driver.quit()
        self.visualize_data(name_of_the_trends, numbers_of_the_trends, urls_of_the_trends)

    @staticmethod
    def get_daily_trends(trend, count_number, list_with_today_trends):
        if count_number < int(trend[0]):
            list_with_today_trends.append(trend)
            return True
        else:
            return False

    @staticmethod
    def get_trend_name(trend, list_with_trend_names):
        return list_with_trend_names.append(trend[1])

    @staticmethod
    def get_trend_search_number(trend, list_with_trend_numbers):
        return list_with_trend_numbers.append(trend[2])

    def get_trend_event_info(self, trend, list_with_trend_info):
        print(f'{self.WARNING}Please wait generating info about events!{self.END_COLOR}')
        self.driver.switch_to.new_window()
        self.driver.get('https://www.google.com/')
        if self.is_element_present(web_driver=self.driver, located_by=By.ID, path="W0wltc"):
            self.wait_for_element(located_by=By.ID, path="W0wltc", clickable=True)
        self.wait_for_element(located_by=By.CSS_SELECTOR, path=".gLFyf", clickable=True, send_text=(f"{trend[1]}", Keys.RETURN))
        self.wait_for_element(located_by=By.XPATH, path='//a[contains(@href, "/search") and contains(@href, "tbm=nws")]', clickable=True)
        return list_with_trend_info.append(self.driver.current_url)
