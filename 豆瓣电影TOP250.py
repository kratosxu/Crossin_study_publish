import requests
import json
from PIL import Image
from io import BytesIO
import pandas as pd
import csv
import time

# # 先找到图片链接
# url = 'https://api.douban.com/v2/movie/1292052?apikey=0df993c66c0c636e29ecbb5344252a4a'
# req = requests.get(url)
# data = json.loads(req.text)
#
# # 在json格式中提供了海报的链接
# image_req = requests.get(data['image'])
# image = Image.open(BytesIO(image_req.content))
# image.save('The Shawshank Redemption.jpg')
# print (image)

# 主要用pandas汇总的Dataframe作为数据格式
rs = pd.DataFrame(columns = ['豆瓣电影id', '电影名', '主要卡司', '电影海报链接'])

# 由于是前250，观察数据后是以20为单位递增，所以最后递增到240之后，就可以停止了，所以需要循环0-12，再乘以20
for i in range (13):
    url250 = 'https://api.douban.com/v2/movie/top250?start=%i&apikey=0df993c66c0c636e29ecbb5344252a4a' % (i*20)
    req250 = requests.get(url250)
    req250.encoding = 'utf-8'
    data = json.loads(req250.text)
    # 每次20部电影，通过循环找到每部电影的相关信息
    for j in range(len(data['subjects'])):
        # 主演通过全角逗号分隔，然后以字符串形式连接
        casts = ''
        for k in range(len(data['subjects'][j]['casts'])):
            if k == len(data['subjects'][j]['casts']) - 1:
                casts += data['subjects'][j]['casts'][k]['name']
            else:
                casts += data['subjects'][j]['casts'][k]['name'] + '， '
        rs = rs.append([{'豆瓣电影id':data['subjects'][j]['id'],
                         '电影名':data['subjects'][j]['title'],
                         '主要卡司':casts,
                         '电影海报链接':data['subjects'][j]['images']['small']}])

        # 直接在循环里面把每一个电影海报保存下来了
        poster_req = requests.get(data['subjects'][j]['images']['small'])
        image = Image.open(BytesIO(poster_req.content))
        image.save('./top250poster/%s.jpg'%data['subjects'][j]['title'])
        time.sleep(5)

# 写入CSV，用UTF8打开CSV的时候会乱码，用GBK不会；本来想用电影的ID做INDEX，但是好像INDEX不能在第一行命名列名
rs.to_csv('豆瓣250.csv', encoding = 'gbk', index = False)

# 用了csv模块中的csv.writer的方法，一行一行写入。个人更喜欢Dataframe的方式
# with open ('豆瓣250csvversion.csv', 'w') as f:
# #     writer = csv.writer(f)
# #     writer.writerow(['豆瓣电影id', '电影名', '评分', '主要卡司', '电影海报链接'])
# #
# #     for i in range (13):
# #         url250 = 'https://api.douban.com/v2/movie/top250?start=%i&apikey=0df993c66c0c636e29ecbb5344252a4a' % (i*20)
# #         req250 = requests.get(url250)
# #         req250.encoding = 'utf-8'
# #         data = json.loads(req250.text)
# #         for j in range(len(data['subjects'])):
# #             casts = ''
# #             for k in range(len(data['subjects'][j]['casts'])):
# #                 if k == len(data['subjects'][j]['casts']) - 1:
# #                     casts += data['subjects'][j]['casts'][k]['name']
# #                 else:
# #                     casts += data['subjects'][j]['casts'][k]['name'] + '，'
# #             writer.writerow([data['subjects'][j]['id'], data['subjects'][j]['title'], casts, data['subjects'][j]['images']['small']])