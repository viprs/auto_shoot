#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
from selenium import webdriver


class Base(object):
    def __init__(self, username, password):
        self.login_url = ''
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.username = username
        self.password = password

    def login(self):
        """登录操作"""
        pass

    def search_job(self):
        """搜索工作"""
        pass

    def custom_select_job(self):
        """定制工作，去掉一些皮包公司"""
        pass