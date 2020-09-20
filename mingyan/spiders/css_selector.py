from os import name
import scrapy
import os
from . import DOWNLOAD_PATH


class CssSelector(scrapy.Spider):
    name = os.path.abspath(__file__).split('\\')[-1].split('.')[0]

    def __init__(self):
        if not os.path.exists:
            os.mkdir(DOWNLOAD_PATH)

    def start_requests(self):
        urls = []
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        # 使用css选择器提取数据

        # 保存数据
        fileName = os.path.join(DOWNLOAD_PATH, '{0:}-{1:}'.format(name, 0))

        with open(fileName, 'a+', encoding='utf-8') as f:  # 追加读写模式打开文件
            f.close()
