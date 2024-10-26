#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

class scrapeBot:
    def __init__(self,link):
        self.link = link

    def makeReq(self, link):
        # check/print status code (success = 200)
        self.r = requests.get(self.link)
        print(self.r)
    
    def makeSoup(self, request):
        #Parse request content with BS4 
        self.soup = BeautifulSoup(self.r.content, 'html.parser')
        self.soup.prettify()
        print(self.soup)

if __name__ == "__main__":
    link = 'https://en.wikipedia.org/wiki/Old_School_Runescape'
    # Create scrape bot object
    sb1 = scrapeBot(link)
    sb1.makeReq(link)
    sb1.makeSoup(sb1.r)
