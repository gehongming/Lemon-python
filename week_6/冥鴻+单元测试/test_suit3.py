import  unittest
import HTMLTestRunnerNew
#通过loader来加载用例  通过模块来加载用例
suite=unittest.TestSuite()#创建一个对象

import  w_1   #调用模块
loader=unittest.TestLoader()   #用力的加载器
suite.addTest(loader.loadTestsFromModule(w_1)) #执行用例

# with open('test3.html','wb') as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(
#         stream=file,
#         verbosity=2,
#         title='20190324py15测试报告',
#         description='httpq请求测试报告',
#         tester='冥鴻')
#     runner.run(suite)


# 执行用例--unittest版本
with open('test3.txt','w') as file:
    runner=unittest.TextTestRunner(stream=file,verbosity=2)#创建一个对象来执行用例
    runner.run(suite)