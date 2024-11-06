const num1 = parseInt(prompt("Enter your first integer: ", "0"))
const num2 = parseInt(prompt("Enter your second integer: ", "0"))
const num3 = parseInt(prompt("Enter your third integer: ", "0"))

if (num1 != null && num2 != null && num3 != null){
    document.getElementById("sum").innerHTML = "The sum of all the integers is: " + (num1 + num2 + num3);
    document.getElementById("product").innerHTML = "The product of all the integers is: " + (num1 * num2 * num3);
    document.getElementById("average").innerHTML = "The average of all the integers is: " + ((num1 + num2 + num3) /3 );
}