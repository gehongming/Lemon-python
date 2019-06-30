import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir =  os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")



htmlreport_dir =  os.path.join(base_dir,"Outputs/reports")

log_dir =  os.path.join(base_dir,"OutPuts/log")
print(log_dir)
# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")
# print(screenshot_dir)
#h获取当前week_9
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)


global_file = os.path.join(base_dir, 'config', 'global.conf')
# print(global_file)

online_file = os.path.join(base_dir, 'config', 'online.conf')
# print(online_file)
