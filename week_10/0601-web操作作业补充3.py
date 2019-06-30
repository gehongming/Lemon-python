from  selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from week_10.wait import Wait
from selenium.webdriver.common.keys import Keys
import  time
from selenium.webdriver.common.by import By
from week_10.putfile import upload

driver=webdriver.Chrome()
driver.maximize_window()#窗口最大化
driver.get('https://www.12306.cn')

a=Wait(driver)
time.sleep(2)
#选择出发地
chufa=a.yuansu_wait(By.ID,'fromStationText')
chufa.click()
chufa.send_keys('南京南',Keys.ENTER)
#选择到达地
daoda=a.yuansu_wait(By.ID,'toStationText')
daoda.click()
daoda.send_keys('北京市',Keys.ENTER)
#选择时间，并登录
js_pha = 'var a = document.getElementById("train_date");' \
         'a.readOnly = false;' \
         'a.value = "2019-06-05";' \
         'document.getElementById("search_one").click();'

driver.execute_script(js_pha)
time.sleep(3)
driver.quit()