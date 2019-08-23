import datetime
import pandas as pd
import numpy as np

# 日期检查函数
def date_input():
    while True:
        try:
            input_date = input('日期：')
            year_location = input_date.find('-')
            input_year = input_date[:year_location]
            month_location = input_date.find('-', year_location+1)
            input_month = input_date[year_location+1 : month_location]
            input_day = input_date[month_location+1 : ]
            rs_input_date = datetime.datetime.strptime(input_year+input_month+input_day, '%Y%m%d')
            return rs_input_date
            break
        except Exception as err:
            print (err)
            print("日期格式为：年年年年-月月-年年")

# 根据输入日期，增量更新损益表
op_bs = open('c:/users/suhao.xu/desktop/asset&liability.txt', 'r')
bs = [i.split() for i in op_bs]
bs_rs = []
for i in range(len(bs)):
    if i==0:
        bs_head = bs[i]
    else:
        bs_rs.append(bs[i])
        bs_date = bs_rs[i-1][0]
        bs_rs[i-1][0] = datetime.datetime.strptime('2019年'+bs_date, '%Y年%m月%d日')
op_bs.close()
df_bs = pd.DataFrame(np.array(bs_rs), columns = bs_head)
print (df_bs)


op_cashflow = open('c:/users/suhao.xu/desktop/in&outcome.txt', 'r')
cf = [i.split() for i in op_cashflow]
cf_rs = []
for i in range(len(cf)):
    if i == 0:
        cf_head = cf[i]
    else:
        cf_rs.append(cf[i])
        cf_date = cf_rs[i-1][5]
        cf_rs[i-1][5] = datetime.datetime.strptime('2019年'+cf_date, '%Y年%m月%d日')
        for j in range(len(cf_rs[i-1])-2):
            cf_rs[i-1][j+1] = float(cf_rs[i-1][j+1])
op_cashflow.close()
df_cf = pd.DataFrame(np.array(cf_rs), columns=cf_head)
print(df_cf)

cf_income = df_cf['收入/w'].groupby(df_cf['交易日期']).sum()
cf_outcome = df_cf['支出/w'].groupby(df_cf['交易日期']).sum()
cf_receivable = df_cf['应收账款/w'].groupby(df_cf['交易日期']).sum()
cf_payable = df_cf['应出账款/w'].groupby(df_cf['交易日期']).sum()
print (cf_income)

# df_full = pd.merge(df_bs, df_cf, left_on='结算日期', right_on='交易日期')
# print (df_full['应收账款/w'])
print('您想从哪天开始更新？（日期格式为：年年年年-月月-年年）')
input_date=date_input()
asset = (df_bs.loc[df_bs['结算日期']==input_date, '资产']).astype('float')
liability = df_bs.loc[df_bs['结算日期']==input_date, '负债'].astype('float')
net_asset = df_bs.loc[df_bs['结算日期']==input_date, '净资产'].astype('float')
print (asset)
print (liability)
print (net_asset)