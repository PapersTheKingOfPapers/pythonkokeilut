let person = prompt("Whats your name?");

function getRandomIntInclusive(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled); // The maximum is inclusive and the minimum is inclusive
}

const rand = getRandomIntInclusive(0,3);

const houses = ["Hufflepuff","Ravenclaw","Gryffindor","Slytherin"];

if (person != null){
    document.getElementById("sort").innerHTML = "Well " + person + ", better be... " + houses[rand] + "!"
}