// In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions

function myMove() {
    const container = document.getElementById('container');
    const animate = document.getElementById('animate');
    
    const containerWidth = container.offsetWidth;
    const animateWidth = animate.offsetWidth;

    let position = 0;
    let interval = setInterval(frame, 1);

    function frame() {
        if( position >= containerWidth - animateWidth) {
            clearInterval(interval);
        } else {
            position++;
            animate.style.left = position + "px";
        }
    }
}