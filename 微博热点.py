import requests

url = 'https://weibo.com/a/hot/realtime'
wb_cookie = 'UOR=bj.expo.jiehun.com.cn,widget.weibo.com,bj.expo.jiehun.com.cn; SINAGLOBAL=1174967033686.698.1541553971382; ULV=1567046119442:2:1:1:3941678685999.0503.1567046119435:1541553971798; wvr=6; Ugrow-G0=5c7144e56a57a456abed1d1511ad79e8; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whr6OzlhRYTBBwfULXeWDKI5JpX5KMhUgL.Fo-RShqXSKnNeKq2dJLoIpzLxKqLBoBLB.-LxK-L12qL12Bt; ALF=1598681365; SSOLoginState=1567145366; SCF=AqU9ALO-8FBWAk_9E_yMwOKRqeyImY2NStd0WSgyg6BBjBl7hwM61PIWAahzkdxJocCKqW-affwUPjiKr_4rLMQ.; SUB=_2A25wbM3GDeRhGeNG71QV9SbLyjqIHXVTG7gOrDV8PUNbmtAKLRTXkW9NS0aZ-wzq492OiKRwFGuZekKo8XdFVIDV; SUHB=0nluHEzZcucTSz; YF-V5-G0=a5a6106293f9aeef5e34a2e71f04fae4; WBStorage=f54cf4e4362237da|undefined'
us_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
headers = {'user-agent': us_agent,
           'Cookie': wb_cookie}

req = requests.get(url, headers = headers)
req.encoding = 'utf8'
print (req.status_code)
with open ('weibohotpoint.html', 'w', encoding = 'utf8') as f:
    f.write(req.text)