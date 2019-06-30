from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from week_10.wait import Wait
from selenium.webdriver.common.keys import Keys
import  time
from selenium.webdriver.common.by import By
from week_10.putfile import upload


driver=webdriver.Chrome()
driver.get('https://ke.qq.com/')

a=Wait(driver)
ac = ActionChains(driver)
driver.maximize_window()#窗口最大化

login=a.yuansu_wait(By.ID,'js_login')
login.click()

#选择qq
check_qq=a.yuansu_wait(By.XPATH,'//a[@data-type="1"]')
check_qq.click()
#切换iframe
iframe=a.iframe('login_frame_qq')
#选择账号登录
check_zh=a.yuansu_wait(By.ID,'switcher_plogin')
check_zh.click()
#输入qq号
qq=a.yuansu_wait(By.ID,'u')
qq.send_keys('1010562639')
#输入密码
password=a.yuansu_wait(By.ID,'p')
password.send_keys('*******')
#登录 login_button
password=a.yuansu_wait(By.ID,'login_button')
password.click()

driver.close()