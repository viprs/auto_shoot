#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import os
import time
import logging


class Logger(object):
    def __init__(self, logname='./log/logger.log', loglevel=logging.DEBUG):
        """
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        """

        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(loglevel)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname)
        fh.setLevel(loglevel)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d  - %(message)s')
        #fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


if __name__ == '__main__':
    logger = Logger("product.log", logging.DEBUG).getlog()
    logger.info('info message')
    logger.error("error message")
    logger.warn("warn message")
    logger.critical("critical message")