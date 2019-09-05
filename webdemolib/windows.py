# -*- coding: utf-8 -*-

'''Windows端测试基类
'''

from qt4c import testcase
from qt4w.browser import Browser


class WindowsWebTestBase(testcase.ClientTestCase):
    '''Windows端测试基类
    '''

    def pre_test(self):
        Browser.register_browser('IE', 'browser.ie.IEBrowser') # 注册IE浏览器
        Browser.register_browser('Chrome', 'browser.chrome.ChromeBrowser') # 注册Chrome浏览器
        self._clean_env()

    def _clean_env(self):
        from browser.ie import IEBrowser
        from browser.chrome import ChromeBrowser
        IEBrowser.killall()
        ChromeBrowser.killall()