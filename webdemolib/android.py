# -*- coding: utf-8 -*-

'''Android端Web测试基类
'''

from qt4a.androidtestbase import AndroidTestBase
from qt4w.browser import Browser

class AndroidWebTestBase(AndroidTestBase):
    '''Android端Web测试基类
    '''
    
    def pre_test(self):
        Browser.register_browser('TestBrowser', 'qt4a.browser.QT4ABrowser') # 注册Android端浏览器
    