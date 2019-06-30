from selenium import  webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#


class Wait:

    def __init__(self,driver):
        self.driver=driver

    def  yuansu_wait(self,style,element):
        locator=(style,element)
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locator))
        except TimeoutError:
            print("没有找到元素")
        else:
            return self.driver.find_element(*locator)
    def iframe(self,elemnet):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(elemnet))
    def get_elements(self,element):
        a=self.driver.find_elements_by_xpath(element)
        return a
    def get_element(self,element):
        b=self.driver.find_element_by_xpath(element)
        return b


