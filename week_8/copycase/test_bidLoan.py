import json
import unittest

from ddt import ddt, data, unpack  # 装饰器
from common import openexcel
from common.http_request import HttpSessions

from common import contants


@ddt
class BidLoan(unittest.TestCase):
    excel = openexcel.DoExcel(contants.case_file, 'bidLoan')
    cases = excel.read()
    @classmethod
    def setUpClass(cls):
        cls.http_request= HttpSessions()

    @data(*cases)
    @unpack
    def test_bidLoan(self,url,method,data,expected,case_id,title,result):
        resp=self.http_request.http_request(method,url,data)# 实际值
        resp2=json.loads(resp)['code']#转换成字符串
        print('''用例编号{}，用例标题{}'''.format(case_id,title))
        try:
            self.assertEqual(expected,int(resp2))
            self.excel.write(int(case_id) + 1, resp, 'PASS')
        except AssertionError as e:
            self.excel.write(int(case_id) + 1,resp, 'FALSE')
    @classmethod
    def tearDownClass(cls):

        cls.http_request.close()