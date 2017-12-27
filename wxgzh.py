#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import json
def log_in():
    js = {}
    account = input("Please input account:")
    password = input("Please input password:")
    web = webdriver.Chrome()
    web.get("https://mp.weixin.qq.com/")
    web.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').send_keys(account)
    time.sleep(3)
    web.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').send_keys(password)
    time.sleep(3)
    web.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[3]/label/i').click()
    time.sleep(3)
    web.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[4]/a').click()
    time.sleep(15)
    web.get("https://mp.weixin.qq.com/")
    cookies =  web.get_cookies()
    for cookie in cookies:
        js[cookie['name']] = cookie['value']
    str_cookies = json.dumps(js)
    print (str_cookies)
if __name__ == '__main__':
    log_in()
