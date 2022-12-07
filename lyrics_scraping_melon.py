import selenium
from selenium import webdriver as wd
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from itertools import repeat
from selenium.webdriver.common.by import By

#open Chromedriver

driver = wd.Chrome('/chromedriver') #path
driver.maximize_window() #maximise the size of chrome window

#access to specific URL
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)


#Decade | Year
# 2020 - 1 | 2 - 1
# 2010 - 2 | 10 - 1
# 2000 - 3 | 5 - 1


def scraping(Decade, Year):

    result_df = pd.DataFrame()

    #select chart_finder
    driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/div/div/button/span').click()

    # Yearly Chart
    driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/h4[3]/a').click()
    time.sleep(2)

    # Select Decade (2000s)
    driver.find_element(By.XPATH, f'//*[@id="d_chart_search"]/div/div/div[1]/div[1]/ul/li[{Decade}]/span/label').click()
    time.sleep(2)

    # Select Year (2005 - (li[10]), 2009 - (li[1]))
    driver.find_element(By.XPATH, f'//*[@id="d_chart_search"]/div/div/div[2]/div[1]/ul/li[{Year}]/span/label').click()
    time.sleep(2)

    # Select Domestic Chart
    driver.find_element(By.XPATH, '//*[@id="d_chart_search"]/div/div/div[5]/div[1]/ul/li[2]/span/label').click()
    time.sleep(2)


    #Click 'Search'
    driver.find_element(By.XPATH, '//*[@id="d_srch_form"]/div[2]/button/span/span').click()


    #html
    html = driver.page_source #cf) requests.get(url)
    soup = BeautifulSoup(html, 'lxml')

    title_lst = [title.find('a').get_text() for title in soup.find_all('div', attrs={'class': 'ellipsis rank01'})]
    artist_lst = [singer.get_text() for singer in soup.find_all('span', attrs={'class':'checkEllipsis'})]

    rank_lst = []
    for i in range(len(title_lst)):
        rank_lst.append(i+1)

    year_ = soup.find_all('span', attrs={'class':'datelk'})[0].get_text()
    year_lst = list(repeat(soup.find_all('span', attrs={'class':'datelk'})[0].get_text(), len(title_lst)))


    df = pd.DataFrame({'YEAR':year_lst,'RANK':rank_lst,'TITLE':title_lst,'ARTIST':artist_lst})
    result_df = pd.concat([result_df, df], ignore_index=True)

    result_df.to_csv(f'melonchart_{year_}.csv') #글자 깨질 때 ,encoding='ANSI'
