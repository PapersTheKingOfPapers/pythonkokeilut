let numbers = [];

while(true){
    let input = parseInt(prompt("Give me a number, or 0 to end this:"));
    if(input === 0){
        break;
    }
    numbers.push(input);
}

numbers.sort(function (a,b){
    return a-b;
});

for (let i = numbers.length-1; i >= 0; i--){
    console.log(numbers[i])
}