#!/usr/bin/
# -*- coding: UTF-8 -*-

from base.uicommon.web_base_page import *

class SwitchFrame(WebBasePage):
    def __init__(self,driver):
        super(SwitchFrame, self).__init__(driver)

    def switch_to_topLeft(self):
        self.switch_frame("frame_topLeft")

    def switch_to_topBottom(self):
        self.switch_frame("frame_topBottom")

    def switch_to_topRight(self):
        self.switch_frame("frame_topRight")

    def switch_to_leftFrame(self):
        self.switch_frame("frame_leftFrame")

    def switch_to_mainFrame(self):
        self.switch_frame("frame_mainFrame")

    def switch_to_per_OrgFrame(self):
        xf = self.getElement("frame_per_OrgFrame")
        self.driver.switch_to.frame(xf)

    def switch_to_org_OrgFrame(self):
        xf = self.getElement("frame_org_OrgFrame")
        self.driver.switch_to.frame(xf)

    def switch_to_treeBoxFrame(self):
        self.switch_frame("frame_treeBoxFrame")







