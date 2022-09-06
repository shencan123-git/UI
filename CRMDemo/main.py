#!/usr/bin/
# -*- coding: UTF-8 -*-

import HTMLTestRunner
import unittest
from base.uicommon.global_logger import *
from base.utils.file_utils import *
import time
from base.ut.core import _TestCase


def creat_suite(testcase_path):
    discover = unittest.defaultTestLoader.discover(testcase_path, pattern='test_*.py', top_level_dir=None)
    return discover

#判断log文件夹是否存在，不存在新建，存在的话删除里面的文件
def delete_log():
    log_dir = os.path.join(os.getcwd(),"log")
    isLogDirExists = os.path.exists(log_dir)
    if isLogDirExists:
       delete_file(log_dir)
    else:
       os.makedirs(log_dir)
    logger.info("日志路径; %s" % log_dir)

#判断screenshot文件夹是否存在，不存在新建，存在的话删除里面的文件
def delete_screenshot():
    screenshot_dir = os.path.join(os.getcwd(),"screenshots")
    isScreenDirExists = os.path.exists(screenshot_dir)
    if isScreenDirExists:
       delete_file(screenshot_dir)
    else:
       os.makedirs(screenshot_dir)
    logger.info("错误截图路径; %s" % screenshot_dir)

#判断报告文件夹是否存在，不存在新建，存在的话删除里面的文件
def get_report_path():
    report_dir = os.path.join(os.getcwd(),"report")
    isReportDirExists = os.path.exists(report_dir)
    if isReportDirExists:
       delete_file(report_dir)
    else:
       os.makedirs(report_dir)
    now = time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
    report_path = report_dir + "\\report_"+ now +".html"
    logger.info("报告路径; %s" %report_path)
    return report_path

if __name__ == '__main__':
    #删除错误截图
    delete_screenshot()

    unittest.TestCase = _TestCase
    testcase_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"testcases"))
    suite = creat_suite(testcase_path)
    fp = open(get_report_path(),"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="测试报告",description="自动化测试结果",
                                verbosity=3)
    runner.run(suite)
    fp.close()

