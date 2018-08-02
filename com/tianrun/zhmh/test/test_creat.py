# -*- coding: utf-8 -*-
# @Time  : 2018/7/11 21:23 
# @Author: mild
# @File  : test_creat.py
import unittest
import time
import uiautomator2 as u2
from com.tianrun.zhmh.pages.base_page import Action


class Test(unittest.TestCase):
    """智慧门户初始化apk信息"""

    def setUp(self):
        # python -m uiautomator2 init
        self.d = u2.connect_usb('7d8efa72')
        print(self.d.info)
        self.d.healthcheck()

        package = 'com.yuntongxun.rongxin.lite'
        self.d.app_start(package)

    def tearDown(self):
        d = self.d
        print("用例执行结束 等待关闭")
        time.sleep(3)
        d.app_stop('com.yuntongxun.rongxin.lite')
        d.app_clear('com.yuntongxun.rongxin.lite')

    def test_install(self):
        d = self.d
        a = d(resourceId='com.yuntongxun.rongxin.lite:id/password').get_text()
        print(a)