$('#map').click(document.addEventListener("click", MousePos));
let clicks = $('#clicks');
let message = $('#message');
let map = document.getElementById('map')

let width = 1000;
let height = 500;
let clickBase = 30;
let clickCounter = clickBase;
let playing = false
let treasure = { x: Math.floor(Math.random() * width), y: Math.floor(Math.random() * height) }


let mousex = 0;
let mousey = 0;


function getRandomNumber(max) {
   return Math.floor(Math.random() * max);
}

function MousePos(event) {
    if (!playing){
        clickCounter -= 1
        clicks.text(clickCounter)
        if (clickCounter == 0){
            playing = true
            message.text("You lost!")
        }
        else{
            update(event.clientX, event.clientY)
        }
    }
}

function update(x,y) {
    if (!playing){
        dist = getDistance([x,y],treasure.x, treasure.y)
        getMessage(dist)
    }

    
}

function getDistance(event,treasurex, treasurey) {
    let diffX = event[0]
    let diffY = event[1]
    
    return Math.round(Math.sqrt (Math.pow(((treasurex)-diffX),2) + Math.pow(((treasurey)-diffY),2)))   //d=√( (x_2-x_1)² + (y_2-y_1)² )
    
}

function getMessage(value) {
   if (value < 50){
       message.text("You won!, With a click just " + value + " away from the tressure")
       playing = true
   }
   if (value > 50 && value < 150){
    message.text("Oh close!, With a click just " + value + " away from the tressure")

   }
   if (value > 150 && value < 350){
    message.text("On the right path, With a click " + value + " away from the tressure")

   }   
  if (value > 350 && value < 650){
    message.text("hmm not to good, With a click " + value + " away from the tressure")
  
   }
  if (value > 650 && value < 850){
    message.text("not good!, With a click " + value + " away from the tressure")

   }
  else if(value>850){
    message.text("oh no no!, you clicked " + value + " away from the tressure")
    
  }
  

}

function replay() {
    document.removeEventListener("click", MousePos)
    clickBase = 30;
    clickCounter = clickBase;
    playing = false
    treasure = { x: Math.floor(Math.random() * width), y: Math.floor(Math.random() * height) }
    mousex = 0;
    mousey = 0;
    message.text("Click the Map to Begin!")
    clicks.text(clickCounter)
}

function addlistener(){
    document.addEventListener("click", MousePos)
}

