#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Base import Base
import time
from config import *
import traceback

class Cjol(Base):
    def __init__(self, username, password):
        self.base_url = 'http://www.cjol.com'
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.username = username
        self.password = password

    def login(self):
        """登录操作"""
        self.driver.get(self.base_url + '/JobSeekers/Login.aspx')
        print self.username, self.password
        driver = self.driver
        # if driver.find_element_by_id("login_verify").is_displayed():
        #     driver.delete_all_cookies()
        #     time.sleep(5)
        #     driver.refresh()
        # else:
        #     # print driver.get_cookies()
        #     pass
        driver.save_screenshot('./screenshot/cjol_00.jpg')
        driver.find_element_by_id("txtUserName").clear()
        driver.find_element_by_id("txtUserName").send_keys(self.username)
        driver.find_element_by_id("tbxPasswordTip").click()
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys(self.password)
        driver.save_screenshot('./screenshot/cjol_01.jpg')
        driver.find_element_by_id("btnLogin_input").click()
        driver.save_screenshot('./screenshot/cjol_02.jpg')
        time.sleep(2)
        try:
            if driver.find_element_by_class_name("con_mycjolapp").is_displayed():
                print "01有弹出框需要处理"
                driver.find_element_by_class_name("icon_closedmyapp").click()
        except:
            pass

    def search_job(self):
        """搜索工作"""
        self.driver.get("http://s.cjol.com/l2008-kw-软件测试工程师/?SearchType=5&KeywordType=3")
        """
        driver = self.driver
        # driver.find_element_by_id("mini_locationtype_txt").clear()
        # driver.find_element_by_id("mini_locationtype_txt").send_keys(JOB_CITY)
        driver.find_element_by_id("mini_txtKeyWords_tip").click()
        driver.find_element_by_id("mini_txtKeyWords").click()
        driver.find_element_by_id("mini_txtKeyWords").send_keys(JOB_NAME)
        driver.find_element_by_id("mini_btnSearch").click()
        # 防止第二个浏览器窗口延迟加载
        now_handle = driver.current_window_handle
        time.sleep(3)
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
        """

    def custom_select_job(self):
        """定制工作，去掉一些皮包公司"""
        #1.滚动窗口，把公司完整列表加载完成
        SCREEN = 17
        #for s in range(3):#最多滚动3次
        self.driver.find_element_by_class_name("resultslist_type_tit").send_keys(Keys.SPACE)
        time.sleep(2)

        #2.把皮包公司过滤掉
        job_checkboxes = self.driver.find_elements_by_css_selector(".checkbox")
        company_names = self.driver.find_elements_by_class_name("list_type_second")
        company_count = len(company_names)
        print "company count:", company_count, "job_checkboxes count:", len(job_checkboxes)
        #done: 第一行选不到，页面上可能有bug
        for j in xrange(1, company_count):
            #必须从1开始，因为第0个是『公司名称』
            print company_names[j].text.encode('utf-8')
            if company_names[j].text in (u"深圳怀谷信息技术有限公司", u"深圳市门道信息咨询有限公司"):
                print "=======>skip"
                continue
            try:
                job_checkboxes[j-1].click()
                print "=======>正在勾选第%s个公司" % j
            except Exception:
                traceback.print_exc()
                ##在Windows机器上不用翻页，Firefox浏览器会自动滚动
                #self.driver.find_element_by_class_name("f_l").send_keys(Keys.PAGE_DOWN)
                time.sleep(2)

    def quit(self):
        self.driver.quit()