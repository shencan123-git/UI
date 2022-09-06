#!/usr/bin/
# -*- coding: UTF-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from base.uicommon.bytype import *
from base.uicommon.global_locator import *
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support import expected_conditions as EC


class WebBasePage(object):
    def __init__(self,driver):
        self.driver = driver

    def getLocator(self,name):
        return locator[name]

    def getElementByLocatorName(self,locatorName):
        return self.getElement(locatorName)

    def getElementsByLocatorName(self,locatorName):
        return self.getElements(locatorName)

    def getElement(self,locatorName):
        w = int(self.getLocator(locatorName)["waitSec"])
        return WebDriverWait(self.driver,w ,1, NoSuchElementException).until(
            lambda driver: self.findElement(locatorName))

    def getElements(self,locatorName):
        w = int(self.getLocator(locatorName)["waitSec"])
        return WebDriverWait(self.driver, w, 1,NoSuchElementException).until(
            lambda driver:self.findElements(locatorName))

    #获取单个元素：元素可见时可以获取到元素
    def getElementUntilVisible(self,locatorName):
        w = int(self.getLocator(locatorName)["waitSec"])
        wait = WebDriverWait(self.driver, w, 1,NoSuchElementException)
        return wait.until(EC.visibility_of(self.findElement(locatorName)))

    #获取多个元素：有一个元素可见时获取属性值相同的多个元素
    def getElementsUntilAnyVisible(self,locatorName):
        w = int(self.getLocator(locatorName)["waitSec"])
        wait = WebDriverWait(self.driver, w, 1,NoSuchElementException)
        return wait.until(EC.visibility_of_any_elements_located(self.findLocator(locatorName)))

    # 获取多个元素：所有元素可见时获取属性值相同的多个元素
    def getElementsUntilAllVisible(self,locatorName):
        w = int(self.getLocator(locatorName)["waitSec"])
        wait = WebDriverWait(self.driver, w, 1,NoSuchElementException)
        return wait.until(EC.visibility_of_all_elements_located(self.findLocator(locatorName)))


    def findElement(self,locatorName):
        ty = self.getLocator(locatorName)["type"]
        value = self.getLocator(locatorName)["value"]
        if ty == ByType.ID:
            element = self.driver.find_element_by_id(value)
        elif ty == ByType.NAME:
            element = self.driver.find_element_by_name(value)
        elif ty == ByType.CLASS_NAME:
            element = self.driver.find_element_by_class_name(value)
        elif ty == ByType.CSS_SELECTOR:
            element = self.driver.find_element_by_css_selector(value)
        elif ty == ByType.XPATH:
            element = self.driver.find_element_by_xpath(value)
        elif ty == ByType.LINK_TEXT:
            element = self.driver.find_element_by_link_text(value)
        elif ty == ByType.PARTIAL_LINK_TEXT:
            element = self.driver.find_element_by_partial_link_text(value)
        elif ty == ByType.TAG_NAME:
            element = self.driver.find_element_by_tag_name(value)
        else:
            element = self.driver.find_element_by_id(value)
        return element

    def findElements(self,locatorName):
        ty = self.getLocator(locatorName)["type"]
        value = self.getLocator(locatorName)["value"]
        if ty == ByType.ID:
            elements =  self.driver.find_elements_by_id(value)
        elif ty == ByType.NAME:
            elements =  self.driver.find_elements_by_name(value)
        elif ty == ByType.CLASS_NAME:
            elements =  self.driver.find_elements_by_class_name(value)
        elif ty == ByType.CSS_SELECTOR:
            elements =  self.driver.find_elements_by_css_selector(value)
        elif ty == ByType.XPATH:
            elements = self.driver.find_elements_by_xpath(value)
        elif ty == ByType.LINK_TEXT:
            elements =  self.driver.find_elements_by_link_text(value)
        elif ty == ByType.PARTIAL_LINK_TEXT:
            elements =  self.driver.find_elements_by_partial_link_text(value)
        elif ty == ByType.TAG_NAME:
            elements =  self.driver.find_elements_by_tag_name(value)
        else:
            elements = self.driver.find_elements_by_id(value)
        return elements

    #获取locator,给visibility_of_all_elements_located和visibility_of_any_elements_located用
    def findLocator(self,locatorName):
        type = self.getLocator(locatorName)["type"]
        value = self.getLocator(locatorName)["value"]
        if type == ByType.ID:
            driver_locator = (By.ID,value)
        elif type == ByType.NAME:
            driver_locator = (By.NAME, value)
        elif type == ByType.CLASS_NAME:
            driver_locator = (By.CLASS_NAME, value)
        elif type == ByType.CSS_SELECTOR:
            driver_locator = (By.CSS_SELECTOR, value)
        elif type == ByType.XPATH:
            driver_locator = (By.XPATH, value)
        elif type == ByType.LINK_TEXT:
            driver_locator = (By.LINK_TEXT, value)
        elif type == ByType.PARTIAL_LINK_TEXT:
            driver_locator = (By.PARTIAL_LINK_TEXT, value)
        elif type == ByType.TAG_NAME:
            driver_locator = (By.TAG_NAME, value)
        else:
            driver_locator = (By.ID, value)
        return driver_locator


    def get_text(self,locatorName):
        element = self.getElement(locatorName)
        return element.text

    #通过text来获取元素
    def getElementByElementsText(self,locatorName,value):
        ei = None
        elements = self.getElementsUntilAnyVisible(locatorName)
        for e in elements:
            if e.text == value:
                ei = e
                return ei
        return ei

    # 通过attribute来获取元素
    def getElementByAttributes(self, locatorName, attr, value):
        ei = None
        elements = self.getElementsUntilAnyVisible(locatorName)
        for e in elements:
            if e.get_attribute(attr) == value:
                ei = e
                return ei
        return ei



    def clickElement(self,locatorName):
        element = self.getElementByLocatorName(locatorName)
        logger.info("click element : %s" %locatorName)
        element.click()

    def rightClickElement(self,locatorName):
        element = self.getElementByLocatorName(locatorName)
        logger.info("right click element : %s" %locatorName)
        ActionChains(self.driver).context_click(element).perform()

    def doubleClickElement(self,locatorName):
        element = self.getElementByLocatorName(locatorName)
        logger.info("double click element : %s" %locatorName)
        ActionChains(self.driver).double_click(element).perform()

    def moveToElement(self,locatorName):
        element = self.getElementByLocatorName(locatorName)
        logger.info("move to element : %s" %locatorName)
        ActionChains(self.driver).move_to_element(element).perform()

    #按下按键输入
    def pressKeyAndSendKey(self,key_value,send_value):
        action = ActionChains(self.driver)
        action.key_down(key_value).send_keys(send_value).key_up(key_value).perform()

    #长按元素
    def longPressElement(self,locatorName,t):
        element = self.getElementByLocatorName(locatorName)
        logger.info("long click element : %s" %locatorName)
        ActionChains(self.driver).click_and_hold(element).perform()
        time.sleep(t)
        ActionChains(self.driver).release(element).perform()

    def getWindowSize(self):
        x =  self.driver.get_window_size()['width']
        y =  self.driver.get_window_size()['height']
        return x,y



    def clear(self,locatorName):
        element = self.getElementByLocatorName(locatorName)
        element.clear()

    def inputByLocatorName(self,locatorName, s):
        element = self.getElementByLocatorName(locatorName)
        element.send_keys(s)

    def elementExist(self,locatorName):
        try:
            self.findElement(locatorName)
            return True
        except NoSuchElementException:
            return False

    def elementEnabled(self,locatorName):
        element = self.getElement(locatorName)
        return element.is_enabled()

    def elementDisplayed(self,locatorName):
        element = self.getElement(locatorName)
        return element.is_displayed()


    def execute_script(self,js):
        self.driver.execute_script(js)

    def switch_frame(self,locatorName):
        value = self.getLocator(locatorName)["value"]
        self.driver.switch_to.frame(value)