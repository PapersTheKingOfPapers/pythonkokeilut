let amount_of_candidates = parseInt(prompt("Give me the amount of candidates: "));

let candidates = [];

function create_candidate(name){
    return {"name":name,"votes":0};
}
function print_candidates_names(arr){
    let sentence = "";
    for (let i = 0; i < arr.length; i++){
        sentence += arr[i]["name"] + "\n";
    }
    return sentence;
}

for (let i = 0; i < amount_of_candidates; i++){
    candidates.push(create_candidate(prompt("Name for candidate " + (i+1))));
}

let amount_of_voters = parseInt(prompt("Give me the amount of voters:"))

for(let i = 0; i < amount_of_voters; i++){
    let vote = prompt("Who are you voting for? Enter the candidates's name.\nThese are the candidates:\n" + print_candidates_names(candidates));
    for (let x = 0; x < candidates.length; x++){
        if (candidates[x]["name"] === vote){
            candidates[x]["votes"]++;
        }
    }
}

candidates.sort((a, b) => {
   //console.log(a.votes, b.votes);
   return b.votes - a.votes;
});

console.log("The winner is " + candidates[0].name + " with " + candidates[0].votes + " votes.");
console.log("The results are:");
for(let i = 0; i<candidates.length; i++){
    console.log(candidates[i].name + ": " + candidates[i].votes + " votes.")
}
