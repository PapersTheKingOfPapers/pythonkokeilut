let text = "Calculate the square root?";
if (confirm(text) === true) {
    let number = parseInt(prompt("Give me an integer: "))
    if(number < 0){
        text = "The number is a negative! Can't square root it."
    } else {
        text = "The square root of " + number + " is " + (Math.sqrt(number));
    }
  } else {
    text = "You didn't want to square root anything!";
  }
document.getElementById("text").innerHTML = text;