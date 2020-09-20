import scrapy
import os
from . import DOWNLOAD_PATH


class ArgsSpider(scrapy.Spider):
    name = os.path.abspath(__file__).split('\\')[-1].split('.')[0]

    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'

        tag = getattr(self, 'tag', None)  # 获取tag值，也就是爬取时传过来的参数
        if tag is not None:  # 判断是否存在tag，若存在，重新构造url
            url = url + 'tag/' + tag  # 构造url若tag=爱情，url= "http://lab.scrapyd.cn/tag/爱情"

        yield scrapy.Request(url=url, callback=self.parse)  # 将返回的响应交给parse响应

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
            fileName = os.path.join(DOWNLOAD_PATH, '{0:}-语录.txt'.format(
                self.name))  # 定义文件名,如：{name}-{author}-语录.txt

            with open(fileName, "a+",
                      encoding='utf-8') as f:  # 不同人的名言保存在不同的txt文档，“a+”以追加的形式
                f.write(text)
                f.write('\n')  # ‘\n’ 表示换行
                f.write('标签：' + tags)
                f.write('\n-------\n')
                f.close()
                self.log('写入成功，文件：' + fileName)
