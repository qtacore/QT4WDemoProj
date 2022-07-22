# -*- coding: utf-8 -*-

from qt4w import XPath
from qt4w.webcontrols import WebPage


class UploadFilePage(WebPage):

    ui_map = {
        "上传文件": XPath('//input[@type="file"]'),
        "文件名": XPath('//span[@id="fileName"]'),
        "文件大小": XPath('//span[@id="fileSize"]')
    }
