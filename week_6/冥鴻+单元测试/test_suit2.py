import  unittest
import HTMLTestRunnerNew

suite=unittest.TestSuite()
#通过loader来加载用例  通过测试类名来加载用例
from w_1 import *


loader= unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCase))


# with open('test2.html','wb') as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(
#         stream=file,
#         verbosity=2,
#         title='20190324py15测试报告',
#         description='httpq请求测试报告',
#         tester='冥鴻')
#     runner.run(suite)


# 执行用例--unittest版本
with open('test2.txt','w') as file:
    runner=unittest.TextTestRunner(stream=file,verbosity=2)#创建一个对象来执行用例
    runner.run(suite)