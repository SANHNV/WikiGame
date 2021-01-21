color = ["bg-primary", "bg-success", "bg-info", "bg-warning", "bg-danger", "bg-secondary", "bg-dark", "bg-light"];

//Update score and links
eel.expose(showScore_js);
function showScore_js(linkStart, linkActive, linkFinish, score){
  document.getElementById("score").innerHTML = score;
  document.getElementById("startLink").innerHTML = linkStart;
  document.getElementById("activeLink").innerHTML = linkActive;
  document.getElementById("finishLink").innerHTML = linkFinish;
}

//Call when the game start the first time
function gameStart(){
  document.getElementById("game").style.display = "block";
  document.getElementById("startGame").setAttribute("hidden", "none");
  eel.showScore()
}

//button start game
document.getElementById("startGame").addEventListener("click", gameStart);

//#region Test eel
eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}

document.getElementById("button-name").addEventListener("click", ()=>{eel.start()}, false);
document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);
//#endregion
