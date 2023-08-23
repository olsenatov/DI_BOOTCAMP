// DOM - document object model

// const myHeader = document.querySelector('h1')
// console.log(myHeader);
// console.log(myHeader.innerText)
// myHeader.innerText = 'Welcome to my PAGE'

// const myList = document.querySelector('ul');
// console.log(myList);
// console.log(myList.firstChild);
// console.log(myList.firstElementChild);
// myList.firstElementChild.innerText = 'BANANA'

// // ACSESS NODES METHODS

// const myP = document.querySelector('p') // acsesses only the fisrt one
// console.log(myP.textContent)

// const myP2 = document.querySelector('#secondP') // acsesses THE ID 
// console.log(myP2.textContent)

// const myP3 = document.querySelector('.red') // acsesses THE CLASS
// console.log(myP3.textContent)

// const myP4 = document.getElementById('secondP') // no need in # for ID selection
// console.log(myP4.textContent)

// .getElementByClassName
// .getElementByTagName

//  MULTIPLE NODES SIMULTANEOUS ACSESS
// const myPs = document.querySelectorAll('p'); // makes a list(array) of things
// console.log(myPs);

// const myBody = document.querySelector('body');
// console.log(myBody.innerText); // only text
// console.log(myBody.innerHTML)  // html tags

// CREATE AN ELEMENT
const myMain = document.querySelector('main')
const newHeader = document.createElement('h2') // create an element
// const headerText = document.createTextNode('This is a new header'); // give it a value

// newHeader.append(headerText) // makes it a child of this node
// myMain.append(newHeader)

// // or shorter:
newHeader.innerText = 'this is a new-super header2'
myMain.append(newHeader)

// newHeader.remove() // deletes the element

// STYLING
newHeader.style.backgroundColor = 'pink' // more specific and will override css styling
myMain.style.border = '2px solid green'

// ATTRIBUTES

const header = document.getElementById('firstheader')
// console.log(header.hasAttribute('id')) // returns boolean in console

// console.log(header.getAttribute('id')); // returns the value of an attribute
// console.log(header.id) // gives the same

// header.setAttribute('style', 'color:blue') // gives attribute and its properties


// header.className = 'bananaheader'
// header.classList.add('pearheader')
// console.log(header.className)
// myMain.style.fontSize = '18px'
// myMain.style.fontFamily = 'Verdana'
// myMain.style.color = 'brown'

// FORMS
// const form1 = document.querySelector('form')
// console.log(form1)
const forms = document.forms;
// console.log(forms[0])
// console.log(forms.my)
// console.log(forms.yours.elements.one)
const myInput = document.getElementById('one')
