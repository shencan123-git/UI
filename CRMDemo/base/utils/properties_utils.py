#!/usr/bin/
# -*- coding: UTF-8 -*-

def get_properties(filePath):
    """
    读取property文件
    @filePath 文件路径
    @return properties 返回字典
    """
    try:
        pro_file = open(filePath, 'r')
        properties = {}
        for line in pro_file:
            if line.find('=') > 0:
                strs = line.replace('\n', '').split('=')
                properties[strs[0]] = strs[1]
        pro_file.close()
        return properties
    except Exception as e:
        raise e


