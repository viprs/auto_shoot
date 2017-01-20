#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.Logger import Logger
from lib.common import get_user_dict_from_file
from lib.Cjol import Cjol
from lib.Zhilian import Zhilian
from lib.Job51 import Job51
from selenium import webdriver
import logging
import traceback
import time,datetime
import linecache
from __builtin__ import str

#设置需要投递几页的公司
JOB_PAGE_NUM=2 #设置投递公司页数
JOB_CITY= u"深圳"
JOB_NAME= u"软件测试工程师"

d1 = datetime.datetime.now()


#获取排除公司列表，通常是一些皮包公司
def get_company_info():
    with open('exclude_company.txt','r') as info:
        company_info=[]
        for line in info:
            line=line.strip()
            company_info.append(line)
    return company_info


def search_job():
    driver.find_element_by_id("JobLocation").clear()
    driver.find_element_by_id("JobLocation").send_keys(JOB_CITY)
    driver.find_element_by_xpath(".//*[@id='frmSearch']/div/div[3]/input").clear()
    driver.find_element_by_xpath(".//*[@id='frmSearch']/div/div[3]/input").send_keys(JOB_NAME)
    driver.find_element_by_id("search").click()
    #防止第二个浏览器窗口延迟加载
    now_handle = driver.current_window_handle
    time.sleep(3)
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != now_handle:
            driver.switch_to_window(handle)


def screen_company():
    job_checkbox=driver.find_elements_by_css_selector("input[type=checkbox]")
    gsmc=driver.find_elements_by_class_name("gsmc")
    company_count=len(gsmc)
    company_info=get_company_info()
    for select_num in range(1,company_count):
        #去除匹配公司多选框
        if (gsmc[select_num].text.encode('utf-8') in company_info)==False:
            job_checkbox[select_num+1].click()
        if select_num % 10 ==0:
            select_check_job()
            driver.find_element_by_id("checkbox4al2").click()
            time.sleep(1)
            driver.find_element_by_id("checkbox4al2").click()
            time.sleep(2)

def select_check_job():
    try:
        #点击申请工作按钮
        driver.find_element_by_link_text(u"申请职位").click()
    except:pass
    try:
    #点击投递广告页面 忽略按钮
        pass
    except:pass
    try:
        #点击立即申请按钮
        driver.find_element_by_id("applynowbutton").click()
    except:pass
    try:
        #关闭已经申请过的职位弹窗
        driver.find_element_by_css_selector(u"a[title=\"关闭\"] > img").click()
    except:pass
    try:
        #关闭微信广告页面
        driver.find_element_by_css_selector("span.fr.popup_close").click()
    except:pass



def cjol_shoot(username, password):
    """人才热线的投递"""
    cjol = Cjol(username, password)
    #cjol.login()
    cjol.search_job()
    cjol.custom_select_job()
    # cjol.quit()


def zhilian_shoot(username, password):
    """智联招聘简历投递"""
    print username + "   " + password
    #智能等待页面完成加载
    zl = Zhilian(username, password)
    #zl.login()
    zl.search_job()
    zl.custom_select_job()


def job51_shoot(username, password):
    """智联招聘简历投递"""
    print username + "   " + password
    #智能等待页面完成加载
    zl = Job51(username, password)
    #zl.login()
    zl.search_job()
    zl.custom_select_job()

if __name__=="__main__":
    #生成日志文件
    ZHAOPIN_SITE = {
        'zhilian': zhilian_shoot
    }
    now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    logger = Logger("./log/test_shoot_%s.log" % now, loglevel=logging.INFO).getlog()
    count = len(open('stu_data.txt','rU').readlines())
    user_dict = get_user_dict_from_file('stu_data.txt')

    for k,v in user_dict.items():
        print k,v

        try:
            #cjol_shoot(k, v)
            #zhilian_shoot(k, v)
            job51_shoot(k, v)
            logger.info(k + ' is success!!!')
        except Exception as e:
            traceback.print_exc()
            logger.error(k + ' is failed!!!')
        exit(0)
            
    eslapse_time = datetime.datetime.now() - d1
    logger.info('本次投递 '+str(count)+' 个学生的简历共计用时：'+str(eslapse_time))