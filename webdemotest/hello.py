# -*- coding: utf-8 -*-
"""示例测试用例
"""
# 2019/01/18 QTAF自动生成

import os
import random
import tempfile
import time

from qt4w.browser import Browser

from webdemolib.demopage import DemoPage, ProfilePage
from webdemolib.uploadpage import UploadFilePage
from webdemolib.testcase import WebDemoTestCase


class WebDemoTest(WebDemoTestCase):
    """QT4W跨端Demo测试用例"""

    owner = "qta"
    timeout = 5
    priority = WebDemoTestCase.EnumPriority.High
    status = WebDemoTestCase.EnumStatus.Ready

    def run_test(self):
        self.start_step("1. 在浏览器中打开测试页面")
        browser = Browser()
        page = browser.open_url("https://qtacore.github.io/qt4w/demo.html", DemoPage)

        self.start_step("2. 设置信息并提交")
        page.set_name("qta")
        page.set_female()
        page.set_age(str(20))
        page.set_company("tencent")
        page.submit()
        time.sleep(2)  # 等待页面跳转

        self.start_step("3. 检查页面跳转以及内容是否正确")
        page = browser.find_by_url(
            "https://qtacore.github.io/qt4w/welcome.html?name=qta&sex=female&age=20&company=tencent",
            ProfilePage,
        )
        self.assert_equal("检查页面标题", page.title, "欢迎您：qta女士")
        self.assert_equal("检查用户名", page.control("用户名").inner_text, "qta")
        self.assert_equal("检查性别", page.control("性别").inner_text, "女")
        self.assert_equal("检查年龄", page.control("年龄").inner_text, "20")
        self.assert_equal("检查公司", page.control("公司").inner_text, "tencent")


class UploadFileTest(WebDemoTestCase):
    """上传文件测试"""

    owner = "drunkdream"
    timeout = 5
    priority = WebDemoTestCase.EnumPriority.High
    status = WebDemoTestCase.EnumStatus.Ready


    def run_test(self):
        self.start_step("1. 在浏览器中打开上传文件测试页面")
        browser = Browser()
        page = browser.open_url("https://qtacore.github.io//qt4w/upload.html", UploadFilePage)

        file_path = tempfile.mkstemp(".txt")[1]
        file_size = random.randint(1024, 10240)
        with open(file_path, "w") as fp:
            fp.write("a" * file_size)
        page.upload_file(file_path)
        self.assert_equal("检查要上传的文件名", page.control("文件名").inner_text, os.path.split(file_path)[-1])
        self.assert_equal("检查要上传的文件大小", int(page.control("文件大小").inner_text), file_size)


if __name__ == "__main__":
    WebDemoTest().debug_run()
