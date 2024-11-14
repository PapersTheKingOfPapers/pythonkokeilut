function scream(){
    alert("Button clicked!")
    return null;
}

let buttons = document.querySelectorAll("button");
for (let i = 0; i<buttons.length;i++){
    buttons[i].onclick=function(){scream()};
}