from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.google_daily_trends.chart import BarData


class Trends(BarData):
    def __init__(self):
        BarData.__init__(self)
        self.element = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details-wrapper.no-news')))
        self.date = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.content-header-title')))

    def haha(self):
        position_number = 0
        list_with_trends = []
        today_trends = []
        name_of_the_trends = []
        numbers_of_the_trends = []
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
            position_number += 1
        self.driver.close()
        self.visualize_data(name_of_the_trends, numbers_of_the_trends)

    def get_daily_trends(self, trend, count_number, list_with_today_trends):
        if count_number < int(trend[0]):
            list_with_today_trends.append(trend)
            print(trend)
            return True
        else:
            return False

    def get_trend_name(self, trend, list_with_trend_names):
        return list_with_trend_names.append(trend[1])

    def get_trend_search_number(self, trend, list_with_trend_numbers):
        return list_with_trend_numbers.append(trend[2])
