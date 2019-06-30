# 1：自己做好梳理和笔记
# 2：为我们3-12号写的http_request 请求类，写4条用例，要求利用unittest进行单元测试 ，并且用老师教的3个方法 分别去加载用例执行
# 3：4条用例里面要求有2个正常用例 2个异常用例
#

# G = w_1(url, main)
# a = G.http_request('post')
# print(a)
# G = w_1(url, main)
# b = G.http_request('get')
# print(b)

import  unittest
from requeste_http import Requeste_http



class TestCase(unittest.TestCase):
    def test_001 (self): #测试get请求成功
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        main = {'mobilephone': '18688773467', 'pwd': '123456'}
        print('this is TEST001')
        expected='登陆成功'
        res=Requeste_http(url,main).http_request('get')
        self.assertIn = (expected, res)
    def test_002(self): #测试get请求失败
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        main = {'mobilephone': '', 'pwd': '123456'}
        print('this is TEST002')
        expected='登陆成功'
        res=Requeste_http(url,main).http_request('get')
        self.assertNotIn=(expected,res)
    def test_003(self): #测试post请求成功
        url= 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        main = {'mobilephone': '18688773467', 'pwd': '123456'}
        print('this is TEST003')
        expected='登陆成功'
        res = Requeste_http(url, main).http_request('post')
        self.assertIn=(expected,res)
    def test_004(self):   #测试post请求失败
        url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        main = {'mobilephone': '18688773467', 'pwd': '123456324'}
        print('this is TEST004')
        expected='登陆成功'
        res=Requeste_http(url,main).http_request('post')
        self.assertNotIn=(expected,res)