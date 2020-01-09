# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2019/01/18 QTAF自动生成

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
elif settings.QT4W_PLATFORM == 'Headless':
    from .headless import WebHeadlessTestBase
    WebTestBase = WebHeadlessTestBase
else:
    raise NotImplementedError(settings.QT4W_PLATFORM)


class WebDemoTestCase(WebTestBase):
    '''Web demo测试用例基类
    '''
    pass
