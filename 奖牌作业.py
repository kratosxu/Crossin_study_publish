# coding=GBK
import pandas as pd
import numpy as np
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class medal_status:

    def __init__(self, country):
        self.medal_status = pd.read_csv('medal_status.csv', header = 0, index_col = 0, encoding = 'GBK')
        self.country_name = country
        self.goldmedal = self.medal_status['金牌'].loc[country]
        self.silvermedal = self.medal_status['银牌'].loc[country]
        self.bronzemedal = self.medal_status['铜牌'].loc[country]
        self.totalmedal = self.medal_status['总奖牌'].loc[country]

    def show_countries(self, order_class):
        if order_class == 'bygold':
            new_status = self.medal_status.sort_values(by = '金牌', ascending = False)
            print(new_status)
        elif order_class == 'bytotal':
            new_status = self.medal_status.sort_values(by='总奖牌', ascending=False)
            print(new_status)
        else:
            print ('没有该排序方法，请确认后重新输入（按总奖牌数展示请输入"bytotal"; 按金牌数展示请输入“bygold”）')


    def edit_medal(self):
        first_place = input('该项目获金牌的国家是：')
        second_place = input('该项目获银牌的国家是：')
        third_place = input('该项目获铜牌的国家是：')
        self.medal_status['金牌'].loc[first_place] += 1
        self.medal_status['总奖牌'].loc[first_place] += 1
        self.medal_status['银牌'].loc[second_place] += 1
        self.medal_status['总奖牌'].loc[second_place] += 1
        self.medal_status['铜牌'].loc[third_place] += 1
        self.medal_status['总奖牌'].loc[third_place] += 1
        self.medal_status.to_csv('medal_status.csv', index = True, encoding = 'GBK')


a = medal_status('中国')
a.edit_medal()
a.show_countries('bytotal')

