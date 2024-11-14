const trigger = document.getElementById("trigger");

function hoverFunc(){
    document.getElementById("target").src="img/picB.jpg";
}
function leaveHoverFunc(){
    document.getElementById("target").src="img/picA.jpg";
}

trigger.addEventListener("mouseover",hoverFunc)
trigger.addEventListener("mouseleave",leaveHoverFunc)