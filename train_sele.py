
# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd
import requests
"""
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://shifucon.ppihgroup.com/staffpage/')
print(driver)
elemname = driver.find_element_by_id("login_email")
elemname.send_keys('0167938')
elemname = driver.find_element_by_id("login_pass")
elemname.send_keys('3104chalo')
log_in = driver.find_element_by_class_name('btn btn-lg btn-primary btn-block')
log_in.click()
"""
def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #options.add_argument('--disable-features=VizDisplayCompositor')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    browser.get("https://scraping-for-beginner.herokuapp.com/login_page")
    username = browser.find_element_by_id('username')
    username.send_keys("imanishi")
    userpass = browser.find_element_by_id('password')
    userpass.send_keys("ki")
    log_in = browser.find_element_by_id('login-btn')
    log_in.click()
    NAME = browser.find_element_by_id("name")
    print("名前:", NAME.text)
    COM = browser.find_element_by_id("company")
    print("所属企業:", COM.text)
    birthday = browser.find_element_by_id("birthday")
    print("生年月日:", birthday.text)
    birthplace = browser.find_element_by_id("come_from")
    print("出身地：", birthplace.text)
    hobby = browser.find_element_by_id("hobby")
    print("趣味：", hobby.text)
    #要素一つ
    elemth = browser.find_element_by_tag_name("th")
    #要素複数
    elemth = browser.find_elements_by_tag_name("th")
    print(elemth[0].text)
    key = []
    for i in elemth:
        key.append(i.text)
    value = []
    elemtd = browser.find_elements_by_tag_name("td")
    for i in elemtd:
        value.append(i.text)
    sleep(5)
    browser.quit()
    df = pd.DataFrame()
    df["項目"] = key
    df["値"] = value
    print(df)
    df.to_csv("講師情報.csv", index = False)
    

if __name__ == '__main__':
    main()
