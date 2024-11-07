let numbers = [];

while(true){
    let input = parseInt(prompt("Give me a number, duplicates end the loop:"));
    if(numbers.includes(input)){
        break
    }
    numbers.push(input);
}

numbers.sort(function (a,b){
    return a-b;
});

for (let i = 0; i < numbers.length; i++){
    console.log(numbers[i])
}