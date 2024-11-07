function getRandomIntInclusive(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled); // The maximum is inclusive and the minimum is inclusive
}

function rollTheDice(){
    return getRandomIntInclusive(1,6);
}

let rolls = [];

while(true){
    let roll = rollTheDice()
    if(roll === 6){
        rolls.push(roll);
        break;
    }
    rolls.push(roll);
}

const ul = document.getElementById('one');

for (let x = 0; x < rolls.length; x++) {
    const li = document.createElement("li"); // create li element.

    li.innerHTML = rolls[x]; // assigning text to li using array value.

    ul.appendChild(li); // append li to ul.
}