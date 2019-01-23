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
    
class WebDemoTestCase(WebTestBase):
    '''Web demo测试用例基类
    '''
    pass
