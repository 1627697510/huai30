#��ȡ�ں�����_�ں���


# -*- coding:utf-8 -*-
import urllib
import urllib2
import re






user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'
headers = { 'User-Agent' : user_agent }


for i in range(1,3):
    url = 'http://www.neihan.net/tags/4_'+str(i)+'.html'
    print url

    
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    #��ȡ�ں����ӵı���
    content_pattern = re.compile('<span class="title"><a.*?>(.*?)</a></span>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #��ȡ�ں����ӵ�����
    content_pattern = re.compile('<dd class="content">(.*?)</dd>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #�ں����ӵ�����
    content_pattern = re.compile('<p class="user">.*?<a.*?>(.*?)</a>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #�ں����ӵĶ���
    content_pattern = re.compile('<a.*?title="��">.*?<div class="dingcai">.*?<span></span>.*?<i>(.*?)</i>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item
    #�ں����ӵĲ���
    content_pattern = re.compile('<a.*?title="��">.*?<div class="dingcai">.*?<span></span>.*?<i>(.*?)</i>', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item


#����س�������һҳ������Q�˳�
    input = raw_input()
    if input == "":
        print "nextPage:"
        continue
    elif input =="Q":
        break


