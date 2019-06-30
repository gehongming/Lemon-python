from selenium import  webdriver
driver= webdriver.Chrome()
driver.get("https://www.ketangpai.com/Course/Homework/courseid/MDAwMDAwMDAwMLOspd2Gz79r.html")

# ===元素定位练习+等待===课堂派系统当中，你能看到的元素都定位一下==用我们上课讲的内容===
# 截至：05月27日  23:59 下载讨论内容展示词云
# 格式：
# #备注（哪个页面哪个元素）
# 定位代码
#
# 多复习一下等待的用法。

#备注：课堂页面 课堂按钮
driver.find_element_by_xpath('//a[@class="active"]')
#备注：课堂页面 私信按钮
driver.find_element_by_xpath('//a[text()="私信"]')
#备注：课堂页面 私信按钮
driver.find_element_by_xpath('a[text()="文库"]')
#备注：课堂页面 课程资源按钮
driver.find_element_by_xpath('//a[text()="课程资源"]')
#备注：课堂页面 加入课程按钮
driver.find_element_by_xpath('//div[@class="chuangjiankctop"]')'
#备注：课堂页面 通知按钮
driver.find_element_by_xpath('//img[@alt="通知"]')
#备注：课堂页面 课程排序按钮
driver.find_element_by_xpath('//a[contains(text(),"课程排序")]')
#备注：课堂页面 归档管理按钮
driver.find_element_by_xpath('//a[contains(text(),"归档管理")]')
#备注：课堂页面 作业标题
driver.find_element_by_xpath('//li[contains(@title,"元素定位练习+等待")]')
#备注：课堂页面 开通vip按钮
driver.find_element_by_xpath('//div[@class="close-vip"]')
#备注：课堂页面 作业链接
driver.find_element_by_xpath('//a[contains(text(),"元素定位") and contains(@href,"/Homework")]')
#备注：课堂页面 作业链接
driver.find_element_by_xpath('//li[contains(@title,"0511")]/preceding-sibling::li[contains(@title,"元素定位")]')
#备注：课堂派首页 首页按钮
driver.find_element_by_xpath('//a[text()="首页"]')
#备注：课堂派首页 移动端按钮
driver.find_element_by_xpath('//a[text()="首页"]/following-sibling::a[text()="移动端"]')
#备注：课堂派首页 解决方案按钮
driver.find_element_by_xpath('//a[text()="首页"]/following-sibling::div[@id="solutiontop"]/a[text()="解决方案"]')
#备注：课堂派首页 会员权益按钮
driver.find_element_by_xpath('//a[text()="首页"]/following-sibling::a[text()="会员权益"]')
#备注：课堂派首页 帮助中心按钮
driver.find_element_by_xpath('//a[text()="首页"]/following-sibling::a[text()="帮助中心"]')
#备注：课堂派首页 进入课堂派按钮
driver.find_element_by_xpath('//a[@href="/Main/index.html"]')
#备注：课堂派首页 免费注册按钮
driver.find_element_by_xpath('//a[@class="reg-btn"]/parent::div/a[@class="reg-btn"]')
#备注“提交作业页面 提交作业tap
driver.find_element_by_xpath('//a[@class="active"]')
#备注“提交作业页面 作业讨论tap
driver.find_element_by_xpath('//a[@class="active"]/following-sibling::a[text()="作业讨论"]')
##备注“提交作业页面 输出文件按钮
driver.find_element_by_xpath('//div[@id="rt_rt_1dbnergemg3n1sd8hssg0b14kr1"]/preceding-sibling::div[text()="上传文件"]')
##备注“提交作业页面 提交按钮
driver.find_element_by_xpath('//a[text()="提交"]')
##备注“提交作业页面 查看谁提交按钮
driver.find_element_by_xpath('//p[text()="查看谁交了"]')
##备注“提交作业页面 提交日志按钮
driver.find_element_by_xpath('//a[text()="查看提交日志"]')
#备注：作业提交页面 帮助按钮
driver.find_element_by_xpath('//a[@class="help-icon help-icon-ques"]')