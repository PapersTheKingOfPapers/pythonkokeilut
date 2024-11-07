let numbers = [];

for (let i = 0; i < 5; i++){
    numbers.push(parseInt(prompt("Give me an Int: " + (i+1) + "/5")))
}

for (let i = 4; i >= 0; i--){
    console.log(numbers[i])
}