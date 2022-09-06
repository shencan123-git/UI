#!/usr/bin/
# -*- coding: UTF-8 -*-

import unittest
from base.uicommon.chrome_driver_init import *
from po.menu_page import *
from po.organzitation_page import *
from po.switch_frame import *
from base.utils.take_screenshot_utils import *


class OrganizationProject(unittest.TestCase):

    def setUp(self):
        self.driver = start_chrome_driver()
        self.menuPage = MenuPage(self.driver)
        self.orgPage = OrganizationPage(self.driver)
        self.switchFrame = SwitchFrame(self.driver)


    def tearDown(self):
        self.driver.quit()


    @take_screen_shot
    def test_organization_add_department(self):
        logger.info("start to run test case test_organization_add_department")
        # 切换frame
        self.switchFrame.switch_to_leftFrame()
        logger.info("点击系统管理")
        self.menuPage.menu_click_system_management()
        logger.info("点击组织机构")
        self.menuPage.menu_click_organization()
        self.driver.switch_to.default_content()
        time.sleep(1)
        #切换frame
        self.switchFrame.switch_to_mainFrame()
        logger.info("判断是否打开组织机构页面,公司集团可见")
        self.assertTrue(self.orgPage.organization_is_display_company(),"公司集团不可见")
        logger.info("点击新增按钮")
        self.orgPage.organization_click_add()
        self.switchFrame.switch_to_treeBoxFrame()
        logger.info("输入编码")
        self.orgPage.organization_input_group_code("TEMP")
        logger.info("输入名称")
        self.orgPage.organization_input_name("test")
        logger.info("点击保存按钮")
        self.orgPage.organization_click_save()
        self.driver.switch_to.default_content()
        self.switchFrame.switch_to_mainFrame()
        self.assertEqual(self.orgPage.organization_txt_get_department(),"test")
        time.sleep(1)
        logger.info("选择新建的部门")
        self.orgPage.organization_txt_click_department()
        logger.info("点击删除按钮")
        self.orgPage.organization_btn_delete()
        time.sleep(1)
        logger.info("从html页面切换到alert弹框")
        alert = self.driver.switch_to.alert
        logger.info("点击确定按钮")
        alert.accept()
        time.sleep(2)
        logger.info("finish to run test case test_organization_add_department")




















