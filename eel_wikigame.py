#region import

import eel
import random
from bs4 import BeautifulSoup
import urllib.request
import re

#endregion

#start gui
eel.init('web')

#Get url and title from random wiki url
def ReturnLink(link):
    with urllib.request.urlopen(link) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        return (response.url, soup.find(id="firstHeading").get_text())

#region Initialization

#Initialize the wiki links
linkRandom = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"
linkStart = ReturnLink("https://fr.wikipedia.org/wiki/Philippe_le_Hardi")
linkFinish = ReturnLink(linkRandom)
likeBase = "https://fr.wikipedia.org"

#Variables
global linkActive 
linkActive = linkStart
listLinkToIgnore = [("","")]
global score = 0

#Clean up the links captured
def CheckLinkToKeep(link):
    return link != None and not (link in listLinkToIgnore) and not (link.startswith('/w/index')) and not (link.startswith('http')) and not (link.startswith('#')) and not (link.startswith('/wiki/Cat%C3%A9gorie')) and not (link.startswith('/wiki/Portail:')) and not (link.startswith('/wiki/Fichier')) and not (link.startswith('/wiki/Aide')) and not (link.startswith('/wiki/Projet'))

#Format tuple to string = "tuple0=tuple1"
def TupleToJs(tuple):
    return tuple[0] + "=" + tuple[1]

#region GUI eel

#Get StartLink
@eel.expose
def getStartLink():
    eel.setStartLink(TupleToJs(linkStart))

#Filter list of links for next jump and return it
@eel.expose
def getLinks(link):
    linkActive = ReturnLink(link)
    if score == None :
        score =0
    listLink = [("","")]
    listLink.remove(("",""))

    #Get all the link in the page
    print(link)
    print(linkActive)
    print("\n\n\n")

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

        #Clean up the list
        listLink[:] = [(x,_) for (x,_) in listLink if CheckLinkToKeep(x)]
        listjs = []
        for i in listLink:
            listjs.append(TupleToJs(i))
        
        #return list and score
        temp = score if score !=0 else "Let's get started"
        eel.displayOptions(listjs,linkStart[1], linkActive[1], linkFinish[1], temp)
        score +=1


#endregion

#start GUI
eel.start('index.html')

#endregion