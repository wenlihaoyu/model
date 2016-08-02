# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:04:37 2016
网页请求
@author: lywen
文银龙，2016－07-13 增加日志logs功能，记录网页请求错误
"""
import urllib
import urllib2
import requests
import traceback
from log.logs import logs
from help.helper import timesleep

class Request(object):
      """
      网络请求
      """
      def __init__(self,url,headers={},data=None,timeout=10,urlencode=True):
          self.url     = url##网址
          self.headers = headers## headers
          if data is None:
              self.data = data
          else:
              if urlencode:
                 self.data    = urllib.urlencode(data) ## 参数
              else:
                  self.data = data
          self.timeout = timeout
          
      def setCookie(self,url):
         """
         设置Cookie
         """
         if self.headers is None:
             try:
                req = requests.session().post(url)
                if req.status_code==200:
                   self.headers = req.headers
                   self.cookies=req.cookies
             except:
                logs('requests','Request','__setCookie__',traceback.format_exc())  
             
        
      def post(self):
        """
        执行post请求
        """
        try:
           self.response  = requests.session().post(self.url,data = self.data,headers=self.headers)
           
        except:
            ###网络出现问题
            logs('requests','Request','post',traceback.format_exc()) 
            
        
      def urlopen(self): 
          """
          基本网页读取
          """
          req = urllib2.Request(self.url,data=self.data,headers=self.headers)
          try:
              
              self.response = urllib2.urlopen(req, timeout=self.timeout)
          except:
              
              logs('requests','Request','urlopen',traceback.format_exc())
          
          
     
          
def testRequestIsOk():
    """
    判断网通是否畅通
    """
    url = 'http://www.baidu.com'
    req = Request(url)
    req.urlopen()
    num=0
    while req.response.getcode()!=200:
          logs('requests','testRequestIsOk','url test','the net is bad!')
         
          num+=1
          if num>10:
              timesleep(10)
          else:
              timesleep(1)
              
    return True
          
          
        
           
        
        
             
             
            
