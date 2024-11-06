let dice = parseInt(prompt("How many dice do I throw?"))

function getRandomIntInclusive(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled); // The maximum is inclusive and the minimum is inclusive
}

let sum = 0

for (let i=0; i < dice; i++){
    sum += getRandomIntInclusive(1,6);
}
document.getElementById("text").innerHTML = "The sum of the " +dice+ "d6 dices is " + sum;
