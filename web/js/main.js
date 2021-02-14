//Initilization Variables
const color = ["bg-primary", "bg-success", "bg-info", "bg-warning", "bg-danger", "bg-secondary"];
var score = 0;
var end =""

//Get Start link at the start
eel.expose(setStartLink);
function setStartLink(linkStart){
  StartLink = linkStart.split("=");
  eel.getLinks(StartLink[0]);
}

//Update score and links
eel.expose(showScore);
function showScore(linkStart, linkActive, linkFinish){

  //Update the informations
  document.getElementById("score").innerHTML = score ;
  document.getElementById("startLink").innerHTML = linkStart;
  document.getElementById("activeLink").innerHTML = linkActive;
  document.getElementById("finishLink").innerHTML = linkFinish;

  //In case of win
  if (linkActive == linkFinish){
    document.getElementById("game").setAttribute("hidden", '');
    document.getElementById("button_startGame").removeAttribute("hidden");
    document.getElementById("win").removeAttribute("hidden");
    document.getElementById("display_score").innerText = "You only needed " + score + " tries!!";
  }
}

//Call when the game start the first time
function gameStart(){
  score = 0;
  document.getElementById("game").removeAttribute("hidden");
  document.getElementById("button_startGame").setAttribute("hidden", '');
  document.getElementById("win").setAttribute("hidden", '');
  eel.getStartLink();
}

//Update score then do the next jump
function onClick(link){
  score += 1;
  eel.getLinks(link);
}

//Remove all the options'children
function cleanOption(parent){
  while (parent.hasChildNodes()) {  
    parent.removeChild(parent.firstChild);
  } 
}

//Display links in list ul
eel.expose(displayOptions);
function displayOptions(links){
  linksOption = links;

  var parent = document.getElementById("options");
  cleanOption(parent);

  //Add new element in dom
  linksOption.forEach(element => {
    var link = element.split("=");
    //display only if it's not white nor empty, more than 1 character
    if (link[1].trim() != "" && link[1].length >=2){
      var child = document.createElement("li");
      child.className = "list-group-item rounded m-3 border-light " + color[Math.floor(Math.random() * 6)];
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
  if (element.getAttribute("hidden") != null)
  {
    element.removeAttribute("hidden");
    document.getElementById("button_rules").innerText = "Hide Rules";
  }
  else{
    element.setAttribute("hidden", '');
    document.getElementById("button_rules").innerText = "Rules";
  }
});

//Button start game or restart
document.getElementById("button_startGame").addEventListener("click", gameStart);
document.getElementById("button_restart").addEventListener("click", gameStart);
