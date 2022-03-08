BUFFER_TIME = 100
BASE_SIZE = "10px"
BG_COLOR = "#d9d9d9"
BORDER = "0px solid black"
SPEED = 100
BOARD_SIZE = [100,100]

//start and reset button
//self collision

game_board = document.getElementById('game-board')

//create player
class Snake {
    constructor(x,y) {
      this.x = x;
      this.y = y;
      this.len = 10
    }
}

const snake = new Snake(BOARD_SIZE[0]/2,BOARD_SIZE[1]/2)
let x = BOARD_SIZE[0]/2
let y = BOARD_SIZE[1]/2
direction = "right"
playing = true
used_boxes = []
max_appels = 1
spotx = 0
spoty = 0

function make_appels(){
    for (let index = 0; index < max_appels; index++) {
        spotx = Math.floor(Math.random() * 99)
        spoty = Math.floor(Math.random() * 99)
        document.getElementById("box" + spotx.toString() + "x" + spoty.toString() + "y").style.backgroundColor = "red";
    }
}
function create_gird(){
    xl = BOARD_SIZE[0]
    yl = BOARD_SIZE[1]
    xg=0
    yg=0
    gtc = ""
    for (let i=0; i < xl; i++){ gtc += " " + BASE_SIZE}

    game_board.style.gridTemplateColumns = gtc
    game_board.style.gridTemplateRows = gtc + " 20px"
    
    for (let index = 0; index < yl; index++) {
        for (let index = 0; index < xl; index++) {
            let element = document.createElement("div")
            element.style.background = BG_COLOR
            element.style.border = BORDER
            element.id = ("box" + xg.toString() + "x" + yg.toString() + "y")
            game_board.appendChild(element)
            xg += 1
        }
        xg = 0
        yg += 1
    }

    make_appels()

}

function draw(){
    try{

        if (direction == "right"){
            //update pos
            x += 1
            snake.x = x
            snake.y = y
            //draw snake
            document.getElementById("box" + snake.x + "x" + snake.y + "y").style.backgroundColor = "blue";
            if (used_boxes.includes("box" + snake.x + "x" + snake.y + "y")  && used_boxes[used_boxes.length-1] != ("box" + snake.x + "x" + snake.y + "y")){
                alert("Game over")
                playing = false
            }
            //remove last pice 
            used_boxes.push(("box" + snake.x + "x" + snake.y + "y"))
            
        }
        if (direction == "left"){
            //update pos
            x -= 1
            snake.x = x
            snake.y = y
            //draw snake
            document.getElementById("box" + snake.x + "x" + snake.y + "y").style.backgroundColor = "blue";
            if (used_boxes.includes("box" + snake.x + "x" + snake.y + "y")  && used_boxes[used_boxes.length-1] != ("box" + snake.x + "x" + snake.y + "y")){
                alert("Game over")
                playing = false
            }
            //remove last pice 
            used_boxes.push(("box" + snake.x + "x" + snake.y + "y"))
        }
        if (direction == "up"){
            //update pos
            y -= 1
            snake.x = x
            snake.y = y
            //draw snake
            document.getElementById("box" + snake.x + "x" + snake.y + "y").style.backgroundColor = "blue";
            if (used_boxes.includes("box" + snake.x + "x" + snake.y + "y")  && used_boxes[used_boxes.length-1] != ("box" + snake.x + "x" + snake.y + "y")){
                alert("Game over")
                playing = false
            }
            //remove last pice 
            used_boxes.push(("box" + snake.x + "x" + snake.y + "y"))
       
        }
        if (direction == "down"){
            //update pos
            y += 1
            snake.x = x
            snake.y = y
            //draw snake
            document.getElementById("box" + snake.x + "x" + snake.y + "y").style.backgroundColor = "blue";
            if (used_boxes.includes("box" + snake.x + "x" + snake.y + "y") && used_boxes[used_boxes.length-1] != ("box" + snake.x + "x" + snake.y + "y")){
                alert("Game over")
                playing = false
            }
            //remove last pice 
            used_boxes.push(("box" + snake.x + "x" + snake.y + "y"))
        }

        if(x == spotx && y == spoty){
            snake.len += 1
            make_appels()
        }
       
 
    }
    catch(err){
        alert("Game over")
        playing = false
    }                                                                                              
}

async function main(){
    //INPUT 
    window.addEventListener("keydown", function (event) {
        if (event.defaultPrevented) {
          return; // Do nothing if the event was already processed
        }
      
        switch (event.key) {
          case "ArrowDown":
            if (direction != "up"){
                direction = "down"
            }
            break;
          case "ArrowUp":
            if (direction != "down"){
                direction = "up"
            }
            break;
          case "ArrowLeft":
            if (direction != "right"){
                direction = "left"
            }
            break;
          case "ArrowRight":
            if (direction != "left"){
                direction = "right"
            }
            break;
          default:
            return;
        }
      
        // Cancel the default action to avoid it being handled twice
        event.preventDefault();
      }, true);
    
    //main loop
    while (playing == true){
        draw()
        if (used_boxes.length >= snake.len+1){
            document.getElementById(used_boxes[0]).style.backgroundColor = BG_COLOR;
            used_boxes.shift()
        }
        await new Promise(r => setTimeout(r, SPEED));
    }
}

create_gird(BOARD_SIZE)
main()

