from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

PATH = './chromedriver'
driver = webdriver.Chrome(PATH)
driver.get("https://www.wongnai.com/attractions?regions=5322")

df = pd.DataFrame()
length = len(driver.find_elements(By.CSS_SELECTOR, '#body > div:nth-child(2) > div > div.row > div.col-md-6 > div.ejocme-0.jDCUqL > div > div > a'))
print(length)
for i in range(length):
    try:
        data = driver.find_element_by_css_selector('#body > div:nth-child(2) > div > div.row > div.col-md-6 > div.ejocme-0.jDCUqL > div > div > a')
        name = data[i].find_element_by_css_selector('h2')
        NAME = name.text
        print(NAME)
        name.click()
        time.sleep(2)
    except NoSuchElementException:
        name=" "
        pass
    address = driver.find_element_by_css_selector('#body > div.content.noSidePadding > div.iowx8b-0.jqBVFb.row > div.iowx8b-3.btqpuE.col-md-8 > div:nth-child(5) > div > div > div > div.ba60x6-1.eTmqOK.mt-8-mWeb > div.text-gray-700 > div > div > span > div')
    ADDRESS = address.text
    print(ADDRESS)
    try:
        phone = driver.find_element_by_css_selector('#body > div.content.noSidePadding > div.iowx8b-0.jqBVFb.row > div.iowx8b-3.btqpuE.col-md-8 > div:nth-child(5) > div > div > div > div.ba60x6-1.eTmqOK.mt-8-mWeb > div:nth-child(5) > div > div > div > span')
        PHONE = phone.text.split(":")[-1]
        print(PHONE)
    except NoSuchElementException:
        PHONE=" "
        pass
    df = df.append({
        'The attraction': NAME,
        'Phone': PHONE,
        'Address': ADDRESS
    }, ignore_index=True)
    driver.back()
    time.sleep(2)

df.to_csv('Yala.csv')