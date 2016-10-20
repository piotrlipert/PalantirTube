# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Utility class to control and initialize Selenium Driver.

class SeleniumControl:
    def __init__(self):
        self.driver = None

# In case we need to use proxy (but we don't).
    def useProxy(self,proxy):
        if self.driver != None:
            self.closeDriver()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % proxy)   
        

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
 
 # Initialize the driver without proxy.
    def noProxy(self):
        if self.driver != None:
            self.closeDriver()
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
 
# I just like the name of my function better.
    def openUrl(self,url):
        self.driver.get(url)
        
# Same goes here.    
    def closeDriver(self):
        self.driver.close()

# Opens new tab in Chrome Selenium.
    def newTab(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 





#s.closeDriver()