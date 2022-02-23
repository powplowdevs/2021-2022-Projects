let output = document.getElementById("output")
let mealcost = document.getElementById("input")
let drop = document.getElementById("dropdown")

function calculateTip(){
    document.getElementById("output").innerHTML = "Total tip at " + drop.value + "% will be: " + (parseInt(mealcost.value)*parseInt(drop.value))/100 + "$, And total meal cost will be: " + (parseInt(mealcost.value) + parseInt(drop.value))
}
