import json
import unittest
from ddt import ddt, data, unpack  # 装饰器
from common import openexcel
from common.http_request import HttpSessions
from common.log import LogTools
from common import contants
import warnings


@ddt
class Add(unittest.TestCase):
    excel = openexcel.DoExcel(contants.case_file, 'add')
    cases = excel.read()
    @classmethod
    def setUpClass(cls):
        cls.http_request= HttpSessions()
        warnings.simplefilter("ignore", ResourceWarning)
    @data(*cases)
    @unpack
    def test_add(self,url,method,data,expected,case_id,title,result,check_sql):
        data = self.context.replace(json.dumps(data))
        LogTools().info('用例标题是:{}'.format(title))
        LogTools().info('请求是:{}'.format(data))
        resp=self.http_request.http_request(method,url,data)# 实际值
        resp2=json.loads(resp)['code']#转换成字符串
        print('''用例编号{}，用例标题{}'''.format(case_id,title))
        try:
            self.assertEqual(expected,int(resp2))
            result = 'PASS'
        except AssertionError as e:
            result = 'FALSE'
            raise e
        finally:
            LogTools().info('响应结果是：{}'.format(result))
            self.excel.write(int(case_id) + 1, resp, result)
    @classmethod
    def tearDownClass(cls):

        cls.http_request.close()