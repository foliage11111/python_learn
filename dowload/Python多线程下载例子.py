#/ust/local/bin/python
#-*- coding:utf-8 -*-
'''
@QQ: 1532206263
'''
from __future__ import print_function
import os
import urllib2
from threading import Thread

class DownloadThread(Thread):
    """
    一个简单的多线程下载文件的例子
    """
    
    def __init__(self, url, name):
        """初始化线程"""
        Thread.__init__(self)
        self.name = name
        self.url = url
    
    def run(self):
        """Run the thread"""
        handle = urllib2.urlopen(self.url)
        fname = os.path.basename(self.url)
        with open("Bootstrap3.rar", "wb") as f_handler:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                f_handler.write(chunk)
        msg = "%s 已经从 %s 下载完成!" % (self.name,self.url)
        print(msg)
        
def main(urls):
    """
    Run the program
    """
    for item, url in enumerate(urls):
        name = "Thread %s" % (item+1)
        thread = DownloadThread(url, name)
        thread.start()
        
if __name__ == "__main__":
    urls = ["http://www.mycodes.net/do/job.php?job=down_encode&fid=154&id=7676&rid=7706&i_id=5333&mid=106&field=softurl&ti=0"]
    main(urls)