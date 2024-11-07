let dogs = [];

for (let i = 0; i < 6; i++){
    dogs.push(prompt("Give me a name for the dog: " + (i+1) + "/6"));
}

const ul = document.getElementById('one');

dogs.sort();

for (let x = dogs.length-1; x >= 0; x--) {
    const li = document.createElement("li"); // create li element.

    li.innerHTML = dogs[x]; // assigning text to li using array value.

    ul.appendChild(li); // append li to ul.
}