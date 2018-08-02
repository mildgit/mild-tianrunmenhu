# -*- coding: utf-8 -*-
# @Time  : 2018/7/11 21:29 
# @Author: mild
# @File  : base_page.py
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Action(object):

    def __init__(self, d):
        self.driver = d
