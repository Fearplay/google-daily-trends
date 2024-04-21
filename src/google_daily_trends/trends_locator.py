from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Trends:
    def __init__(self):
        self.element = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details-wrapper.no-news')))
        self.date = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.content-header-title')))

    def haha(self):
        position_number = 0
        list_with_trends = []
        today_trends = []
        for ele in self.element:
            list_with_trends.append(ele.text.split('\n'))
        for trend in list_with_trends:
            trend.pop(-1)
            if "tis" in trend[-1]:
                trend[-1] = trend[-1].split(' ')
                trend[-1] = trend[-1][0].replace(trend[-1][0], f'{trend[-1][0]} 000+')
            elif "mil" in trend[-1]:
                trend[-1] = trend[-1].split(' ')
                trend[-1] = trend[-1][0].replace(trend[-1][0], f'{trend[-1][0]} 000 000+')
            if not self.get_daily_trends(trend, position_number, today_trends):
                break
            position_number += 1
        print(today_trends)

    def get_daily_trends(self, trend, count_number, list_with_today_trends):
        if count_number < int(trend[0]):
            list_with_today_trends.append(trend)
            print(trend)
            return True
        else:
            return False
