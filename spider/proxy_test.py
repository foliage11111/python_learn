# -*- coding: utf8 -*-
__author__ = 'zr'
#"测试是否成功"  http://ip.zdaye.com/
#http://www.whatismyip.com.tw/ 查看自己的ip
import urllib2
import urllib
import time
import json
url_test = 'http://www.whatismyip.com.tw'
url_target = 'http://www.woying.com/kaijiang/ssq'
url_proxy = '27.38.152.195:9797'
headers = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'

# req_proxy= urllib2.Request(url_target)
# req_proxy.set_proxy(url_proxy,'http')
# req_proxy.add_header('User-Agent',headers)
# urllib2.urlopen(req_proxy)
#这次试用opener来代替urlopen，看看有什么不同
proxys_handler=urllib2.ProxyHandler({'http':url_proxy})
opener1=urllib2.build_opener(proxys_handler)
opener1.addheaders = [('User-agent', headers)]
urllib2.install_opener(opener1)

response1 = urllib2.urlopen(url_test)

print response1.getcode()
html1 = response1.read()

print html1

