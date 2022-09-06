#!/usr/bin/
# -*- coding: UTF-8 -*-

from base.uicommon.web_base_page import *

class MenuPage(WebBasePage):
    def __init__(self,driver):
        super(MenuPage, self).__init__(driver)

    #点击客户管理菜单
    def menu_click_customer_management(self):
        self.clickElement("menu_btn_customer")

    #点击潜在客户
    def menu_click_potential_customer(self):
        self.clickElement("menu_btn_potential")

    #点击系统管理
    def menu_click_system_management(self):
        self.clickElement("menu_btn_system")

    #点击组织机构
    def menu_click_organization(self):
        self.clickElement("menu_btn_organization")







