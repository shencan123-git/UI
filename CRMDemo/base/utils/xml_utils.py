#!/usr/bin/
# -*- coding: UTF-8 -*-

from base.utils.file_utils import *
import xml.etree.cElementTree as ET
from base.uicommon.global_logger import *

def parse_xml(path):
    """
    解析xml文件，将元素信息存到字典中
    @path 根目录文件
    @return elements 返回字典
    """
    elements = {}
    if os.path.exists(path):
        f = get_filepath_by_type(path,"xml",all_files = [])
        for fi in f:
            tree = ET.ElementTree(file=fi)
            for elem in tree.iter(tag="locator"):
                locator =elem.attrib
                locator_name = locator['name']
                #需要保证locator_name唯一
                if locator_name in elements.keys():
                    logger.error("xml中元素name有重复，重复名：%s" %locator_name)
                    raise RuntimeError('elements duplicate')
                else:
                   elements[locator_name] = locator
        return elements





