//button colors
const xColor = "";  //Choose a color for each variable
const oColor = "";
const emptyColor = "";
const allEqual = arr => arr.every(val => val === arr[0]);

//initialize scores
    /*create a variable for x wins and assign it to zero
    do the same for o wins
    and also draws or 'cat' games*/
let xwins = 0
let owins = 0
let moves = 0

let turn = true //false = Y's turn :: true = X's turn
let buttonArray = []

let side = []
let up = []
let angle = [] 

getButtonIds()
let avalablebuttons = buttonArray

//set up intial board
    //create a varialbe buttons and assign it to the getButtonIds() function
    //call the clearButtons () function

//this function should create and return an array of buttons that represents the game board
function getButtonIds() {
    //create a variable buttonArray and assign as an empty array
    //create a for loop that runs 9 times
        /*inside the loop create a variable buttonID and assign it to hold an element from 
        the html, incrementing each time so it holds a different element each time the loop
        runs */
        //use the .push() method to push each buttonID into the buttonArray
    //return the buttonArray
    for (let index = 0; index < 9; index++) {
        buttonArray.push(document.getElementById("button"+index))
    }
    clearButtons()
}

//this function should reset each button back to its original 'emptyColor' state
function clearButtons() {
    /*create a for loop that runs through the length of the buttons array*/
        //set the innerHTML of each element in the buttons array to "-"
        //set the .style.color of each element in the buttons array to emptyColor
        //set the background color to emptyColor as well
    //call the updateScores function
    buttonArray.forEach(button => {
        button.style.color = "red"
        button.innerHTML = "-"
        button.backgroundcolor = "silver"
    });


}

//this function is called when a player clicks on a button on the webpage
function buttonClick(buttonNumber) {
    /*create a variable button and assign it to be the buttonNumber element of the 
    buttons array*/
    //check if the button's is still an empty button
        //if it is change it's innerHTML to be the players symbol
        //change its background color to the correct color
    //if not, then return and do nothing
    
    //set up a conditional structure that checks if a player wins (use a return function)
        //increase the win total for that player
        //call the alert function with the correct message
        //clear buttons for next game
    //else check if it was a draw (use a teturn function)
        //increase the draw total
        //alert that it was a draw
        //clear the buttons
    //call the computer turn or set the game up for the next player
    button = buttonArray[buttonNumber]
    //console.log(button.innerHTML)
    if (button.innerHTML == "-"){
        if (turn == true){
            turn = false
            button.innerHTML = "X"
            checkForWin("X")
            moves++
        }
        else{
            turn = true
            button.innerHTML = "O"
            checkForWin("Y")
            moves++
        }
    }

}

//this function should check if the given player has achieved a win
function checkForWin(player) {
    /*set up a control structure that checks through all the possible win scenarios, 
        hint: compare the innerHTML of each element in the button to the player argument
    returning true if the player has met a win scenario*/
    //if none are found return false
    
}

/*this function will check for a draw situation
    a draw will occur when no one has won and there are no empty location*/
function checkForDraw() {
    //loop through the buttons array
        //check if each buttons innerHTML is empty
            //if an empty button space is found return false
    //if the loop doesn't find any empty buttons it should return true
}

//This function should allow the computer to make its move
function computerTurn()  {
    //First have the computer check if there are any winning moves for it
    for(let i = 0; i < buttons.length; i++){
       /*checks if each move produces a computer win. If a move is found using the 
       checkForWin() function, increase the o wins, produce an alert, clear the buttons
       and return*/
    }

    //next have the computer block any spaces that would allow the user to win
    for(let i = 0; i < buttons.length; i++){
        /*checks if each move produes a player win. If a move is found, make the move,
        check for a draw and return*/
    }

    /*---------now build the computer's playing style------*/
    /*create a flag variable that will keep the computer picking squares until it finds
    the best square */
    //set up a while loop that uses the flag variable
        /*use a control structure to check the best spots first, if it finds one change
        the innerHTML and the background color and then break out of the loop */

        /*If no strategic spot is available, have the computer pick a random spot that is
        empty.  Put its symbol, change the background color and break out of the loop.*/
    
    //check if the computer move produced a draw
        //if it did, increase the draw total, alert the user and clear the buttons
}

//this function will be the scoreboard, keeping track of x wins, o wins, and draws
function updateScores() {
    //create a variable to hold the result element from the html
    //clear the result variable's innerHTML
    //create a text variable and assign it to display the correct information
    //set the result variable's innerHTML to this text
}
