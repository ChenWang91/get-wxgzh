#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import time
def log_in():
    account = raw_input("Please input account:")
    password = raw_input("Please input password:")
    web = webdriver.Chrome()
    web.get("https://mp.weixin.qq.com/")
    web.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').send_keys(account)
    time.sleep(3)
    web.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').send_keys(password)
    time.sleep(3)
    web.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[4]/a').click()

if __name__ == '__main__':
    log_in()
