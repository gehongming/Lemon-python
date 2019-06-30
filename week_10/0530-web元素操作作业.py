from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #a按键
from selenium.webdriver.support.select import Select #下拉框
from selenium.webdriver.support.wait import WebDriverWait #等待
from selenium.webdriver.support import expected_conditions as EC #条件
from selenium.webdriver.common.by import By #定位
from week_10.wait import Wait
from selenium.webdriver.common.keys import Keys #按键操作
import  time

driver=webdriver.Chrome()
driver.get("https://www.ketangpai.com/")

a=Wait(driver)
ac = ActionChains(driver)
#点击登录
denglu=a.yuansu_wait(By.XPATH,'//a[@class="login"]')
denglu.click()
#输入手机号
phone=a.yuansu_wait(By.XPATH,'//input[@type="text"and@name="account"]')
phone.send_keys("17625188013")
#输入密码
name=a.yuansu_wait(By.XPATH,'//input[@type="password"]')
name.send_keys('woaini@1314')
#登录
login=a.yuansu_wait(By.XPATH,'//div[@class="padding-cont pt-login"]//a[@class="btn-btn"]')
login.click()

#关闭弹框
close=a.yuansu_wait(By.XPATH,'//a[@class="close"]')
close.click()
#休息下
time.sleep(0.5)

#进入所在班级
into_class = a.yuansu_wait(By.XPATH, '//strong//a[@href="/Course/Homework/courseid/MDAwMDAwMDAwMLOspd2Gz79r.html"]')
into_class.click()

#查看成绩
Viewing_results = a.yuansu_wait(By.XPATH, '//a[contains(@href,"MDAwMDAwMDAwMLSGx92Huclt.html")and text()="查看成绩"]')
Viewing_results.click()
time.sleep(0.2)
#获取成绩
# store=driver.find_element_by_xpath('//p[@class="score fr"]//span')
store=a.get_element('//p[@class="score fr"]//span')
print('我的成绩{}'.format(store.text))

#获取优秀学生名单
# students= a.get_elements('//p[@class="share-name"]')
students=a.get_elements('//p[@class="share-name"]')
# print(students)
for i in  students:
    i=i.get_attribute('textContent')
    print('三好学生是：{}'.format(i))
#去讨论
taolun=a.yuansu_wait(By.XPATH,'//a[text()="作业讨论"]')
taolun.click()
#休息一下
time.sleep(0.2)
#添加评论
pinglun=a.yuansu_wait(By.XPATH,'//p[text()="添加评论"]')
pinglun.click()
#输入评论
shuru=a.yuansu_wait(By.XPATH,'//textarea[@class]')
shuru.send_keys('you are my hero {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#取消
fasong=a.yuansu_wait(By.XPATH,'//div[@class="opt-btn fr"]//a[@class="cancel"]')
fasong.click()
#返回主页面
re=a.yuansu_wait(By.ID,'return-course')
re.click()
#休息一下
time.sleep(0.5)
#点击同学
stu=a.yuansu_wait(By.XPATH,'//li[@class="li5"]//a')
stu.click()
time.sleep(0.5)
#打开同学列表
open=a.yuansu_wait(By.XPATH,'//li[@class="all"]')
open.click()
time.sleep(5)
#选择同学
check=driver.find_element_by_xpath('//p[text()="北京-盈盈"]//parent::li')
ac.move_to_element(check)
ac.perform()
#点击对话框
cl=a.yuansu_wait(By.XPATH,'//p[text()="北京-盈盈"]/following-sibling::a[@class="call"]')
cl.click()
time.sleep(0.2)
#输入发送语句
dianji=a.yuansu_wait(By.XPATH,'//textarea[@class]')
dianji.send_keys('想你问好')#,#Keys.CONTROL,Keys.ENTER)
# 关闭信息框
cl=a.yuansu_wait(By.XPATH,'//span[@class="layui-layer-setwin"]//a')
cl.click()
#搜索同学
time.sleep(0.2)
se=a.yuansu_wait(By.XPATH,'//input[@placeholder="姓名、学号"]')
se.send_keys('1505',Keys.ENTER)
#搜索结果
result=a.get_element('//h3//span[text()="1505"]')
print('搜索结果是{}'.format(result.get_attribute('textContent')))

driver.close()