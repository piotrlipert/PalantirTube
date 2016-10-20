# -*- coding: utf-8 -*-

import SeleniumControl
import time
import random
class Palantir:
    def __init__(self):
        self.s = SeleniumControl.SeleniumControl()
    
    
    
        
        

    def createSearchTerms(self,gamelist):
        searchTerms = []
        for x in gamelist:
            searchTerms.append(x)
            #searchTerms.append(x + " longplay")
            #searchTerms.append(x + " gameplay")
            #searchTerms.append(x + " review")
            #searchTerms.append(x + " let's play")
            #searchTerms.append(x + " walkthrough")
            #searchTerms.append(x + " pt1")
            #searchTerms.append(x + " part 1")
            #searchTerms.append(x + " quick look")
        return searchTerms
            
       
       
    def getChannelLinks(self):
        channellinks = self.s.driver.find_elements_by_class_name("g-hovercard")
        return channellinks
        
        
    
    def openSearch(self,searchterm):
        self.s.noProxy()
        self.s.openUrl("https://www.youtube.com/results?q=" + searchterm + "&sp=CAMSBAgFEAE%253D")

        for z in range(10):
            
            for x in self.getChannelLinks():
                if not self.isOnList(x.get_attribute("href")):
                    self.saveLink(x.get_attribute("href"))
            
            self.nextPage()
            time.sleep(random.randint(5,6) + random.random())
        
    def nextPage(self):
        el = self.s.driver.find_elements_by_class_name("yt-uix-button-content")
        for x in el:
            if x.text.find("Nast") != -1:
                x.click()
            else:
                pass

    def saveLink(self,link):
        f = open("data/YoutubeChannels.Oink",'a')
        f.write(link+"\n")
        f.close()
        
    def isOnList(self,link):
        f = open("data/YoutubeChannels.Oink",'r')
        data = f.read().split("\n")
        f.close()
        
        if link in data:
            return True
        return False
            
    
gamelist = ["\"smart wallet\"", "\"unboxing gadgets\"", "\"unboxing wallet\"", "\"slim wallet\"", "\"ultimate slim wallet\"", "\"unboxing slim wallet\"", "\"unboxing smart wallet\"", "\"unboxing ultimate slim wallet\"", "\"wallet tracker\"", "\"wallet finder\""]
#gamelist = ["indie games","dwarf fortress","adom","enter the gungeon","broforce"]

#gamelist = gamelist + ["full throttle", "psychonauts 2","deponia", "botanicula"]
#gamelist = gamelist + ["loom game", "the whispered world","flight of the amazon queen"]
#gamelist = gamelist + ["armikrog", "the last express game","raymen origins"]
#gamelist = gamelist + ["shantae and the pirate curse", "trine","raymen legends"]
#gamelist = gamelist + ["alladin game", "cave story","karoshii game"]
#gamelist = gamelist + ["undertale", "stardew valley","earthworm jim"]
#gamelist = gamelist + ["super meat boy", "braid","earthworm jim"]
#gamelist = gamelist + ["undertale", "stardew valley","bad mojo redux"]
#gamelist = gamelist + ["sanitarium game", "amnesia game"]


p = Palantir()
searchterms = p.createSearchTerms(gamelist)
    
for x in searchterms:
    p.openSearch(x)

        
        

