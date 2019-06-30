# 1：作业安排：
# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码

import  requests
import json

class Requeste_http:
    def __init__(self,url,main):
        self.url=url
        self.main=main

    def http_request(self,GP):
        if GP=='get':
            return requests.get(self.url,self.main).text
        elif GP=='post':
            return  requests.post(self.url,data=self.main).text
        # return  ('响应报文:{}'.format(a.text))


if __name__=='__main__':
  url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
  main = {'mobilephone': '18688773467', 'pwd': '123456'}
  G=Requeste_http(url,main)
  a=G.http_request('post')
  print(a)
  G=Requeste_http(url,main)
  b=G.http_request('get')
  print(type(b))



