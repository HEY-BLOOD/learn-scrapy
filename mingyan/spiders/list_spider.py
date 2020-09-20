import scrapy
import os
from . import DOWNLOAD_PATH


class ListSpider(scrapy.Spider):
    name = os.path.abspath(__file__).split('\\')[-1].split('.')[0]

    start_urls = [
        'http://lab.scrapyd.cn/',
    ]

    def parse(self, response, **kwargs):
        posts = response.css('.post')

        if not os.path.exists(DOWNLOAD_PATH):
            os.mkdir(DOWNLOAD_PATH)
            
        for post in posts:
            text = post.css('.text::text').extract_first()
            author = post.css('.author::text').extract_first()
            tags = post.css('.tags .tag::text').extract()
            tags = ','.join(tags)
            """
            接下来进行写文件操作，每个名人的名言储存在一个txt文档里面
            """
            fileName = os.path.join(DOWNLOAD_PATH, '{0:}-{1:}-语录.txt'.format(
                self.name, author))  # 定义文件名,如：{name}-{author}-语录.txt

            with open(fileName, "w+",
                      encoding='utf-8') as f:  # 不同人的名言保存在不同的txt文档，“w+”以覆盖读写的形式
                f.write(text)
                f.write('\n')  # ‘\n’ 表示换行
                f.write('标签：' + tags)
                f.write('\n-------\n')
                f.close()
                self.log('写入成功，文件：' + fileName)
