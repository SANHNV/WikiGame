color = ["bg-primary", "bg-success", "bg-info", "bg-warning", "bg-danger", "bg-secondary", "bg-dark"];
linkActive_js = ["", ""];
linksOption = [];
StartLink = "";

//Get Start link at the start
eel.expose(setStartLink);
function setStartLink(linkStart){
  StartLink = linkStart.split("=");
  document.getElementById("test").innerText = StartLink;
  StartLink[1] = StartLink[1].slice(1, StartLink[1].lenght);
  //document.getElementById("test").innerText = StartLink;
  eel.getLinks(StartLink[0]);
}

//Update score and links
eel.expose(showScore);
function showScore(linkStart, linkActive, linkFinish, score){
  document.getElementById("score").innerHTML = score;
  document.getElementById("startLink").innerHTML = linkStart;
  document.getElementById("activeLink").innerHTML = linkActive_js[1];
  document.getElementById("finishLink").innerHTML = linkFinish;
}

//Call when the game start the first time
function gameStart(){
  document.getElementById("game").style.display = "block";
  document.getElementById("button_startGame").setAttribute("hidden", "none");
  eel.getStartLink();
}

//Display links in list ul
eel.expose(displayOptions);
function displayOptions(links){
  linksOption = links;

  //Remove any element existing in dom
  var parent = document.getElementById("options");
  while (parent.hasChildNodes()) {  
    parent.removeChild(parent.firstChild);
  } 

  //Add new element in dom
  linksOption.forEach(element => {
    var child = document.createElement("li");
    child.className = "list-group-item rounded m-3 border-light " + color[Math.floor(Math.random() * 7)];
    child.innerText = element.slice(element.indexOf("=")+1, element.lenght);
    //child.addEventListener("click", eel.getLinks(child.innerText));
    parent.appendChild(child);
  });
}

//Show Rules
document.getElementById("button_rules").addEventListener("click", ()=>
{
  var element = document.getElementById("rules");
  if (element.style.display == "none")
  {
    element.style.display = "block";
    document.getElementById("button_rules").innerText = "Hide Rules"
  }
  else{
    element.style.display = "none";
    document.getElementById("button_rules").innerText = "Show Rules"
  }
});

//Button start game or restart (not working)
document.getElementById("button_startGame").addEventListener("click", gameStart);
document.getElementById("button_restart").addEventListener("click", gameStart);
