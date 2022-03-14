let output = document.getElementById("output")
let input = document.getElementById("input")
let button = document.getElementById("button")

output.innerHTML = "Type a color then hit enter:"

function changeColor(){
    output.style.color = (input.value).replace(" ", "");
}

input.onchange = changeColor