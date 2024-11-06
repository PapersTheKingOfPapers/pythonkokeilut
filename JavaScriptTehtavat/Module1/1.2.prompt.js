let person = prompt("Please tell me your name:");

if (person != null){
    document.getElementById("name").innerHTML = "Hello, " + person + "!";
}