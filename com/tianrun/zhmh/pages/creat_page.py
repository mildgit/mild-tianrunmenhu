# -*- coding: utf-8 -*-
# @Time  : 2018/7/11 21:28 
# @Author: mild
# @File  : creat_page.py

from com.tianrun.zhmh.pages import base_page
from com.tianrun.zhmh.pages import id_page
import time


class CreatPage(base_page.Action, id_page.Elements):

    """用例1--登陆"""
    def add_button_link(self):
        pass

    def name_password(self):  # 输入用户名 密码
        pass

    def py_image(self):  # 验证码 识别
        pass
