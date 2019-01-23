# -*- coding: utf-8 -*-

'''iOS端Web测试基类
'''

from qt4i.itestcase import iTestCase
from qt4w.browser import Browser

class iOSWebTestBase(iTestCase):
    '''iOS端Web测试基类
    '''
    
    def pre_test(self):
        Browser.register_browser('TestBrowser', 'qt4i.app.Safari') # 注册iOS端浏览器
    