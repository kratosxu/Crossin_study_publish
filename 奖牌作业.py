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
        self.goldmedal = self.medal_status['����'].loc[country]
        self.silvermedal = self.medal_status['����'].loc[country]
        self.bronzemedal = self.medal_status['ͭ��'].loc[country]
        self.totalmedal = self.medal_status['�ܽ���'].loc[country]

    def show_countries(self, order_class):
        if order_class == 'bygold':
            new_status = self.medal_status.sort_values(by = '����', ascending = False)
            print(new_status)
        elif order_class == 'bytotal':
            new_status = self.medal_status.sort_values(by='�ܽ���', ascending=False)
            print(new_status)
        else:
            print ('û�и����򷽷�����ȷ�Ϻ��������루���ܽ�����չʾ������"bytotal"; ��������չʾ�����롰bygold����')


    def edit_medal(self):
        first_place = input('����Ŀ����ƵĹ����ǣ�')
        second_place = input('����Ŀ�����ƵĹ����ǣ�')
        third_place = input('����Ŀ��ͭ�ƵĹ����ǣ�')
        self.medal_status['����'].loc[first_place] += 1
        self.medal_status['�ܽ���'].loc[first_place] += 1
        self.medal_status['����'].loc[second_place] += 1
        self.medal_status['�ܽ���'].loc[second_place] += 1
        self.medal_status['ͭ��'].loc[third_place] += 1
        self.medal_status['�ܽ���'].loc[third_place] += 1
        self.medal_status.to_csv('medal_status.csv', index = True, encoding = 'GBK')


a = medal_status('�й�')
a.edit_medal()
a.show_countries('bytotal')

