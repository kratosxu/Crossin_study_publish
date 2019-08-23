import requests
import json
import re

# url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'
# req = requests.get(url)
# req.encoding = 'utf-8'
# data = json.loads(req.text)
# print (type(data))
# print (data)

input_city = input('你想查哪个城市的天气？\n')
try:
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=%s' % input_city
    req = requests.get(url)
    req.encoding = 'utf-8'
    wether_data = json.loads(req.text)
    if wether_data['status'] ==1000:
        regex_high = re.compile(r'高温 (.+℃)')
        regex_low = re.compile(r'低温 (.+℃)')
        print (wether_data['data']['forecast'][0]['type'])
        print (regex_low.findall(wether_data['data']['forecast'][0]['low'])[0]
               +'~'+regex_high.findall(wether_data['data']['forecast'][0]['high'])[0])
    else:
        print ('没有找到该城市')
except Exception as e:
    print('查询失败')
    print('失败原因：%s' % e)