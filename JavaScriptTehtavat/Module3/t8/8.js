function letsMath(){
    let num1 = parseInt(document.getElementById("num1").value);
    let num2 = parseInt(document.getElementById("num2").value);
    let oper = document.getElementById("operation").value;

    switch (oper){
        case "add":
            document.getElementById("result").innerHTML="" + (num1 + num2);
            break;
        case "sub":
            document.getElementById("result").innerHTML="" + (num1 - num2);
            break;
        case "multi":
            document.getElementById("result").innerHTML="" + (num1 * num2);
            break;
        case "div":
            document.getElementById("result").innerHTML="" + (num1 / num2);
            break;
    }
}

let button = document.getElementById("start");
button.addEventListener("click",letsMath)
