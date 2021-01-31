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

#Initialize the wiki links
linkRandom = "https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard"
linkStart = ReturnLink(linkRandom)
linkFinish = ReturnLink(linkRandom)
likeBase = "https://fr.wikipedia.org"

#Variables
global linkActive
listLinkToIgnore = ([])
score = 0

#GUI
eel.init('web')

#endregion

#Show score first time on web
@eel.expose
def showScore():
    temp = score if score !=0 else "Let's get started"
    eel.showScore_js(linkStart[1], linkStart[1], linkFinish[1], temp)

#region Test eel
@eel.expose
def get_random_name():
    eel.prompt_alerts('Random name')

@eel.expose
def get_random_number():
    eel.prompt_alerts(random.randint(1, 100))
#endregion

#start GUI
eel.start('index.html')
