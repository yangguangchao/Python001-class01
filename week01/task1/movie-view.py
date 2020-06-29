"""
安装并使用 requests、bs4 库,爬取猫眼电影（）的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# 电影详细页面
url = 'https://maoyan.com/films?showType=3'

# 设置UA，网站会根据UA反爬虫
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# 声明为字典使用字典的语法赋值
header = {}
header['user-agent'] = user_agent
response = requests.get(url, headers=header)

# 处理字符串，获取电影类型、上映时间
def parse_str(str):
    return str.split(':')[-1].strip()


bs_info = bs(response.text, 'html.parser')

#判断是否跳转到访问页面，访问页面进行信息爬取，验证页面提醒在浏览器中打开url进行验证
if response.url == url:
    movie_views = []
    for tags in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
        for atag in tags.find_all('div',attrs={'class': 'movie-hover-title'}):
            for btag in atag.find_all('span', attrs={'class': 'hover-tag'}):
                if btag.text == '类型:':
                    movie_type = parse_str(btag.find_parent('div').text)
                    film_name = btag.find_parent('div').get('title')
                if btag.text == '上映时间:':
                    plan_date = parse_str(btag.find_parent('div').text)
                    if len(movie_views) < 10:        #判断列表元素个数是否达到10个
                        movie_views.append([film_name, movie_type, plan_date])
                    else:
                        break

    movie_file = pd.DataFrame(data = movie_views)
    movie_file.to_csv('./movies.csv', encoding='utf8', index=False, header=False)
else:
    print('请使用浏览器打开url:%s 进行安全验证后再重新运行' % response.url)
