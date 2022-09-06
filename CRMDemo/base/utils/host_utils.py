#!/usr/bin/
# -*- coding: UTF-8 -*-

import socket


#获取本机电脑名
def get_hostname():
   return socket.getfqdn(socket.gethostname()).split(".")[0]

#获取本机ip
def get_addr():
   return socket.gethostbyname(get_hostname())