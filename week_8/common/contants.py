import os

#h获取当前week_8
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
case_file=os.path.join(base_dir,'data','testcase.xlsx')
# print(case_file)

global_file = os.path.join(base_dir, 'config', 'global.conf')
# print(global_file)

online_file = os.path.join(base_dir, 'config', 'online.conf')
# print(online_file)

test_file = os.path.join(base_dir, 'config', 'test.conf')
# print(test_file)
#测试报告txt
reports_text=os.path.join(base_dir,'reports','text3.txt')
# print(reports_text)
#测试报告html
reports_html=os.path.join(base_dir,'reports')
# print(reports_html)
#测试目录
case_dir=os.path.join(base_dir,'testcases')
# print(case_dir)
#日志目录
log_dir=os.path.join(base_dir,'log')
# print(log_dir)
