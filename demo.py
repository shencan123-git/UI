#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import time
from selenium.webdriver.chrome.options import Options

user='admin'
password='admin'
url='http://localhost:6060/aeaicrm/index?Login'
chrome_driver_path = "F:\\虫师资料\\webui\\脚本\\CRMDemo\\config\\chromedriver.exe"
driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)


driver.delete_all_cookies()
driver.get(url)
time.sleep(10)
# cookie_1 = {'domain': 'localhost',
#             'name': 'JSESSIONID',
#             'value': 'BF6429DE849B4F70996BD20550983E23',
#             'path': '/aeaicrm/',
#             'httpOnly': True,
#             'secure': False}
#
# #添加cookie
# driver.add_cookie(cookie_1)
# driver.refresh()
# time.sleep(2)

# #根据id找到元素，输入用户名
# driver.find_element_by_id("userId").send_keys("admin")
# #根据name找到元素，输入用户名
# driver.find_element_by_name("userPwd").send_keys("admin")
# #根据class找到元素，点击重置按钮
# driver.find_element_by_class_name("btn-reset").click()

#根据tag name和属性值找到元素，输入用户名
els=driver.find_elements_by_tag_name('input')
for i in els:
    if i.get_attribute("label")=="用户":
        i.send_keys("admin")
time.sleep(10)
#根据css Selector找到元素，输入密码
driver.find_element_by_css_selector("input[label=密码]").send_keys("admin")
time.sleep(10)
#根据xpath找到元素，点击重置按钮
driver.find_element_by_xpath('//form[@id="form1"]//input[@name="reset"]').click()
time.sleep(10)

# #根据link text找元素
# driver.find_element_by_link_text("潜在客户").click()
time.sleep(3)
driver.quit()

