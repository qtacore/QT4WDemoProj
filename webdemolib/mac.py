# -*- coding: utf-8 -*-

'''Mac端Web测试基类
'''

from qt4mac.testcase import MacTestCase
from qt4w.browser import Browser

class MacOSWebTestBase(MacTestCase):
    '''Mac端Web测试基类
    '''
    
    def pre_test(self):
        Browser.register_browser('Chrome', 'qt4mac.browser.ChromeHeadlessBrowser') # 注册Chrome浏览器
