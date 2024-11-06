function innerHTMLchange(input){
    document.getElementById("text").innerHTML = input;
}

let number = parseInt(prompt("Give me an int:"))

if (number === 0 || number === 1){
    innerHTMLchange(number + " is not a prime number.");
} else if (number > 1){
    if(number === 2){
        innerHTMLchange(number + " is a prime number.");
    } else {
        for (let i = 2; i < number; i++){
            if (number % i === 0) {
                innerHTMLchange(number + " is not a prime number.");
                break
            } else {
            innerHTMLchange(number + " is a prime number.");
            }
        }
    }
} else {
    innerHTMLchange(number + " is not a prime number.");
}


