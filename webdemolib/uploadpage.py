# -*- coding: utf-8 -*-

from qt4w import XPath
from qt4w.webcontrols import WebPage, FrameElement, InputFileElement


class UploadFilePage(WebPage):
    """文件上传页面"""

    ui_map = {
        "上传文件1": {"type": InputFileElement, "locator": XPath('//input[@id="myFile1"]')},
        "文件名1": XPath('//span[@id="fileName1"]'),
        "文件大小1": XPath('//span[@id="fileSize1"]'),
        "上传文件2": {"type": InputFileElement, "locator": XPath('//input[@id="myFile2"]')},
        "文件名2": XPath('//span[@id="fileName2"]'),
        "文件大小2": XPath('//span[@id="fileSize2"]'),
    }

    def upload_file1(self, file_path):
        self.control("上传文件1").upload_file(file_path)

    def upload_file2(self, file_path):
        self.control("上传文件2").upload_file(file_path)


class IFrameUploadFilePage(UploadFilePage):
    """iframe中的文件上传页面"""

    ui_map = {
        "iframe": {
            "type": FrameElement,
            "locator": XPath('//iframe[@id="frame"]'),
            "ui_map": UploadFilePage.ui_map,
        }
    }

    def upload_file1(self, file_path):
        self.control("iframe.上传文件1").upload_file(file_path)

    def upload_file2(self, file_path):
        self.control("iframe.上传文件2").upload_file(file_path)
