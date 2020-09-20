# mingyan
scrapy 框架练习

learn from http://www.scrapyd.cn/doc/

操作系统：Windows 10 Pro 19041.508

**克隆项目：**

```sh
git clone https://github.com/HEY-BLOOD/mingyan.git

cd ./mingyan
```

**环境准备：**

这里使用的conda创建虚拟环境，因为它能够自动处理库的依赖；我把环境放在了 `D:/scrapy_venv` 路径下

```sh
conda create --prefix=D:/scrapy_venv python=3.6 scrapy -y
```

**激活虚拟环境：**

```sh
conda activate D:\scrapy_venv
```

**运行蜘蛛：**

```sh
scrapy crawl next_spider
```



