let first_array = [2,7,4];

function even(arr){
    let second_array = [];

    for (let i = 0; i < arr.length; i++){
        if(arr[i] % 2 === 0){
            second_array.push(arr[i]);
        }
    }
    return second_array;
}

console.log(first_array);
console.log(even(first_array));