function concat(arr){
    let a = "";
    for(let i = 0; i<arr.length; i++){
        a += arr[i];
    }
    return a;
}

const strings = ["Johnny", "DeeDee", "Joey", "Marky"];

document.getElementById("text").innerHTML = concat(strings);