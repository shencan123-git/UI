#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from io import BytesIO
from PIL import Image,ImageEnhance
import pytesseract
import time
from selenium.webdriver.chrome.options import Options
from PIL import ImageOps

user='admin'
password='admin'
url='http://localhost:6060/aeaicrm/index?Login'
chrome_driver_path = "F:\\虫师资料\\webui\\脚本\\CRMDemo\\config\\chromedriver.exe"
driver=webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)



screenImg = "F:\\test.png"
driver.get(url)
time.sleep(2)
# 获取用户输入框
input = wait.until(EC.presence_of_element_located((By.ID, 'userId')))  # type:WebElement
input.clear()
# 发送用户名
input.send_keys(user)
# 获取密码框
inpass = wait.until(EC.presence_of_element_located((By.ID, 'userPwd')))  # type:WebElement
inpass.clear()
# 发送密码
inpass.send_keys(password)
# 获取验证输入框
yanzheng = wait.until(EC.presence_of_element_located((By.ID, 'valideCode')))  # type:WebElement

#浏览器页面截屏
driver.get_screenshot_as_file(screenImg)
img = Image.open(screenImg).crop((1265,505, 1391, 542))
img = img.convert('L') 			#转换模式：L | RGB
img = ImageEnhance.Contrast(img)#增强对比度
img = img.enhance(2.0) 	#增加饱和度
#img.show()
img.save(screenImg)

#再次读取识别验证码
img = Image.open(screenImg)
code = pytesseract.image_to_string(img)
print(code)
print("111111111111")
print(code.strip().replace(' ', ''))


driver.find_element_by_id("valideCode").send_keys(code.strip().replace(' ', ''))
yanzheng.send_keys(Keys.ENTER)
time.sleep(2)




