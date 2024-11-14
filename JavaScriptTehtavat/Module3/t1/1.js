let stuff = ["First item", "Second item", "Third item"];
let text = "";
for (let i = 0; i<stuff.length;i++){
    text += "<li>" + stuff[i] + "</li>";
}
document.getElementById("target").innerHTML=text;
document.getElementById("target").classList.add("my-list");