color = ["bg-primary", "bg-success", "bg-info", "bg-warning", "bg-danger", "bg-secondary", "bg-dark", "bg-light"];
linkActive_js = ["", ""]

//Update score and links
eel.expose(showScore_js);
function showScore_js(linkStart, linkActive, linkFinish, score){
  linkActive_js = linkActive.split("=");
  document.getElementById("score").innerHTML = score;
  document.getElementById("startLink").innerHTML = linkStart;
  document.getElementById("activeLink").innerHTML = linkActive_js[1];
  document.getElementById("finishLink").innerHTML = linkFinish;
  document.getElementById("options").innerHTML = typeof(linkActive);
  eel.getLinks(linkActive_js[0]);
}

eel.expose(displayOptions);
function displayOptions(links){
  // var list = []
  // links.forEach(element => {
  //   list.push(element.slice(element.indexOf("=")+1, element.lenght));
  // });
  
  var parent = document.getElementById("options");
  links.forEach(element => {
    var child = document.createAttribute("li");
    child.className = "list-group-item " + color[Math.floor(Math.random() * 8)];
    child.setAttribute("id", element.slice(0, element.indexOf("=")));
    child.innerText = element.slice(element.indexOf("=")+1, element.lenght);
    parent.appendChild(child);
  });
}

//Call when the game start the first time
function gameStart(){
  document.getElementById("game").style.display = "block";
  document.getElementById("button_startGame").setAttribute("hidden", "none");
  //as the score to python
  eel.showScore()
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

//Button start game or restart 
document.getElementById("button_startGame").addEventListener("click", gameStart);
document.getElementById("button_restart").addEventListener("click", gameStart);

//#endregion
