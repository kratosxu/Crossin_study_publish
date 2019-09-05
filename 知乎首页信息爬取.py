import requests
import json
import pandas as pd

class zhihu_indexpage(object):

    def __init__(self, input_cookie='_xsrf=MclbbI0gtXrCMncdNeK5LNELe8ZrtsI1; _zap=1cad0604-4e92-4ca7-886d-5a5011081f2d; d_c0="AIBkyaYTcQ6PTmFi4Mc8K1HSknCsvnZ9hFw=|1540886621"; q_c1=cd2ffa7227e448f09f6484c19b5c51a7|1540886676000|1540886676000; __utma=51854390.1029515552.1540888300.1540888300.1540888300.1; __utmv=51854390.100--|2=registration_date=20161013=1^3=entry_date=20161013=1; capsion_ticket="2|1:0|10:1567156714|14:capsion_ticket|44:ZTIxOTQ2NWQ1MjVkNDdjMjhiOGFlN2RhMGFhYTVmNzQ=|568e8be4f7692516d17dfa0e788f85f863565758d9530e3bc0a4be6e43ea6ddd"; z_c0="2|1:0|10:1567156734|4:z_c0|92:Mi4xdDFlUkF3QUFBQUFBZ0dUSnBoTnhEaVlBQUFCZ0FsVk5famRXWGdDR0pMcWJ1RGJPbjFqcUVZYXdMVUZRSGpLTHRB|ab054f738a6ae096fa3ca19f6dac3da251b7c4d2676d89df08e34e3005bc4268"; tst=r; tgw_l7_route=060f637cd101836814f6c53316f73463'):
        self.url = 'https://www.zhihu.com/'
        req_useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        self.rs = pd.DataFrame(columns=['问题/文章ID', '条目类型', '问题/文章题目', '问题/文章标签', '回答条目', '关注问题人数', '回答ID', '回答/文章作者', '该回答/文章评论数', '该回答/文章点赞数', '感谢答者数目'])
        req_cookie = input_cookie
        self.req_headers = {'cookie': req_cookie, 'user-agent': req_useragent}

    def indexpage_spider(self):
        target_cnt = int(input('希望爬取大约多少条数据？\n'))
        spider_cnt = 2
        try:
            while True:
                if len(self.rs) >= target_cnt:
                    break
                else:
                    req_path = 'api/v3/feed/topstory/recommend?session_token=d433fdca5155b7782de7e7b8da799ab1&desktop=true&page_number=%i&limit=6&action=down&after_id=%i' % (spider_cnt, (spider_cnt - 2) * 6 + 5)
                    req = requests.get(self.url+req_path, headers = self.req_headers)
                    req.encoding = 'UTF-8'
                    data = json.loads(req.text)['data']

                    for j in range(len(data)):
                        if data[j]['target']['type'] == 'article':
                            self.rs = self.rs.append([{'问题/文章ID':data[j]['target']['id'],
                                             '条目类型':'文章',
                                             '问题/文章题目':data[j]['target']['title'],
                                             '问题/文章标签':data[j]['action_text'],
                                             '回答条目':'-',
                                             '关注问题人数':'-',
                                             '回答ID':'-',
                                             '回答/文章作者':data[j]['target']['author']['name'],
                                             '该回答/文章评论数':data[j][  'target']['comment_count'],
                                             '该回答/文章点赞数': data[j]['target']['voteup_count'],
                                             '感谢答者数目': '-'}])
                        else:
                            self.rs = self.rs.append([{'问题/文章ID':data[j]['target']['question']['id'],
                                             '条目类型': '回答',
                                             '问题/文章题目':data[j]['target']['question']['title'],
                                             '问题/文章标签': data[j]['action_text'],
                                             '回答条目':data[j]['target']['question']['answer_count'],
                                             '关注问题人数':data[j]['target']['question']['follower_count'],
                                             '回答ID':data[j]['target']['id'],
                                             '回答/文章作者':data[j]['target']['author']['name'],
                                             '该回答/文章评论数':data[j][  'target']['comment_count'],
                                             '该回答/文章点赞数': data[j]['target']['voteup_count'],
                                             '感谢答者数目': data[j]['target']['thanks_count']}])
            self.rs.to_csv('知乎首页推荐.csv', encoding='gbk', index=False)
        except Exception as e:
            print ('本次爬取未完成，错误为：%s' % e)
        finally:
            print ('本次爬取了%i条数据' % len(self.rs))

a = zhihu_indexpage()
a.indexpage_spider()