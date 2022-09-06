#!/usr/bin/
# -*- coding: UTF-8 -*-

import os
from base.utils.properties_utils import *

def getPropertyValue(filename):
   #读取property文件
   configFile = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir,"config",filename))
   return get_properties(configFile)