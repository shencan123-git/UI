#!/usr/bin/
# -*- coding: UTF-8 -*-

from base.uicommon.web_base_page import *


class OrganizationPage(WebBasePage):
    def __init__(self,driver):
        super(OrganizationPage, self).__init__(driver)

    #判断分组列表中的公司集团是否显示
    def organization_is_display_company(self):
        return self.elementDisplayed("organization_txt_company")

    #点击新增按钮
    def organization_click_add(self):
        self.clickElement("organization_btn_add")

    #输入编码
    def organization_input_group_code(self,value):
        el = self.getElement("organization_input_code")
        el.send_keys(value)

    #输入名称
    def organization_input_name(self,value):
        el = self.getElement("organization_input_name")
        el.send_keys(value)

    #点击保存按钮
    def organization_click_save(self):
        self.clickElement("organization_btn_save")

    #获取公司集团列表中第3个部门
    def organization_txt_get_department(self):
        el = self.getElement("organization_txt_tree")
        return el.text

    #选择公司集团列表中第3个部门
    def organization_txt_click_department(self):
        self.clickElement("organization_txt_tree")

    #删除
    def organization_btn_delete(self):
        self.clickElement("organization_btn_delete")