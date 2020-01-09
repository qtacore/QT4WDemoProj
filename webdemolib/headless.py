# -*- coding: utf-8 -*-

'''Headless模式测试基类
'''

import testbase.testcase as tc
from qt4w.browser import Browser


class WebHeadlessTestBase(tc.TestCase):
    '''无界面Web测试基类
    '''

    def pre_test(self):
        Browser.register_browser('TestBrowser', 'chrome_headless.browser.ChromeHeadlessBrowser') # 注册Chrome Headless浏览器
