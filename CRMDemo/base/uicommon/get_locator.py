#!/usr/bin/
# -*- coding: UTF-8 -*-

from base.utils.xml_utils import *


def get_locatorMap():
    # 解析xml文件
    eleFilePath = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir,"elements"))
    logger.info("xml路径：%s" %eleFilePath)
    locatorMap = parse_xml(eleFilePath)
    logger.info("解析xml完成")
    return locatorMap









