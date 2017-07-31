import requests

se=requests.Session()

url='http://202.204.48.66/'
data={
      "userName":"xxxxxxxx",
      "password":"xxxxx",
      "school_id":"xxxx"
     }

headers={
          'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
          'Accept-Encoding': 'gzip, deflate',
          'Accept-Language': 'en-US, en; q=0.8, zh-Hans-CN; q=0.5, zh-Hans; q=0.3',
          'Connection': 'Keep-Alive',
          'Host': '139.198.3.98',
          'Referer': 'http://139.198.3.98/sdjd/protalAction!loginrInit.action?wlanuserip=10.177.31.212&basip=124.128.40.39',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
          'X-Requested-With': 'XMLHttpRequest'
        }

content=se.post(url,data=data,headers=headers)

print(content.text)