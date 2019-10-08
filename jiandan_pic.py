# -*- coding:GBK -*-
import requests
import re
from PIL import Image
from io import BytesIO
import time

from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

pic_url = 'http://jandan.net/ooxx/MjAxOTEwMDgtNQ==#comments'
pic_useragent = 'MoziMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
pic_cookie = '_ga=GA1.2.81925243.1569658593; _gid=GA1.2.934080477.1570496147; _gat_gtag_UA_462921_3=1'
headers = {'User-agent': pic_useragent,
           'Cookie': pic_cookie}
pic_get = requests.get(pic_url, headers = headers)

jiandan_text = BeautifulSoup(pic_get.text, 'lxml')

for i in range(len(jiandan_text.find_all('img'))):
    pic_url = 'https:'+jiandan_text.find_all('img')[i]['src']
    pic_content = requests.get (pic_url)
    image = Image.open(BytesIO(pic_content.content))
    print (pic_url)
    image.save('./jiandan_pics/%s' % re.findall(r'.*/(.*\.(jpg|gif|png))', pic_url)[0][0])
    time.sleep(5)