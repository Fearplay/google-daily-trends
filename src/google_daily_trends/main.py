from src.google_daily_trends.utils import Utils

utils = Utils()

if __name__ == '__main__':
    utils.start_of_the_script()


# import json
#
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# url = 'http://ipinfo.io/json'
# response = requests.get(url)
# data = json.loads(response.text)
# country_code = data['country']
# list_with_trends = []
# driver.get(f"https://trends.google.com/trends/trendingsearches/daily?geo={country_code}&hl=cs")
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.details-wrapper.no-news')))
# i = 0
# for ele in element:
#     list_with_trends.append(ele.text.split('\n'))
# for trend in list_with_trends:
#     trend.pop(-1)
#     if "tis" in trend[-1]:
#         trend[-1] = trend[-1].replace(trend[-1], '')
#         print(trend)
#
#     # trend.replace(0, "2")
#
# print(list_with_trends)
#
# driver.close()
