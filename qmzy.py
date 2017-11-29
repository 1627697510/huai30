# -*- coding:utf-8 -*-
#爬取内涵段子爬虫类
import urllib
import urllib2
import re



user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
headers = { 'User-Agent' : user_agent }

for i in range(2,60):
    url = 'http://www.neihan8.com/article/index_'+str(i)+'.html'
    #print url


    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()

    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    '''
    #爬取内涵段子的标题
    content_pattern = re.compile('<div class="text-column-item box box-790">.*?<h3><a.*?>(.*?)</a></h3>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #爬取内涵段子的内容
    content_pattern = re.compile('<div class="text-column-item box box-790">.*?<div class="desc">(.*?)</div>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #内涵段子的点赞数
    content_pattern = re.compile('<div class="good" >(.*?)</div>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #内涵段子的踩数
    content_pattern = re.compile('<div class="bad" >(.*?)</div>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #内涵段子的浏览人数
    content_pattern = re.compile('<div class="view" >(.*?)</div>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    '''
   


all_pattern = re.compile('<div class="text-column-item box box-790">.*?<h3><a.*?>(.*?)</a></h3>.*?<div class="desc">(.*?)</div>.*?<div class="good" >(.*?)</div>.*?<div class="bad" >(.*?)</div>.*?<div class="view" >(.*?)</div>',re.S)
all_list = re.findall(all_pattern, html)
for item in all_list:
    print "title:" + item[0]
    print "content:" + item[1]
    print "Point of praise:" + item[2].strip()
    print "Step number:" + item[3]
    print "Browse count:" + item[4]
    
    print "-----------------"

#输入回车加载下一页，输入Q退出
    input = raw_input()
    if input == "":
        print "nextPage:"
        continue
    elif input =="Q":
        break



