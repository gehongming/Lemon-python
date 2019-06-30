import sys

sys.path.append('./')  #获取project 根目录,jenkits执行需要
print(sys.path)
import HTMLTestRunnerNew
import unittest
from week_8.common import contants


discover = unittest.defaultTestLoader.discover(contants.case_dir, pattern='test*.py')

with open(contants.reports_html+'/test3.html', 'wb+') as files:
            runner = HTMLTestRunnerNew.HTMLTestRunner(
                stream=files,
                verbosity=1,
                title='20190411py15测试报告',
                description='借口测试报告',
                tester='冥鴻')
            runner.run(discover)




















