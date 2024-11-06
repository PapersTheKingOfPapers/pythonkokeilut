let start = parseInt(prompt("Give me a start year: "))
let end = parseInt(prompt("Give me an end year: "))

let leapyears = [];

for (let i=start; i <= end; i++){
    if(i % 4 === 0){
        if(i % 100 === 0) {
            if (i % 400 === 0) {
                leapyears.push(i);
            }
        }
        else {
            leapyears.push(i);
        }
    }
}

const ul = document.getElementById('one');

for (let x = 0; x < leapyears.length; x++) {
    const li = document.createElement("li"); // create li element.

    li.innerHTML = leapyears[x]; // assigning text to li using array value.

    ul.appendChild(li); // append li to ul.
}
