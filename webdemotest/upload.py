# -*- coding: utf-8 -*-

"""文件上传用例
"""

import os
import random
import tempfile


from qt4w.browser import Browser

from webdemolib.uploadpage import UploadFilePage, IFrameUploadFilePage
from webdemolib.testcase import WebDemoTestCase


class UploadSingleFileTest(WebDemoTestCase):
    """上传文件测试"""

    owner = "drunkdream"
    timeout = 5
    priority = WebDemoTestCase.EnumPriority.High
    status = WebDemoTestCase.EnumStatus.Ready

    def run_test(self):
        self.start_step("1. 在浏览器中打开上传文件测试页面")
        browser = Browser()
        page = browser.open_url(
            "https://qtacore.github.io/qt4w/upload.html", UploadFilePage
        )

        file_path = tempfile.mkstemp(".txt")[1]
        file_size = random.randint(1024, 10240)
        with open(file_path, "w") as fp:
            fp.write("a" * file_size)
        page.upload_file(file_path)
        self.assert_equal(
            "检查要上传的文件名", page.control("文件名").inner_text, os.path.split(file_path)[-1]
        )
        self.assert_equal("检查要上传的文件大小", int(page.control("文件大小").inner_text), file_size)


class UploadSingleFileTest(WebDemoTestCase):
    """上传单文件测试"""

    owner = "drunkdream"
    timeout = 5
    priority = WebDemoTestCase.EnumPriority.High
    status = WebDemoTestCase.EnumStatus.Ready

    def run_test(self):
        self.start_step("1. 在浏览器中打开上传文件测试页面")
        browser = Browser()
        page = browser.open_url(
            "https://qtacore.github.io/qt4w/upload.html", UploadFilePage
        )

        file_path = tempfile.mkstemp(".txt")[1]
        file_size = random.randint(1024, 10240)
        with open(file_path, "w") as fp:
            fp.write("a" * file_size)
        page.upload_file(file_path)
        self.assert_equal(
            "检查要上传的文件名", page.control("文件名").inner_text, os.path.split(file_path)[-1]
        )
        self.assert_equal("检查要上传的文件大小", int(page.control("文件大小").inner_text), file_size)


class UploadMultiFileTest(WebDemoTestCase):
    """上传多文件测试"""

    owner = "drunkdream"
    timeout = 5
    priority = WebDemoTestCase.EnumPriority.High
    status = WebDemoTestCase.EnumStatus.Ready

    def run_test(self):
        self.start_step("1. 在浏览器中打开上传文件测试页面")
        browser = Browser()
        url = "https://qtacore.github.io/qt4w/upload.html"
        url = "http://127.0.0.1:8080/qt4w/upload.html"
        page = browser.open_url(url, UploadFilePage)

        file_path1 = tempfile.mkstemp(".txt")[1]
        file_size1 = random.randint(1024, 10240)
        with open(file_path1, "w") as fp:
            fp.write("a" * file_size1)
        page.upload_file1(file_path1)
        self.assert_equal(
            "检查要上传的文件名", page.control("文件名1").inner_text, os.path.split(file_path1)[-1]
        )
        self.assert_equal(
            "检查要上传的文件大小", int(page.control("文件大小1").inner_text), file_size1
        )

        file_path2 = tempfile.mkstemp(".txt")[1]
        file_size2 = random.randint(1024, 10240)
        with open(file_path2, "w") as fp:
            fp.write("a" * file_size2)
        page.upload_file2(file_path2)
        self.assert_equal(
            "检查要上传的文件名", page.control("文件名2").inner_text, os.path.split(file_path2)[-1]
        )
        self.assert_equal(
            "检查要上传的文件大小", int(page.control("文件大小2").inner_text), file_size2
        )


class IFrameUploadFileTest(WebDemoTestCase):
    """iframe中上传文件测试"""

    owner = "drunkdream"
    timeout = 5
    priority = WebDemoTestCase.EnumPriority.High
    status = WebDemoTestCase.EnumStatus.Ready

    def run_test(self):
        self.start_step("1. 在浏览器中打开上传文件测试页面")
        browser = Browser()
        url = "https://qtacore.github.io/qt4w/upload.html"
        url = "http://127.0.0.1:8080/qt4w/iframe.html?url=upload.html"
        page = browser.open_url(url, IFrameUploadFilePage)

        file_path = tempfile.mkstemp(".txt")[1]
        file_size = random.randint(1024, 10240)
        with open(file_path, "w") as fp:
            fp.write("a" * file_size)
        page.upload_file(file_path)
        self.assert_equal(
            "检查要上传的文件名",
            page.control("iframe.文件名1").inner_text,
            os.path.split(file_path)[-1],
        )
        self.assert_equal(
            "检查要上传的文件大小", int(page.control("iframe.文件大小1").inner_text), file_size
        )
