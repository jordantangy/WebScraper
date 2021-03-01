import bs4
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver
import time as t

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.imdb.com')


data = pd.read_csv('duplicate_free_41K.csv')
truncat = data[:30000]
truncat = truncat.to_numpy()


plots = []
for i in range(len(truncat)):
    movie_name = truncat[i][2]
    query = movie_name
    search = driver.find_element_by_xpath("""//*[@id="suggestion-search"]""")
    search.send_keys(query)
    driver.find_element_by_css_selector("""#suggestion-search-button > svg""").click()
    driver.find_element_by_xpath("""//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a""").click()
    driver.find_element_by_xpath('//*[@id="title-overview-widget"]/div[2]/div[2]/div[1]/div[1]/div/div[1]/div/div/a').click()
    driver.find_element_by_xpath('// *[ @ id = "summary-ps0628196"] / p')
    t.sleep(10)




