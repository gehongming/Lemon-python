import json
import unittest
from ddt import ddt, data, unpack  # 装饰器
from week_9.common import do_mysql
from week_9.common import openexcel
from week_9.common.webservice_request import WebService
from week_9.common.context import Context
from week_9.common import contants
from week_9.common import log
import warnings
logger = log.get_logger(__name__)


@ddt
class RegisterCase(unittest.TestCase):
    excel = openexcel.DoExcel(contants.case_file, 'sendMCode')
    cases = excel.read()


    def setUp(self):
        logger.info('准备测试前置')
        self.http_request= WebService()
        self.mysql= do_mysql.DoMysql()
        self.context = Context()
        warnings.simplefilter("ignore", ResourceWarning)
    @data(*cases)
    @unpack
    def test_sendMCode(self,url,data,method,expected,case_id,title,result,check_sql):
        logger.info('开始测试：{}'.format(title))
        logger.info('请求是:{}'.format(data))

        resp=self.http_request.webservice(url,data,method)# 实际值
        # resp2=json.dumps(resp,ensure_ascii=False) #转换成字符串
        try:
            self.assertIn(expected,resp)
            result = 'PASS'
            if check_sql is not None:
                sql = eval(check_sql)['sql1']
                Fverify_code = self.mysql.fetch_one(sql)
                logger.info('验证码是：{}'.format(Fverify_code[2]))
        except AssertionError as e:
            result = 'FALSE'
            logger.error("报错了，{0}".format(e))
            raise e
        finally:
           logger.info('响应结果是：{}'.format(result))
           self.excel.write(int(case_id) + 1, str(resp), result)
           logger.info('结束测试：{0}'.format(title))
        def tearDown(self):
            self.mysql.close()

