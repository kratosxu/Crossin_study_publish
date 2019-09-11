# coding=UTF-8
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
import sys
import io
import time
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class lianjia_zufang(object):

    def __init__(self):
        self.rs = pd.DataFrame(columns = ['房屋标题', '链接', '所在区域', '平米数', '房屋朝向', '房屋规格', '楼层区域', '房屋特点'])
        # 最开始想根据输入的城市来查找租房信息，但是发现SOUP里面的标签不一样……
        # lj_cities_url = 'https://www.lianjia.com/city/'
        # lj_cities_bs = BeautifulSoup(requests.get(lj_cities_url).text, 'lxml')
        # wanted_city = input('您想查询哪个城市的租房信息?\n')
        # self.lj_req_url = lj_cities_bs.find('a', text = wanted_city)['href']
        self.lj_req_url = 'https://sh.lianjia.com/zufang'
        lj_cookie = 'lianjia_uuid=edf68ab2-db72-431a-9628-c4273db626a5; all-lj=8e5e63e6fe0f3d027511a4242126e9cc; select_city=310000; UM_distinctid=16d003484cdb4-0630bffb9704e3-5373e62-100200-16d003484ce4e9; CNZZDATA1253492439=52190204-1567664788-%7C1567664788; CNZZDATA1254525948=1552591089-1567663672-%7C1567663672; CNZZDATA1255633284=1619095033-1567661163-%7C1567661163; CNZZDATA1255604082=169328530-1567663670-%7C1567663670; _jzqa=1.3258270478238783500.1567666505.1567666505.1567666505.1; _jzqc=1; _jzqckmp=1; _qzja=1.1483091905.1567666505011.1567666505011.1567666505012.1567666505011.1567666505012.0.0.0.1.1; _qzjc=1; _qzjto=1.1.0; _smt_uid=5d70b149.15acb379; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d0034872d2c9-0e8b72f07f2d06-5373e62-1049088-16d0034872e24f%22%2C%22%24device_id%22%3A%2216d0034872d2c9-0e8b72f07f2d06-5373e62-1049088-16d0034872e24f%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.1618726943.1567666507; _gid=GA1.2.1471569872.1567666507; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMzJjODViY2E3OTgzYTA3MDQzNTc2ZmViMGU4MDkxODgxMmFjNzBiODBkMjMyZDA4NWI0MWIxODFiZDBlYTc3YzJiMGMyZWI3N2JkMWNkMzIzMjFhZTUwYzM4NzU2Yjg1MDVhYWRhZjY3YjRlZGZlYzkwMjI5MDBjYWI2NDgwODQxYzgzMTgxNTBiZjdiMjU1MzBhN2EzY2Q2ZTFmODJkNDIyZjhjZTVlM2U1OTc5ODFiYmI3NGVmN2VkMGNiNzQ3YzY2OTQ5ODMzNWFlNTQxMWViZmI0MmRjM2JmZWQzZWMwNDQ2Y2ZkYjYwYjljZTcxZmRhYjEyNmEyMDQxZTA3NzYzOGZjODM1ZmJkN2ZmYTEyNTAzNTJiNzk2NzM5MWM5NTNiNzdiMDI0NWNlZmNmZDBmM2EzY2Q0NjEwMjUyYWE0NWIyNGU1YzhmYjc4ZTY3OTE0YzJjNTRhMmM4ZmQ5OFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI0YTRhZTUwNlwifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL3p1ZmFuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
        lj_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        self.lj_header = {'User-Agent': lj_ua, 'Cookie': lj_cookie}


    def lj_spider(self):
        pages = int(input('您需要爬多少页数据？（每页30条房源信息）\n'))
        try:
            for i in range(pages):
                if i == 0:
                    spider_url = self.lj_req_url
                else:
                    spider_url = self.lj_req_url + '/p' + str(i+1)

                lj_req = requests.get(spider_url, headers = self.lj_header)
                print (lj_req.status_code)
                print (spider_url)
                lj_soup = BeautifulSoup(lj_req.text, 'lxml')

                for j in range(len(lj_soup.find_all(attrs = {'class':'content__list--item--aside'}))):
                    a = (lj_soup.find_all(attrs={'class':'content__list--item--des'})[j]).get_text(strip = True).split('/')
                    self.rs = self.rs.append([{
                        '房屋标题': lj_soup.find_all(attrs = {'class':'content__list--item--aside'})[j]['title'],
                        '链接': lj_soup.find_all(attrs = {'class':'content__list--item--aside'})[j]['href'],
                        '所在区域': re.findall(r'(\b\w*-\w*)-\w*', a[0])[0],
                        '平米数': a[1],
                        '房屋朝向': a[2],
                        '房屋规格': a[3],
                        '楼层区域': a[4].replace(' ', ''),
                        '房屋特点': ','.join(lj_soup.find_all(attrs={'class':'content__list--item--bottom oneline'})[j].text.split())
                    }])

                time.sleep(5)
            self.rs.to_csv('链家上海租房信息.csv', encoding = 'GBK', index = False)

        except Exception as e:
            print ('本次爬取失败\n报错信息为：\n%s' % e)
        finally:
            print ('本次总共爬取%i条数据' % len(self.rs))


a = lianjia_zufang()
a.lj_spider()
