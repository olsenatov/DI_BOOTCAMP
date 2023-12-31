// // Part I
// // In your Javascript file, using setTimeout, call a function after 2 seconds.
// // The function will alert “Hello World”.
// function sayHello() {
//     alert('Hello World');
// }
// setTimeout(sayHello, 2000);


// // Part II
// // In your Javascript file, using setTimeout, call a function after 2 seconds.
// // The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// function addP() {
//     let par = document.createElement('p');
//     par.textContent = 'Hello World';

//     let container = document.getElementById('container');
//     container.appendChild(par);
// }

// setTimeout(addP, 2000)


// Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

let interval
function addP() {
    let par = document.createElement('p');
    par.textContent = 'Hello World';

    let container = document.getElementById('container');
    container.appendChild(par);

    let countP = container.querySelectorAll('p').length

    if(countP === 5) {
        clearInterval(interval)
    }

}

interval = setInterval(addP, 2000)
