#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import os


def get_user_dict_from_file(file_path):
    """
    :desc 获取用户列表
    :param file_path:
    :return:
    """
    if not os.path.exists(file_path):
        return
    user_dict = {}
    with open(file_path) as f:
        for i in f.readlines():
            username, password = i.split()
            user_dict[username] = password
    return user_dict



def get_fake_company(file_path):
    """
    :Desc: 获取排除公司列表，通常是一些皮包公司
    :param file_path
    :return:返回公司名称的unicode编码
    """
    if not os.path.exists(file_path):
        return
    fake_list = []
    with open(file_path) as f:
        for line in f:
            fake_list.append(line.strip().decode("utf-8"))
    assert fake_list != []
    return fake_list