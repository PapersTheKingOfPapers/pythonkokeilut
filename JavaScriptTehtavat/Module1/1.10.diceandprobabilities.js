let dice = parseInt(prompt("How many dice should I throw?"))
let sumoffaces = parseInt(prompt("How big of a sum do you expect?"))

function getRandomIntInclusive(min, max) {
  const minCeiled = Math.ceil(min);
  const maxFloored = Math.floor(max);
  return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled); // The maximum is inclusive and the minimum is inclusive
}

let amountofsums = 0

for (let x = 0; x < 10000; x++){
    let sum = 0
    for (let i=0; i < dice; i++){
        sum += getRandomIntInclusive(1,6);
    }
    if(sum === sumoffaces){amountofsums++}
}

document.getElementById("text").innerHTML = "Probability to get sum " +sumoffaces+ " with " + dice + " dice is " + Number.parseFloat((amountofsums/10000)*100).toFixed(2) + "%";