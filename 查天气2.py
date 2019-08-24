import requests
import json

try:
    while True:
        input_city = input('请输入城市，回车退出\n')
        if input_city=='':
            exit()
        else:
            url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' % input_city
            req = requests.get(url)
            req.encoding = 'utf-8'
            wether_data = json.loads(req.text)
            if wether_data['status'] ==1000:
                print (wether_data['data']['forecast'][0]['date'])
                print(wether_data['data']['forecast'][0]['high'])
                print(wether_data['data']['forecast'][0]['low'])
                print(wether_data['data']['forecast'][0]['type'])
            else:
                print ('未获得')
except Exception as e:
    print('查询失败')
    print('失败原因：%s' % e)