# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class SeleniumControl:
    def __init__(self):
        self.driver = None


    def useProxy(self,proxy):
        if self.driver != None:
            self.closeDriver()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % proxy)   
        chrome_options.add_argument("--load-extension=F:\programowanie\onering\moriagoblins")   

        #chrome_options.add_argument("--lang=en_US")   

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
 
    def noProxy(self):
        if self.driver != None:
            self.closeDriver()
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
 

    def openUrl(self,url):
        self.driver.get(url)
    
    
    
    def closeDriver(self):
        self.driver.close()
    
    def newTab(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 





#s.closeDriver()