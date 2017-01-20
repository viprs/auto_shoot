#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coder: samren
# version : 1.0
import os


def get_user_dict_from_file(file_path):
    if not os.path.exists(file_path):
        return
    user_dict = {}
    with open(file_path) as f:
        for i in f.readlines():
            username, password = i.split()
            user_dict[username] = password
    return user_dict