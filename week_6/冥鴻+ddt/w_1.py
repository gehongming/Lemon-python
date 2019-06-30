# G = w_1(url, main)
# a = G.http_request('post')
# print(a)
# G = w_1(url, main)
# b = G.http_request('get')
# print(b)

import  unittest
from requeste_http import Requeste_http
from ddt import ddt,data,unpack  #装饰器
from openexcel import w_2
import json





g = w_2('py15.xlsx', 'Sheet1')
a = g.read()

@ddt
class TestCase(unittest.TestCase):

    @data(*a)
    @unpack
    def test_get001(self,url,method,data,exp_data, case_id): #测试get请求成功
        print('请求地址是:{},请求的方式是：{}，传递的参数是：{}'.format(url, method, data))

        res=json.loads(Requeste_http(url,data).http_request(method))#实际值
        # self.assertIn = (exp_data, res)


        try:
            self.assertEqual(exp_data,res["msg"])
        except AssertionError as e:
            row=int(case_id)+1
            g.write_result(row,'failed')



    # @data(*[{'mobilephone': 18688773467, 'pwd': 123456, 'expected': '登陆成功'},
    #         {'mobilephone': 18688773467, 'pwd': 123456, 'expected': '登陆成功'},
    #         {'mobilephone': '', 'pwd': 123456, 'expected': '用户名或密码错误'},
    #         {'mobilephone': 18688773467, 'pwd': 13456, 'expected': '用户名或密码错误'}])
    # @unpack
    # def test_post002(self,mobilephone,pwd,expected): #测试get请求失败
    #     url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    #     main = {'mobilephone': mobilephone, 'pwd': pwd}
    #     res = Requeste_http(url, main).http_request('post')
    #     self.assertIn = (expected, res)
    #     print('this is postrequsets mobilephone is{},pwd is{},expected is{}'.format(mobilephone,pwd,expected))

    # def test_003(self): #测试post请求成功
    #     url= 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    #     main = {'mobilephone': '18688773467', 'pwd': '123456'}
    #     print('this is TEST003')
    #     expected='登陆成功'
    #     res = Requeste_http(url, main).http_request('post')
    #     self.assertIn=(expected,res)
    # def test_004(self):   #测试post请求失败
    #     url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    #     main = {'mobilephone': '18688773467', 'pwd': '123456324'}
    #     print('this is TEST004')
    #     expected='登陆成功'
    #     res=Requeste_http(url,main).http_request('post')
    #     self.assertNotIn=(expected,res)