# -*- coding: utf8 -*-
__author__ = 'zr'
#模块化抓取双色球
import urllib2
import re

def get_ssq_by_spider(ssq_rul):
    #输入网址从网页抓取内容，并返回下载的全部内容

    header1 = {}
    header1['User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"
    req1 = urllib2.Request(ssq_rul)   ##req1 = urllib2.Request(urll,'',header1)
    req1.add_header('User-Agent',header1['User-Agent']) ##需要区别上面加header的方法，这里需要指定header里面某个关键字，然后增加字符串内容
    # req1.set_proxy('27.38.152.195:9797','http')
    response=urllib2.urlopen(req1)
    return response

def ssq_filter(response):
    #把response中抓到的内容转到新的fileter中
        contents=''
        switch1=False
        for i  in response.readlines():
             if i.strip()=='<tbody>':
              switch1=True
             if i.strip() == '</tbody>':
              switch1=False
             if switch1 :
                 contents=contents+i.strip()
        ##正则清理list
        ssq_list=re.findall(r'<td>\d{7}.*?"blue">\d{2}</td>', contents)
        #print ssq_list[0]
        ssq_dict = {}
        #字符串清洗,结果写入dict
        for k in ssq_list:
            str1=k[k.find('\"red\">')+6:k.find('</td><td class=\"blue\">')].replace('&nbsp;',',')+','+k[k.find('\"blue\">')+7:len(k)-5]
            temp_list=[int(x) for x in str1.split(',')]
            ssq_dict[k[4:11]]=temp_list
        return ssq_dict

#def compare_data():
    #跟数据库中的内容进行对比，返回需要插入的list

def spider_main():
    ssq_url = 'http://www.woying.com/kaijiang/ssqls/50.html'
    #后续新增网址re校验
    new50_list={}
    response = get_ssq_by_spider(ssq_url)
    if response.getcode() == 200 and response:
        new50_list=ssq_filter(response)
        #print new50_list
    else:
        print "数据抓取失败，不进行清洗"


spider_main()
