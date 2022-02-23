let numberPennies = 23;
/*Complete these three lines of code to grab the correct elements
from the HTML file to set up the program. */
let info = document.getElementById('info');
let feedback = document.getElementById('feedback');
let pieces = document.getElementById('pieces');
let diff = document.getElementById("diff");

let intro = "<h3>23 Pennies</h3>";
intro += "Take turns removing 1, 2, or 3 pennies. ";
intro += "Whoever takes the last penny loses. ";
info.innerHTML = intro;

let amountRemoved = 0;
let end = false;
let difficulty = "E"

displayPennies();

/*updates the pieces div in the HTML to display the proper number of 'pennies' */
function displayPennies() {
    for (let index = 0; index < 23; index++) {
        var img = document.createElement("img");
        img.src = "https://www.kindpng.com/picc/m/131-1318213_penny-png-transparent-png.png";
        img.width = 20
        img.style.margin = "5px"
        img.setAttribute("id", index)
        pieces.appendChild(img);
        
    }
}

/*This is the players turn, each button in the HTML will call this function when clicked on 
by the player, sending the corresponding number of pennies selected to the function and updating
the game. */
function take(num) {
    //enter all code here
    feedback.innerHTML = ""
    if (end == false){
        base = amountRemoved
        for (let index = 0; index < num; index++) {
            
            if (base+num < 23){
                let penney = document.getElementById(amountRemoved);
                penney.parentNode.removeChild(penney)
                amountRemoved++
            }
            else{
                for (let index = 0; index < 23-base; index++) {
                    let penney = document.getElementById(amountRemoved);
                    penney.parentNode.removeChild(penney)
                    amountRemoved++
                }
                end = true
                feedback.innerHTML = "You took " + num + " pennies and the last penney, you lost!"
                break
            }
            
        
            
        }
        
    }
    
    if (!end){
        feedback.innerHTML += "You took " + num
        setTimeout(() => {computerTurn();}, 1500); //last line of the function
    }
}

/*This is the computer's turn, it should have the computer select a number of pennies, check to see
if it lost, and update the game.*/
function computerTurn(){
    if (difficulty == "E"){
    num = Math.floor(Math.random() * 3);
    num++
    }
    else if (difficulty == "M"){
        chance = Math.floor(Math.random() * 3);
        if (amountRemoved < 15 && chance == 0){
            num = 3
        }
        if (amountRemoved == 19 && chance == 0){
            num = 3
        }
        if (amountRemoved == 20 && chance == 0){
            num = 2
        }

        else if(chance != 0){
            num = Math.floor(Math.random() * 3);
            num++ 
        }

    }
    else if (difficulty == "H"){
        chance = 0
        console.log(amountRemoved,chance)
        if (amountRemoved < 15){
            num = 3
        }
        if (amountRemoved == 19){
            num = 3
        }
        if (amountRemoved == 20){
            num = 2
        }
        if (amountRemoved == 21){
            num = 1
        }


    }


    if (end == false){
        base = amountRemoved
        for (let index = 0; index < num; index++) {
            
            if (base+num < 23){
                let penney = document.getElementById(amountRemoved);
                penney.parentNode.removeChild(penney)
                amountRemoved++
                
            }
            else{
                for (let index = 0; index < 23-base; index++) {
                    let penney = document.getElementById(amountRemoved);
                    penney.parentNode.removeChild(penney)
                    amountRemoved++
                }
                end = true
                feedback.innerHTML = "The computer took " + num + " pennies and the last penney, you won!"
                break
            }
        
            
            
        }

        if (!end){
            feedback.innerHTML += ", The computer took " + num
        }
    }

}

/*This function will reset the game board and the game will start fresh*/
function reset() {
    if (end){
        for (let index = 0; index < 23-amountRemoved; index++) {
            let penney = document.getElementById(amountRemoved);
            penney.parentNode.removeChild(penney)
            amountRemoved++
        }
        amountRemoved = 0;
        feedback.innerHTML = "";
        end = false
        displayPennies();
    }
    
}

function switchdifficulty() {
    if (difficulty == "H"){
        difficulty = "E"
        diff.innerHTML = "difficulty: Easy"
    }
    else if (difficulty == "M"){
        difficulty = "H"
        diff.innerHTML = "difficulty: Hard"
    }
    else{
        difficulty = "M"
        diff.innerHTML = "difficulty: Medium"
    }
}