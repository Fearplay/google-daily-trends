from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Trends:
    def __init__(self):
        self.element = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details-wrapper.no-news')))
        self.date = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.content-header-title')))

    def haha(self):
        i = 0
        list_with_trends = []
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

            # trend[-1] = trend[-1].replace(trend[-1][0], '')
            # print(trend[-1][0])
        #     print(trend)
        #
        #     # trend.replace(0, "2")
        #
        print(list_with_trends)

    def datess(self):
        oks=[]
        for eme in self.date:
            oks.append(eme.text)
        print(oks)
