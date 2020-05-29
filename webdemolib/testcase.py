# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2019/01/18 QTAF自动生成

import random

from qt4w.browser import Browser
from testbase.conf import settings

if settings.QT4W_PLATFORM == 'Android':
    from .android import AndroidWebTestBase
    WebTestBase = AndroidWebTestBase
elif settings.QT4W_PLATFORM == 'iOS':
    from .ios import iOSWebTestBase
    WebTestBase = iOSWebTestBase
elif settings.QT4W_PLATFORM == 'Windows':
    from .windows import WindowsWebTestBase
    WebTestBase = WindowsWebTestBase
elif settings.QT4W_PLATFORM == 'Mac':
    from .mac import MacOSWebTestBase
    WebTestBase = MacOSWebTestBase
elif settings.QT4W_PLATFORM == 'Headless':
    from .headless import WebHeadlessTestBase
    WebTestBase = WebHeadlessTestBase
else:
    raise NotImplementedError(settings.QT4W_PLATFORM)


class WebDemoTestCase(WebTestBase):
    '''Web demo测试用例基类
    '''

    def pre_test(self):
        super(WebDemoTestCase, self).pre_test()
        try:
            from qt4w.util import HostsManager, ProxyServer
        except ImportError:
            return
        if hasattr(settings, 'QT4W_HTTP_PROXY') and settings.QT4W_HTTP_PROXY:
            # 设置代理服务器
            Browser.proxy_server = settings.QT4W_HTTP_PROXY
        elif hasattr(settings, 'QT4W_HOSTS') and settings.QT4W_HOSTS:
            hosts_manager = HostsManager()
            hosts_manager.add_hosts(settings.QT4W_HOSTS)
            proxy_port = random.randint(10000, 60000)
            self.proxy_server = ProxyServer(proxy_port)
            self.proxy_server.start_in_thread()
            Browser.proxy_server = 'http://127.0.0.1:%d' % proxy_port

    def post_test(self):
        super(WebDemoTestCase, self).post_test()
        try:
            from qt4w.util import HostsManager
        except ImportError:
            return
        hosts_manager = HostsManager()
        hosts_manager.clear_hosts()
        if hasattr(self, 'proxy_server') and self.proxy_server:
            self.proxy_server.stop()
