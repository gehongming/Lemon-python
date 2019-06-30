import  unittest
import HTMLTestRunnerNew
suite=unittest.TestSuite()#创建一个对象
#第一种添加用例方式

from w_1 import *
suite.addTest(TestCase('test_001'))
suite.addTest(TestCase('test_002'))
suite.addTest(TestCase('test_003'))
suite.addTest(TestCase('test_004'))

# with open('test.txt','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)#创建一个对象来执行用例
#     runner.run(suite)

# with open('test.html','wb') as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(
#         stream=file,
#         verbosity=2,
#         title='20190324py15测试报告',
#         description='http请求测试报告',
#         tester='冥鴻')
#     runner.run(suite)
runner=unittest.TextTestRunner() #创建一个对象执行用例
runner.run(suite)

