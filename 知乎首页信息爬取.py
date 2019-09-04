import requests
import json
import pandas as pd

class zhihu_indexpage(object):

    def __init__(self, input_cookie='_xsrf=MclbbI0gtXrCMncdNeK5LNELe8ZrtsI1; _zap=1cad0604-4e92-4ca7-886d-5a5011081f2d; d_c0="AIBkyaYTcQ6PTmFi4Mc8K1HSknCsvnZ9hFw=|1540886621"; q_c1=cd2ffa7227e448f09f6484c19b5c51a7|1540886676000|1540886676000; __utma=51854390.1029515552.1540888300.1540888300.1540888300.1; __utmv=51854390.100--|2=registration_date=20161013=1^3=entry_date=20161013=1; capsion_ticket="2|1:0|10:1567156714|14:capsion_ticket|44:ZTIxOTQ2NWQ1MjVkNDdjMjhiOGFlN2RhMGFhYTVmNzQ=|568e8be4f7692516d17dfa0e788f85f863565758d9530e3bc0a4be6e43ea6ddd"; z_c0="2|1:0|10:1567156734|4:z_c0|92:Mi4xdDFlUkF3QUFBQUFBZ0dUSnBoTnhEaVlBQUFCZ0FsVk5famRXWGdDR0pMcWJ1RGJPbjFqcUVZYXdMVUZRSGpLTHRB|ab054f738a6ae096fa3ca19f6dac3da251b7c4d2676d89df08e34e3005bc4268"; tst=r; tgw_l7_route=060f637cd101836814f6c53316f73463'):
        self.url = 'https://www.zhihu.com/'
        self.req_useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        self.rs = pd.DataFrame(columns=['问题ID', '问题题目', '回答条目', '关注问题人数', '回答ID', '回答作者', '该回答评论数', '该回答点赞数', '感谢答者数目'])
        self.req_cookie = input_cookie
        self.req_headers = {'cookie': self.req_cookie, 'user-agent': self.req_useragent}

    def indexpage_spider(self):
        self.target_cnt = int(input('希望爬取多少条数据？\n'))
        self.spider_cnt = 2
        while True:
            if len(self.rs) >= self.target_cnt:
                break
            else:
                self.req_path = 'api/v3/feed/topstory/recommend?session_token=d433fdca5155b7782de7e7b8da799ab1&desktop=true&page_number=%i&limit=6&action=down&after_id=%i' % (self.spider_cnt, (self.spider_cnt - 2) * 6 + 5)
                self.req = requests.get(self.url+self.req_path, headers = self.req_headers)
                self.req.encoding = 'UTF-8'
                self.data = json.loads(self.req.text)['data']

                for j in range(len(self.data)):
                    if self.data[j]['target']['type'] == 'article':
                        pass
                    else:
                        self.rs = self.rs.append([{'问题ID':self.data[j]['target']['question']['id'],
                                         '问题题目':self.data[j]['target']['question']['title'],
                                         '回答条目':self.data[j]['target']['question']['answer_count'],
                                         '关注问题人数':self.data[j]['target']['question']['follower_count'],
                                         '回答ID':self.data[j]['target']['id'],
                                         '回答作者':self.data[j]['target']['author']['name'],
                                         '该回答评论数':self.data[j]['target']['comment_count'],
                                         '该回答点赞数': self.data[j]['target']['voteup_count'],
                                         '感谢答者数目': self.data[j]['target']['thanks_count']}])

        self.rs.to_csv('知乎首页推荐.csv', encoding='gbk', index=False)
        print ('本次爬取了%i条数据' % len(self.rs))

a = zhihu_indexpage()
a.indexpage_spider()