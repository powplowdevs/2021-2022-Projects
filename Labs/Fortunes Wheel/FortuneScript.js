//ayoub, mohammed
//PRE GIVEN VARS
let puzzle = document.getElementById("puzzle");
let letters = document.getElementById('letters');
let totalPts = document.getElementById('totalPts');
let spinPts = document.getElementById('spinPts') ;
let container = document.getElementById('container');
let UsedLetters = document.getElementById('used')
let emptyPiece = "";
let usedLetters = "";
//PRE GIVEN VARS

//LOGIC VARS-----------------------
//an array with all our possible words
const wordsAll = ["HANGMAN", "POPULATION", "MIGRATION", "WORD", "HARD",  "HAND", "OBJECT",'ability',"about","Because","Even","Find"];
//convert all possible words in the array above to all caps so we dont screw anything up when compare them to the gueses
let words = wordsAll.map(wordsAll => wordsAll.toUpperCase());
//sets our word to a random word within the wordsAll array (see more on line 44)
let word = getPuzzle();
//this variable will store the word we chose minus the words the user has allready guessed, thus letting us know what words are left
let avword = ""
//see line 143 more more info
let word_progress = ""
//this var will not change at al unless we pick a new word or in other words wont chage till the game ends
let base_word = word
//a var that stores out users var
let userInput = null;
//LOGIC VARS-----------------------
//will be true if game has started
let game_start =  false
//LOGIC VARS-----------------------


//our score vars
let pts = 0;
let score = 0;

//start our game
play()

function play(){
    displayArray()
}
function getPuzzle(){
    //this return statement will use list indexing (search it up) to get a return a random word the words list
    return words[Math.floor(Math.random() * words.length)];
}

function getArray(puzzleWord){
   
}

function displayArray() {
    //this function will create all the empty word spaces when the game starts
    //we start off by looping for the length of the word we piced thus making the correct amt of empty spaces IF THE GAME HAS NOT STARTED
    if (game_start == false){
        game_start = true
        for (let i = 0; i < word.length; i++){
            //make a new div
            let div = document.createElement('div');
            //set is text to the empty symbol
            div.innerHTML = '_';

            //style or css
            div.style.width = "30px";
            div.style.display = "inline"
            div.style.margin = "10px"
            div.style.textAlign = "center"
            div.style.backgroundColor = "green"
            //style or css

            //give it an id
            div.id = 'div' + i;
       
            //add it to the html
            puzzle.appendChild(div);
        }
    }
    //if the game did start we will do the same but reset the values insted of makeing new divs
    else{
        for (let i = 0; i < word.length; i++){
            //get div
            let div = document.getElementById("div"+i)
         //destroy div
            div.remove()
        }
        //pick new word
        word = getPuzzle();
        for (let i = 0; i < word.length; i++){
            //make a new div
            let div = document.createElement('div');
            //set is text to the empty symbol
            div.innerHTML = '_';

            //style or css
            div.style.width = "30px";
            div.style.display = "inline"
            div.style.margin = "10px"
            div.style.textAlign = "center"
            div.style.backgroundColor = "green"
            //style or css

            //give it an id
            div.id = 'div' + i;
       
            //add it to the html
            puzzle.appendChild(div);
        }

    }
}

function updateBoard() {
    //this function will update the score,empty word spaces everytime the uses makes a guess

    //start off by resetting out avword var
    avword = ""
    let div = document.createElement('div');
    div.innerHTML = userInput;
    div.style.display = "inline"
    div.style.margin = "5px"
    UsedLetters.appendChild(div)
    //now lets loop trough our word find matches between the users input and the letters in the word
    for (let index = 0; index < word.length; index++) {
        //garb the current letter in the word that we are looking at
        element = word[index]
       

           
        //check to see its the same as the user input
        if (element == userInput){
            //garb the empty slot corisponding to the letter of our word that we are on
            spot = document.getElementById("div"+index)
            //update emtpy slot
            spot.innerHTML = element
            //add to score
            totalPts.innerHTML = parseInt(totalPts.innerHTML) + parseInt(spinPts.innerHTML)
            //remove the letter from the avaibale words list as we used it allready
            avword += "_"
           
            //LOGIC------------
            //ths logic will check to see if the user won with their last guess
            //first loop trough the word slots and garb all there values empty or filled
            //word_progess: This var will have all of the letters the use has guess places into the word. basicly it stores how much of the word the user has guessed
            for (let i = 0; i < word.length; i++){
                let div = document.getElementById("div"+i)
                word_progress += div.innerHTML
               
           
            }
            //check to see if they are equal to our base_word or the word we chose at the start
            if (word_progress == base_word){
                console.log("won")
                alert( "You Won!" )

            }
            //if not just continue and reset out progress word as we will loop trough the slot and redefine it later
            else{
                word_progress = ""
            }
            //LOGIC------------
        }
        //if the element was not the same as the user input we can add it to the avalibe words list as we havent used it
        else{
            avword += element
        }
    }

    word = avword
}

function getInput(num) {
    //garb our users input and set it to all caps for logical reasons
    userInput = num.toUpperCase()
    //run the update baord function
    updateBoard()
}

function spin() {
    //get a random value between 0 and 100 that is divisable by 10, for ex:(10,20,30,etc...)
    pts = Math.floor(Math.random()*11)*10
    //set the random value to pts so the user can see it
    spinPts.innerHTML = pts
}