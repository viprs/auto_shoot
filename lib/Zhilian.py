#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from Base import Base
import time
from config import *
import traceback

class Zhilian(Base):
    def __init__(self, username, password):
        self.base_url = u'http://m.zhaopin.com'
        self.driver = webdriver.Firefox()
        self.driver.set_page_load_timeout(10)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.username = username
        self.password = password

    def login(self):
        """登录操作"""
        try:
            self.driver.get(self.base_url + u'/account/login?prevUrl=http%3A//m.zhaopin.com/')
        except TimeoutException:
            print 'time out after 30 seconds when loading page'
            self.driver.execute_script('window.stop()')
            # 当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
        print self.username, self.password
        driver = self.driver
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(self.username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(self.password)
        time.sleep(2)
        driver.find_element_by_class_name("btn").click()
        time.sleep(2)

    def search_job(self):
        """搜索工作"""
        try:
            self.driver.get(u"http://m.zhaopin.com/shenzhen-765/?keyword=软件测试工程师&pageindex=1")
        except TimeoutException:
            print 'time out after 30 seconds when loading page'
            self.driver.execute_script('window.stop()')

    def custom_select_job(self):
        """定制工作，去掉一些皮包公司"""
        #1.滚动窗口，把公司完整列表加载完成
        # SCREEN = 17
        #
        # self.driver.find_element_by_class_name("resultslist_type_tit").send_keys(Keys.SPACE)
        # time.sleep(2)

        #2.把皮包公司过滤掉
        job_checkboxes = self.driver.find_elements_by_class_name("cheak ")
        company_names = self.driver.find_elements_by_class_name("companyname")
        company_count = len(company_names)
        print "company count:", company_count, "job_checkboxes count:", len(job_checkboxes)
        #done: 第一行选不到，页面上可能有bug
        for j in xrange(company_count):
            #必须从1开始，因为第0个是『公司名称』
            print company_names[j].text.encode('utf-8')
            if company_names[j].text in (u"厦门国际金融技术有限公司", u"深圳怀谷信息技术有限公司", u"深圳市门道信息咨询有限公司"):
                print "=======>skip"
                continue
            try:
                job_checkboxes[j].click()
                print "=======>正在勾选第%s个公司" % j
            except Exception:
                traceback.print_exc()
                ##在Windows机器上不用翻页，Firefox浏览器会自动滚动
                #self.driver.find_element_by_class_name("f_l").send_keys(Keys.PAGE_DOWN)
                time.sleep(2)
        self.driver.find_element_by_link_text(u"申请职位").click()

    def quit(self):
        self.driver.quit()