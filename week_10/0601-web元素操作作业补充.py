from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from week_10.wait import Wait
from selenium.webdriver.common.keys import Keys
import  time
from selenium.webdriver.common.by import By
from week_10.putfile import upload


driver=webdriver.Chrome()
a=Wait(driver)
ac = ActionChains(driver)
driver.maximize_window()#窗口最大化
driver.get("https://www.ketangpai.com/")



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
into_class = a.yuansu_wait(By.XPATH, '//strong//a[@href="/Course/Homework/courseid/MDAwMDAwMDAwMLOsvZeIuauv.html"]')
into_class.click()
#点击上传作业
put=a.yuansu_wait(By.XPATH,'//a[@class="sc-btn"]')
put.click()

time.sleep(0.2)
#点击上传文件
file=a.yuansu_wait(By.XPATH,'//a[@class="sc-btn webuploader-container"]')
file.click()
time.sleep(1.5)
#选择文件
upload('E:\Downloads\为我欢喜为我忧')
time.sleep(1.5)
#提交
tijiao=a.yuansu_wait(By.XPATH,'//a[@class="tj-btn active"]')
tijiao.click()

driver.close()







