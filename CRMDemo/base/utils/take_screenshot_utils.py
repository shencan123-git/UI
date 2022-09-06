#!/usr/bin/env
# -*- coding: UTF-8 -*-

import time
from functools import wraps
import os


def take_screen_shot(function):
    @wraps(function)
    def get_ErrImage(self,*args, **kwargs):

        try:
            result = function(self,*args, **kwargs)
            return result
        except:
            time_str = time.strftime("%Y%m%d_%H%M%S")
            path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir,"screenshots"))
            isExists = os.path.exists(path)
            if not isExists:
                os.makedirs(path)
            self.driver.get_screenshot_as_file('%s\\%s %s_web.png' %
                                           (path,function.__name__,time_str))
            raise
    return get_ErrImage

