color = ["bg-primary", "bg-success", "bg-info", "bg-warning", "bg-danger", "bg-secondary", "bg-dark"];
linkActive_js = ["", ""];
linksOption = [];
StartLink = "";
score = 0;

//Get Start link at the start
eel.expose(setStartLink);
function setStartLink(linkStart){
  StartLink = linkStart.split("=");
  eel.getLinks(StartLink[0]);
}

//Update score and links
eel.expose(showScore);
function showScore(linkStart, linkActive, linkFinish){
  document.getElementById("score").innerHTML = score == 0 ? "Let get Started!" : score ;
  document.getElementById("startLink").innerHTML = linkStart;
  document.getElementById("activeLink").innerHTML = linkActive;
  document.getElementById("finishLink").innerHTML = linkFinish;
}

//Call when the game start the first time
function gameStart(){
  document.getElementById("game").style.display = "block";
  document.getElementById("button_startGame").setAttribute("hidden", "none");
  eel.getStartLink();
}

function onClick(link){
  eel.getLinks(link);
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
    var link = element.split("=");
    //display only if it's not white nor empty
    if (link[1].trim() != ""){
      var child = document.createElement("li");
      child.className = "list-group-item rounded m-3 border-light " + color[Math.floor(Math.random() * 7)];
      child.innerText = link[1];
      child.addEventListener("click",(event)=>{onClick(link[0]); event.stopPropagation();}, false);
      parent.appendChild(child);
    }
  });
}

//Show or Hide Rules
document.getElementById("button_rules").addEventListener("click", ()=>
{
  var element = document.getElementById("rules");
  if (element.style.display != "block")
  {
    element.style.display = "block";
    document.getElementById("button_rules").innerText = "Hide Rules";
  }
  else{
    element.style.display = "none";
    document.getElementById("button_rules").innerText = "Rules";
  }
});

//Button start game or restart (not working)
document.getElementById("button_startGame").addEventListener("click", gameStart);
document.getElementById("button_restart").addEventListener("click", gameStart);
