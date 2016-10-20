# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 15:36:47 2016

@author: dziki
"""

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
        
        
    
    def browseChannel(self,channel):
        self.s.openUrl(channel + "/videos/")
        time.sleep(1)

        score = self.calculateScore()
        subs = self.getSubs()
        self.s.openUrl(channel + "/about")
        time.sleep(1)
                
        links = self.getLinks()
        
        twitterlink = "notwitter"
        facebooklink = "nofacebook"
        linkstring = ""
        for x in links:
            if x.find("twitter") != -1:
                twitterlink = x
            elif x.find("facebook") != -1:
                facebooklink = x
            
            else:
                linkstring = linkstring + ";" + x
        linkstring = linkstring[1:]
        
        hasemail = self.hasEmail()         
        
        savestring = channel + "," + str(score) + "," + str(subs) + "," + linkstring + "," + twitterlink + "," + facebooklink + "," + hasemail
        
        self.saveLink(savestring)
        
    def hasEmail(self):
        if self.s.driver.page_source.find(u"Wyświetl adres e-mail") != -1:
            return "has email"
        return "no email"
    def getLinks(self):
        links = []
        el = self.s.driver.find_elements_by_class_name("about-channel-link")
        for x in el:
            links.append(x.get_attribute("href"))
        return links

    def calculateScore(self):
        score = 0
        gamelist = ["indie games","dwarf fortress","adom","enter the gungeon","broforce"]
        gamelist = gamelist + ["full throttle", "psychonauts 2","deponia", "botanicula"]
        gamelist = gamelist + ["loom game", "the whispered world","flight of the amazon queen"]
        gamelist = gamelist + ["armikrog", "the last express game","raymen origins"]
        gamelist = gamelist + ["shantae and the pirate curse", "trine","raymen legends"]
        gamelist = gamelist + ["alladin game", "cave story","karoshii game"]
        gamelist = gamelist + ["undertale", "stardew valley","earthworm jim"]
        gamelist = gamelist + ["super meat boy", "braid","earthworm jim"]
        gamelist = gamelist + ["undertale", "stardew valley","bad mojo redux"]
        gamelist = gamelist + ["sanitarium game", "amnesia game"]
        gamelist = gamelist + ["point and click", "adventure game"]
        text = self.s.driver.page_source
        for x in gamelist:
            if text.find(x) != -1:
                score = score + 1
                
        return score

    def getSubs(self):
        e = self.s.driver.find_elements_by_class_name("yt-uix-tooltip")
        for x in e:
            if x.text != "":
                return x.text.replace(" ","")
        
        
    def nextPage(self):
        el = self.s.driver.find_elements_by_class_name("yt-uix-button-content")
        for x in el:
            if x.text.find("Nast") != -1:
                x.click()
            else:
                pass

    def saveLink(self,link):
        f = open("data/YoutubeChannelsParsed.Oink",'a')
        f.write(link+"\n")
        f.close()
        
    
            
    



p = Palantir()
f = open("data/YoutubeChannels.Oink",'r')
p.s.noProxy()

channels = f.read().split("\n")
f.close()

i = 0    
for x in range(0, len(channels)):
    print i
    p.browseChannel(channels[x])
    i = i + 1
    

        
        

