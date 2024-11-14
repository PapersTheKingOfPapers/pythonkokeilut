function letsMath(){
    let calculation = document.getElementById("calculation").value;
    let txt = [];
    let num1 = 0;
    let num2 = 0;

    if(calculation.includes('+')) {
        txt = calculation.split('+');
        num1 = parseInt(txt[0])
        num2 = parseInt(txt[1])
        document.getElementById("result").innerHTML="" + (num1 + num2);
    } else if(calculation.includes('-')) {
        txt = calculation.split('-');
        num1 = parseInt(txt[0])
        num2 = parseInt(txt[1])
        document.getElementById("result").innerHTML="" + (num1 - num2);
    } else if(calculation.includes('*')){
        txt = calculation.split('*');
        num1 = parseInt(txt[0])
        num2 = parseInt(txt[1])
        document.getElementById("result").innerHTML="" + (num1 * num2);
    } else if(calculation.includes('/')){
        txt = calculation.split('/');
        num1 = parseInt(txt[0])
        num2 = parseInt(txt[1])
        document.getElementById("result").innerHTML="" + (num1 / num2);
    }
}

let button = document.getElementById("start");
button.addEventListener("click",letsMath)
