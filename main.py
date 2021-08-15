from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

# driver.find_element_by_css_selector('#page > div.Container-sc-1it4kq4.fZpcck > div.ActionPane-sc-mi4n8g.eVYXmg > div > button.sc-eCApnc.ciuTw').click()
# for i in driver.find_elements(By.CSS_SELECTOR, '#body > div:nth-child(2) > div > div.row > div.col-md-6 > div.ejocme-0.jDCUqL > div > div > a'):
#     try:
#         name = i.find_element_by_css_selector('h2')
#         NAME = name.text
#         name.click()
#         time.sleep(2)
#     except NoSuchElementException:
#         name=" "
#         pass
#     address = driver.find_element_by_css_selector('div.rg14')
#     ADDRESS = address.text
#     df = df.append({
#         'The attraction':NAME,
#         'Address':ADDRESS
#     }, ignore_index=True)
#     driver.back()
#     time.sleep(2)

PATH = './chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://scholar.google.com/")

df = pd.DataFrame()
#search page
search_box = driver.find_element_by_css_selector("#gs_hdr_tsi")
search_box.send_keys("Thammasat University\n")
tu = driver.find_element_by_css_selector('#gs_res_ccl_mid > div:nth-child(2) > div > a')
tu.click()

for i in driver.find_elements(By.CSS_SELECTOR, "div.gs_ai_t"):
    a = i.find_element_by_css_selector('a')
    author = a.text
    b = i.find_element_by_css_selector('div.gs_ai_aff')
    affliation = b.text
    df = df.append(
        {
            'author': author,
            'affiliation': affliation
        }, ignore_index=True
    )

df.to_csv('author.csv')