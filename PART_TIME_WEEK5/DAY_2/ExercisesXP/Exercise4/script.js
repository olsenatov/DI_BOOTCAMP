// Write a JavaScript program to calculate the volume of a sphere. Use the html code as a base



function calculateVol(radius) {
    return (4/3) * Math.PI * Math.pow(radius, 3)
}

const form = document.getElementById('MyForm')
form.addEventListener('submit', function(event) {
    event.preventDefault();

    const radius = parseFloat(document.getElementById('radius').value);

    if (!isNaN(radius)) {
        const volume = calculateVol(radius).toFixed(2);
        document.getElementById('volume').value = volume;
        console.log(volume)
    } else {
        document.getElementById('volume').value = ''
    }
})


// // could you write me in person in slack or discuss this exercise in class, why it's not working
// i can't seem to understand where to put the result - in the input window? and how to do that?

