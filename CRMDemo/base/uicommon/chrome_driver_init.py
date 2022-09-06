#!/usr/bin/
# -*- coding: UTF-8 -*-
from base.uicommon.global_logger import *
from base.uicommon.global_property import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def start_chrome_driver():
    logger.info("打开chrome浏览器")
    chrome_driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir,"config","chromedriver.exe"))
    chrome_options = Options()
    driver = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)
    driver.delete_all_cookies()
    logger.info("开始登录")
    driver.get(pro.get('url'))
    driver.maximize_window()

    cookie_1 = {'domain': 'localhost',
                'name': 'JSESSIONID',
                'value': pro.get('JSESSIONID'),
                'path': '/aeaicrm/',
                'httpOnly': True,
                'secure': False}
    driver.add_cookie(cookie_1)
    driver.refresh()
    #判断是否登录成功
    assert driver.current_url==pro.get('home_url')
    logger.info("登录成功")
    return driver