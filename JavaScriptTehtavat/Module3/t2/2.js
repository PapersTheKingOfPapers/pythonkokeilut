let stuff = ["First item", "Second item", "Third item"];
for (let i = 0; i<stuff.length;i++){
    let newli = document.createElement("li");
    newli.innerHTML = stuff[i];
    document.getElementById("target").appendChild(newli);
}
document.getElementById("target").querySelectorAll("li")[1].classList.add("my-item");