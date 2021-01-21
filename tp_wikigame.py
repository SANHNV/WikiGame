#!/bin/python
# coding: utf-8

#region imports

from bs4 import BeautifulSoup
import urllib.request
import re

#endregion

#region Colors

#Some colors or effect
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Colored text
def colored(color, string):
    switcher = {
        "title": bcolors.HEADER + string + bcolors.ENDC,
        "blue": bcolors.OKBLUE + string + bcolors.ENDC,
        "cyan": bcolors.OKCYAN + string + bcolors.ENDC,
        "green": bcolors.OKGREEN + string + bcolors.ENDC,
        "yellow": bcolors.WARNING + string + bcolors.ENDC,
        "red": bcolors.FAIL + string + bcolors.ENDC,
        "bold": bcolors.BOLD + string + bcolors.ENDC,
        "underline": bcolors.UNDERLINE + string + bcolors.ENDC
    }
    return switcher.get(color, "")

#endregion

#Get url and title from wiki url
def ReturnLink(link):
    with urllib.request.urlopen(link) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        return (response.url, soup.find(id="firstHeading").get_text())
        
#Clean up the links captured
def CheckLinkToKeep(link):
    return link != None and not (link in listLinkToIgnore) and not (link.startswith('/w/index')) and not (link.startswith('http')) and not (link.startswith('#')) and not (link.startswith('/wiki/Cat%C3%A9gorie')) and not (link.startswith('/wiki/Portail:')) and not (link.startswith('/wiki/Fichier')) and not (link.startswith('/wiki/Aide')) and not (link.startswith('/wiki/Projet'))

#region Initialization

#Wiki links
linkRandom = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"
linkStart = ReturnLink(linkRandom)
linkFinish = ReturnLink(linkRandom)

#Variables
linkBase = "https://fr.wikipedia.org"
global linkActive
listLinkToIgnore = ([])

#endregion

#Print list of link choice for next jump
def printChoice(listLink):
    count = 1
    for i in listLink:
            print(str(count) + "- " + i[1])
            count +=1

#Print list of next jump and return list
def play(link):
    listLink = [("","")]
    listLink.remove(("",""))

    #Get all the link in the page
    with urllib.request.urlopen(link) as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        for anchor in soup.find_all(id="content"):

            #Get all the links in main content
            for a in anchor.findChildren("a") :
                if(a.get('href') != None) :
                    listLink.append((a.get('href'), a.get_text()))

            #Get links to ignore summary and panel
            for summary in anchor.find_all(id="toc"):
                for a in summary.findChildren("a") :
                    listLinkToIgnore.append(a.get('href'))
            for rightSide in anchor.find_all('div', {'class': re.compile(r"^infobox")}):
                for a in rightSide.findChildren("a") :
                    listLinkToIgnore.append(a.get('href'))

        #Clean up the list
        listLink[:] = [(x,_) for (x,_) in listLink if CheckLinkToKeep(x)]

        #Print the active link and the next choices
        print(colored("blue","Start : ") + colored("cyan", str(linkStart[1])) + colored("blue","\nActive link : ") + colored("cyan", str(linkActive[1])) + colored("blue","\nGoal : ") + colored("cyan", str(linkFinish[1])) + "\n")

        return listLink

#Check the entry is a number between 1 and number of possibilities
def checkSaisie():
    saisie = False
    number = 0
    while not saisie :
        try:
            number = int(input(colored("blue","Next Jump: ")))      
        except:
            print(colored("red", "/!\\ Entrée invalide, recommencer /!\\"))
        else:
            if number ==0:
                quit()
            if number >= 1 and number <= len(listLink) :
                saisie =  True
            else:
                print(colored("yellow", "/!\\ Le nombre n'est pas dans la liste. /!\\ \nMais si tu veux quitter, entre 0."))
    return number

#Start message
print(colored("bold", colored("blue","Welcome to the WikiGame!\n")) + colored("blue","\nThe Only Rule : Enter the number of your next jump to start you wikiwalk.\n")+ "   ------------\n")
linkActive = linkStart
while linkActive[1] != linkFinish[1] :
    listLink = play(linkActive[0]) #get choices
    printChoice(listLink) #show choices
    nextjump = checkSaisie() #get command
    element = listLink[nextjump-1]
    linkActive = ReturnLink(linkBase + element[0]) #update active link
    print("\n   ------------\n")
print( bcolors.OKGREEN + "Congrats, you win !" + bcolors.ENDC)

#Keep :
# "main", {"id" : "content"}
# not "div", {"id" : "toc"}
# not "table", {"class" : "infobox_v2"}