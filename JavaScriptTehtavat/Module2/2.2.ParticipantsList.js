let amount_of_participants = parseInt(prompt("Give me an amount of participants: "));

let participants = [];

for (let i = 0; i < amount_of_participants; i++){
    participants.push(prompt("Give me a name for the participant: " + (i+1) + "/" + amount_of_participants));
}

const ol = document.getElementById('one');

participants.sort();

for (let x = 0; x < participants.length; x++) {
    const li = document.createElement("li"); // create li element.

    li.innerHTML = participants[x]; // assigning text to li using array value.

    ol.appendChild(li); // append li to ol.
}
