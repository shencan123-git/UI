#!/usr/bin/
# -*- coding: UTF-8 -*-

from base.uicommon.web_base_page import *
from selenium.webdriver.support.select import Select

class PotentialPage(WebBasePage):
    def __init__(self,driver):
        super(PotentialPage, self).__init__(driver)

    #判断个人标签是否显示
    def potential_is_display_tab_personal(self):
        return self.elementDisplayed("potential_tab_personal")

    #点击个人资源标签
    def potential_click_tab_personal(self):
        self.clickElement("potential_tab_personal")

    #点击组织资源标签
    def potential_click_tab_organization(self):
        self.clickElement("potential_tab_organization")

    #个人资源选择状态为有效
    def potential_per_click_state(self,value):
        s = self.getElement("potential_per_state")
        Select(s).select_by_visible_text(value)

    #点击查询按钮
    def potential_click_query(self):
        self.clickElement("potential_query")

    #选择一条数据
    def potential_click_data(self):
        self.clickElement("potential_row")

    #点击查看按钮
    def potential_click_check(self):
        self.clickElement("potential_check")

    #判断个人资源-详情-名称是否显示
    def potential_per_is_display_detail_name(self):
        return self.elementDisplayed("potential_per_detail_name")

    #个人资源-详情-获取姓名
    def potential_per_detail_get_name(self):
        el = self.getElement("potential_per_detail_name")
        return el.get_attribute('value')

    #个人资源-详情-获取状态
    def potential_per_detail_get_state(self):
        el = self.getElement("potential_per_detail_state")
        return el.get_attribute('value')

    #组织资源选择状态为有效
    def potential_org_click_state(self,value):
        s = self.getElement("potential_org_state")
        Select(s).select_by_visible_text(value)

    #判断个人资源-详情-名称是否显示
    def potential_org_is_display_detail_name(self):
        return self.elementDisplayed("potential_org_detail_name")

    #个人资源-详情-获取姓名
    def potential_org_detail_get_name(self):
        el = self.getElement("potential_org_detail_name")
        return el.get_attribute('value')

    #个人资源-详情-获取状态
    def potential_org_detail_get_state(self):
        el = self.getElement("potential_org_detail_state")
        return el.get_attribute('value')




