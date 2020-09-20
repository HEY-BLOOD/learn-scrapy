import scrapy
import os
from . import DOWNLOAD_PATH


class ItemSpider(scrapy.Spider):
    name = 'item_spider'

    def start_requests(self):
        urls = [
            'http://lab.scrapyd.cn/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        mingyan = response.css('div.quote')[0]

        text = mingyan.css('.text::text').extract_first()  # 提取名言
        author = mingyan.css('.author::text').extract_first()  # 提取作者
        tags = mingyan.css('.tags .tag::text').extract()  # 提取标签
        tags = ','.join(tags)  # 数组转换为字符串，逗号分隔

        if not os.path.exists(DOWNLOAD_PATH):
            os.mkdir(DOWNLOAD_PATH)
        filename = os.path.join(
            DOWNLOAD_PATH, '{0:}-{1:}-名言.txt'.format(
                os.path.abspath(__file__).split('\\')[-1].split('.')[0],
                author))

        with open(filename, 'w', encoding='utf-8') as f:  # 覆盖文件
            f.write(text)  # 写入名言内容
            f.write('\n')  # 换行
            f.write('标签：' + tags)  # 写入标签
            f.close()  # 关闭文件操作
            self.log('写入成功，文件：{}'.format(filename))
