////Exercise 1
// let headingOne = document.querySelector('h1')
// console.log(headingOne)

// let article = document.querySelector('article');
// let lastP = article.lastElementChild
// article.removeChild(lastP)

// let headingTwo = document.querySelector('h2')
// headingTwo.addEventListener('click', () => {
// headingTwo.style.backgroundColor = 'red'});

// let headingThree = document.querySelector('h3')
// headingThree.addEventListener('click', () => {
// headingThree.style.display = 'none'});

// let boldButton = document.getElementById('boldButton')
// let allP = document.querySelectorAll('p')
// boldButton.addEventListener('click', () => {
//     allP.forEach(eachP => {
//         eachP.style.fontWeight = 'bold'
//     })
// });

// headingOne.addEventListener('mouseenter', () => {
//     let randomFontSize = Math.floor(Math.random() * 101)
//     headingOne.style.fontSize = `${randomFontSize}px`
// })
// headingOne.addEventListener('mouseleave', () =>{
//     headingOne.style.fontSize =''
// })

// let fadingP = document.getElementById('fadingP')
// fadingP.addEventListener('mouseenter', () =>{
//     fadingP.style.opacity = '0'
// })

// fadingP.addEventListener('mouseleave', () =>{
//     fadingP.style.opacity = ''
// })


////Exercise 2

// let form = document.querySelector('form')
// console.log(form)

// let fName = document.getElementById('fname')
// let lName = document.getElementById('lname')
// console.log(fName)
// console.log(lName)

// let fNameInput = document.getElementsByName('firstname')[0]
// let lNameInput = document.getElementsByName('lastname')[0]
// console.log(fNameInput)
// console.log(lNameInput)

// let userAnswer = document.createElement('ul')
// userAnswer.classList.add('userAnswer')

// form.addEventListener('submit', function(e) {
//     e.preventDefault()

//     if (fNameInput.value === '' || lNameInput.value === '') {
//         alert('please, fill in both first and last name')
//         return
//     }

//     let userAnswer = document.createElement('ul')
//     userAnswer.classList.add('userAnswer')

//     let inputValues = [fNameInput.value, lNameInput.value];

//     for (let value of inputValues) {
//         let listItem = document.createElement('li');
//         listItem.textContent = value;
//         userAnswer.appendChild(listItem); }

    

//     const namesList = document.querySelector(".userAnswer");
//     form.insertAdjacentElement("afterend", userAnswer);


//     fNameInput.value = ''
//     lNameInput.value = ''


// })

////Exercise 3

// let allBoldItems
// function getBoldItems() {
//     allBoldItems = document.querySelectorAll('p strong')
//   }

// function highlight() {
//     getBoldItems()
//     allBoldItems.forEach(eachItem => {
//                  eachItem.style.color = 'blue'
//     })
//   }

// function returnItemsToDefault() {
   
//     highlight()
//     allBoldItems.forEach(eachItem => {
//         eachItem.style.color = 'black'
// })
//   }

// const normP = document.querySelector('p')
// normP.addEventListener('mouseover', highlight());
// normP.addEventListener('mouseout', returnItemsToDefault());

////somehow it doesn't work, although there're no errors in console 
/// will be glad to understand what is the issue


////Exercise 4
// const form = document.getElementById('MyForm')
// let radiusInput = document.getElementById('radius')
// let volumeInput = document.getElementById('volume')

// form.addEventListener('submit', function(e){ 
//     e.preventDefault()

//     let radius = parseFloat(radiusInput.value)
//     if (!isNaN(radius)) {
//         let volume = (4/3) * Math.PI * Math.pow(radius, 3)
//         volumeInput.value = volume.toFixed(2)
//     } else {
//         volumeInput.value = ''
//     }

// })

////Exercise 5
let changeableElement = document.getElementById('changeable');

changeableElement.addEventListener('click', function() {
    let newX = changeableElement.style.top +  Math.floor(Math.random())
    changeableElement.style.top = `${newX}px`;
});

changeableElement.addEventListener('mouseover', function() {
    const newY = Math.floor(Math.random())
    changeableElement.style.top = `${newY}px`;
});

// Event listener to change color
changeableElement.addEventListener('mouseout', function() {
    const colors = ['red', 'green', 'blue', 'orange', 'purple'];
    const newColor = Math.floor( Math.random(colors.length))
    changeableElement.style.backgroundColor = newColor;
});

// Event listener to change font size
changeableElement.addEventListener('dblclick', function() {
    const newSize = Math.floor(Math.random() * 40) + 10;
    changeableElement.style.fontSize = `${newSize}px`;
});





