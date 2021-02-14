#region import

import eel
import random
from bs4 import BeautifulSoup
import urllib.request
import re

#endregion

#Get url and title from random wiki url
def ReturnLink(link):
    with urllib.request.urlopen(link) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        return (response.url, soup.find(id="firstHeading").get_text())

#region Initialization

eel.init('web')
linkRandom = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"
likeBase = "https://fr.wikipedia.org"
global linkStart
global linkFinish
global linkActive 
listLinkToIgnore = [("","")]

#endregion

#Clean up the links captured
def CheckLinkToKeep(link, text):
    return link != None and not (link in listLinkToIgnore) and not (link.startswith('/w/index')) and not (link.startswith('http')) and not (link.startswith('#')) and not (link.startswith('/wiki/Cat%C3%A9gorie')) and not (link.startswith('/wiki/Portail:')) and not (link.startswith('/wiki/Fichier')) and not (link.startswith('/wiki/Aide')) and not (link.startswith('/wiki/Projet')) and not (link.startswith('/wiki/Discussion_Wikipédia:')) and not (link.startswith('/wiki/Sp%C3%A9cial:Ouvrages')) and not (link.startswith('/books.google.com/books')) and not (link.startswith('/wiki/Wikipédia:')) 
    
#Format tuple to string = "tuple0=tuple1" as JS don't support tuple
def TupleToJs(tuple):
    return tuple[0] + "=" + tuple[1]

#region GUI eel

#Get Set all links and return the link start 
#Also use to reset the game
@eel.expose
def getStartLink():
    global linkActive
    global linkFinish
    global linkStart
    linkStart = ReturnLink(linkRandom)
    linkFinish = ReturnLink(linkRandom)
    linkActive = linkStart
    eel.setStartLink(TupleToJs(linkStart))

#Filter list of links for next jump and return it
@eel.expose
def getLinks(link):
    link = link if "http" in link else likeBase + link
    linkActive = ReturnLink(link)
    listLink = [("","")]
    listLink.remove(("",""))

    with urllib.request.urlopen(linkActive[0]) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for anchor in soup.find_all(id="content"):

            #Get all the links in main content
            for a in anchor.findChildren("a") :
                if(a.get('href') != None) :
                    listLink.append((a.get('href'), a.get_text()))

            #Get links to ignore summary and panels
            for summary in anchor.find_all(id="toc"):
                for a in summary.findChildren("a") :
                    listLinkToIgnore.append(a.get('href'))
            for rightSide in anchor.find_all('div', {'class': re.compile(r"^infobox")}):
                for a in rightSide.findChildren("a") :
                    listLinkToIgnore.append(a.get('href'))
            for infobox in anchor.find_all('table'):
                for a in infobox.findChildren("a") :
                    listLinkToIgnore.append(a.get('href'))

        #Clean up the list
        listLink[:] = [(x,_) for (x,_) in listLink if CheckLinkToKeep(x,_)]
        #Transform list of Tuple for js
        listjs = []
        for i in listLink:
            listjs.append(TupleToJs(i))
        
        #return list and score
        eel.displayOptions(listjs)
        eel.showScore(linkStart[1], linkActive[1], linkFinish[1])

#endregion

#start GUI in firefox
eel.start('index.html', mode='chrome-app')
