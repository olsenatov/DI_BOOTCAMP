// EVENTS basics

// function clicked(){
//     alert('Button was clicked');  //// to connect to html #1

// }

// const button = document.getElementById('clickEvent') //// declare a variable

// console.log(button)
// button.addEventListener('click', clicked) . //// adding a listener and connect through id #2

// button.addEventListener('click', function click(){
//     alert('clicked button');  //// add listener and function in one line simultaneously #3
// })

// button.addEventListener('click', () => {
//     alert('clicked');     //// one line function #4
// })

// button.addEventListener('click', () => {
//    button.style.backgroundColor = 'red'     //// one line function #4
// })
// button.onclick = clicked;

// function mouseOver(){
//    console.log('mouse over');  //// to connect to html #1

// }

// button.onmouseover = mouseOver;
// innerDiv.onmouseout = mouseOver;

////EXERCISE 1
// const table = document.getElementById('sampleTable')

// function insertRow(){
//     const newRow=document.createElement('tr');
//     const td1 = document.createElement('td');
//     const td2 = document.createElement('td');
//     td1.innerText= 'cell1'
//     td2.innerText='cell2'
//     newRow.append(td1, td2);
//     table.append(newRow);
// }


////MULTIPLE EVENTS
// let x = document.getElementById("innerDiv")
    

// x.addEventListener("click", RespondClick); 
// x.addEventListener("mouseover", RespondMouseOver); 
// x.addEventListener("mouseout", RespondMouseOut); 

// function RespondClick() { 
//     alert("div Clicked")
// } 

// function RespondMouseOver() { 
//     alert("My mouse is over the div")
// } 

// function RespondMouseOut() { 
//     alert("My mouse is out of the div")
// }     


////TRANSFERRING INPUT TEXT
// function RespondClick(e) { 
//     console.log(e)
// } 
// const innerDiv= document.getElementById('innerDiv')
// const myInput = document.getElementById('myInput');

// myInput.oninput =function(e){
//     innerDiv.innerText = console.log(e.target.value);
// }

//// THE MOST INNER CHILD WILL BE THE BEGINNING of the event
// const parentDiv = document.getElementById('parent')
// const childDiv = document.getElementById('child')
// const infantDiv = document.getElementById('infant')

// parentDiv.style.height = '300px'
// childDiv.style.height = '200px'
// infantDiv.style.height = '100px'
// parentDiv.style.border = '1px solid black'
// childDiv.style.border = '2px solid red'
// infantDiv.style.border = '3px solid green'

// parentDiv.onclick = console.log('parent')
// childDiv.onclick = console.log('child')
// infantDiv.onclick = console.log('infant')

////FORMS
// console.log(document.forms[0].name)
// document.forms[0].elements.firstFormInput.value = 'hello I am value'

// function getValue(event){
//     event.preventDefault()
//     console.log(event.target.elements.fname.value) ////ALWAYS PUT ONSUBMIT  ALSO TO HTML FORM
//     console.log(event.target.elements.lname.value)
// }

////SELECT/DROPDOWN
 //get the select form
//  let dropdown = document.getElementById('A')

//  // all three lines do the same thing
//  dropdown.options[2].selected = true; //Banana selected
//  dropdown.value = 'banana'; //Banana selected
//  dropdown.selectedIndex = 2; //Banana selected

//  // To check which option is selected
//    console.log(dropdown.selectedIndex) // "2"
//    console.log(dropdown.value) // "Banana"

////FORM VALIDATION
valid
.setCustomValidity('')

