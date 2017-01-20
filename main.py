#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lib.Logger import Logger
from lib.common import get_user_dict_from_file
from lib.Cjol import Cjol
from lib.Zhilian import Zhilian
from lib.Job51 import Job51
import logging
import traceback
import time, datetime
from __builtin__ import str


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
    d1 = datetime.datetime.now()
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