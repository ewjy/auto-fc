from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import csv
################chrome_headless######################
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
#####################################################
get_title_and_href_dict = {}
for i in range(1,4,1):
    url = 'https://www.mygopen.com/search/label/%E8%AC%A0%E8%A8%80#archive-page-'+str(i)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.refresh()
    WebDriverWait(driver,10).until(lambda d: d.find_elements_by_css_selector('.item-content .item-title a'))
        # print(get_title_and_href_dict)
    with open('storage_mygopen.csv','a',encoding = 'utf-8',newline='')as csvfile:
        fieldNames = ['title','href']
        writer = csv.DictWriter(csvfile,fieldnames= fieldNames,dialect='excel')
        writer.writeheader()
        a_tag = driver.find_elements_by_css_selector('.item-content .item-title a')
        for j in range(len(a_tag)):
            get_title_and_href_dict.update({'title':a_tag[j].text,'href':a_tag[j].get_attribute('href')})
            writer.writerow(get_title_and_href_dict)