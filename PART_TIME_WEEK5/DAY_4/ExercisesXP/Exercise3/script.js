// In your Javascript file add the functionality which will allow you to drag the box and drop it 
//into the target. Check out the Course Notes named DOM animations.

document.addEventListener("DOMContentLoaded", function () {
    const box = document.getElementById('box');
    let toDrag = false;
    let offsetX, offsetY;

    //mouse down
    box.addEventListener('mousedown', function (e) {
        const box = document.getElementById("box");
        toDrag = true;
        offsetX = e.clientX - box.getBoundingClientRect().left;
        offsetY = e.clientY - box.getBoundingClientRect().top;
        
    });

    //move with mouse
    document.addEventListener('mousemove', function(e) {
        if (toDrag) {
            box.style.left = e.clientX - offsetX + "px";
            box.style.top = e.clientY - offsetY + "px"
        }
    });

    //stop
    document.addEventListener('mouseup', function () {
        toDrag = false;
    });

    //target box
    const target = document.getElementById('target');

    // drop when box is in target box
    target.addEventListener('drop', function (e) {
        e.preventDefault();
        const data = e.dataTransfer.getDataData('text');

        if (data === 'box') {
         target.style.background = 'green';

        }
    target.addEventListener('dragover', function (e) {
        e.preventDefault();
    })
    })
} )

//also added attribute to box in html to be draggable
// it's working, but not very smoothly, could you tell me why?