let year = parseInt(prompt("Give me a year!"))

function innerHTMLchange(input){
    document.getElementById("text").innerHTML = input;
}

if(year % 4 === 0){
    if(year % 100 === 0){
        if (year % 400 === 0) {
            innerHTMLchange(year + " is a leap year!")
        }
        else{
            innerHTMLchange(year + " is not a leap year!")
        }
    }
    else{
        innerHTMLchange(year + " is a leap year!")
    }
}
else{
    innerHTMLchange(year + " is not a leap year!")
}