#!/usr/bin/
# -*- coding: UTF-8 -*-

import unittest
from base.uicommon.chrome_driver_init import *
from po.menu_page import *
from po.potiential_customer_page import *
from po.switch_frame import *
from base.utils.take_screenshot_utils import *


class PotentialProject(unittest.TestCase):

    def setUp(self):
        self.driver = start_chrome_driver()
        self.menuPage = MenuPage(self.driver)
        self.potentialPage = PotentialPage(self.driver)
        self.switchFrame = SwitchFrame(self.driver)


    def tearDown(self):
        self.driver.quit()


    @take_screen_shot
    def test_potential_personal_query(self):
        logger.info("start to run test case test_potential_personal_query")
        # 切换frame
        self.switchFrame.switch_to_leftFrame()
        logger.info("点击客户管理")
        self.menuPage.menu_click_customer_management()
        logger.info("点击潜在客户")
        self.menuPage.menu_click_potential_customer()
        self.driver.switch_to.default_content()
        time.sleep(1)
        #切换frame
        self.switchFrame.switch_to_mainFrame()
        logger.info("判断是否打开潜在客户页面,个人标签页签可见")
        self.assertTrue(self.potentialPage.potential_is_display_tab_personal(),"个人标签页签不可见")
        self.switchFrame.switch_to_per_OrgFrame()
        logger.info("查询条件状态选择有效")
        self.potentialPage.potential_per_click_state("有效")
        logger.info("点击查询")
        self.potentialPage.potential_click_query()
        logger.info("选择数据")
        self.potentialPage.potential_click_data()
        logger.info("点击查看按钮")
        self.potentialPage.potential_click_check()
        time.sleep(2)
        logger.info("判断是否打开潜在查看页面,姓名可见")
        self.potentialPage.potential_per_is_display_detail_name()
        logger.info("判断姓名正确")
        self.assertEqual(self.potentialPage.potential_per_detail_get_name(),"孙小三的潜在客户")
        logger.info("判断状态正确")
        self.assertEqual(self.potentialPage.potential_per_detail_get_state(),"有效")
        logger.info("finish to run test case test_potential_personal_query")

    @take_screen_shot
    def test_potential_organization_query(self):
        logger.info("start to run test case test_potential_organization_query")
        # 切换frame
        self.switchFrame.switch_to_leftFrame()
        logger.info("点击客户管理")
        self.menuPage.menu_click_customer_management()
        logger.info("点击潜在客户")
        self.menuPage.menu_click_potential_customer()
        self.driver.switch_to.default_content()
        time.sleep(2)
        #切换frame
        self.switchFrame.switch_to_mainFrame()
        logger.info("判断是否打开潜在客户页面,个人标签页签可见")
        self.assertTrue(self.potentialPage.potential_is_display_tab_personal(),"个人标签页签不可见")
        logger.info("点击组织资源标签")
        self.potentialPage.potential_click_tab_organization()
        self.switchFrame.switch_to_org_OrgFrame()
        logger.info("查询条件状态选择有效")
        self.potentialPage.potential_org_click_state("有效")
        logger.info("点击查询")
        self.potentialPage.potential_click_query()
        logger.info("选择数据")
        self.potentialPage.potential_click_data()
        logger.info("点击查看按钮")
        self.potentialPage.potential_click_check()
        time.sleep(2)
        logger.info("判断是否打开潜在查看页面,姓名可见")
        self.potentialPage.potential_org_is_display_detail_name()
        logger.info("判断姓名正确")
        self.assertEqual(self.potentialPage.potential_org_detail_get_name(),"孙小三的组织客户")
        logger.info("判断状态正确")
        self.assertEqual(self.potentialPage.potential_org_detail_get_state(),"有效")
        logger.info("finish to run test case test_potential_organization_query")




















