# 学习笔记

* 1、爬虫过程中会遇到验证，使用print(response.url)打印出要验证的链接，复制到浏览器中完成验证即可。后面可以使用selenium和chrome device实现自动解锁
* 2、使用scrapy爬取猫眼，可以在settings.py中设置DEFAULT_REQUEST_HEADERS，把浏览器的信息粘贴过来，可以正常爬取页面。
* 3、scrapy使用pipelin要在settings.py中配置，配置文件的pipeline名称要和pipelines.py中名称对应
