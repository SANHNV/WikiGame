color = ["bg-primary", "bg-success", "bg-info", "bg-warning", "bg-danger", "bg-secondary", "bg-dark", "bg-light"];
linkActive_js = ["", ""]
linksOption = []

//Update score and links
eel.expose(showScore_js);
function showScore_js(linkStart, linkActive, linkFinish, score){
  linkActive_js = linkActive.split("=");
  document.getElementById("score").innerHTML = score;
  document.getElementById("startLink").innerHTML = linkStart;
  document.getElementById("activeLink").innerHTML = linkActive_js[1];
  document.getElementById("finishLink").innerHTML = linkFinish;

  //Call the link to choose from
  eel.getLinks(linkActive_js[0]);
}

//Call when the game start the first time
function gameStart(){
  document.getElementById("game").style.display = "block";
  document.getElementById("button_startGame").setAttribute("hidden", "none");
  eel.showScore()
}

//Display links in list ul
eel.expose(displayOptions);
function displayOptions(links){
  linksOption = links;

  //Test links are received
  document.getElementById("test").innerText = linksOption;

  //Add to DOM => Not working
  var parent = document.getElementById("options");
  linksOption.forEach(element => {
    var child = parent.createAttribute("li");
    child.className = "list-group-item " + color[Math.floor(Math.random() * 8)];
    child.innerText = element.slice(element.indexOf("=")+1, element.lenght);
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
