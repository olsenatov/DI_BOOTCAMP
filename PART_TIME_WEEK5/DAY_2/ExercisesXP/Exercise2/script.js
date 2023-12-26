// Retrieve the form and console.log it.
let form = document.querySelector('form');
console.log(form);
// Retrieve the inputs by their id and console.log them.
let fName = document.getElementById('fname');
let lName = document.getElementById('lname');
console.log(fName);
console.log(lName);
// Retrieve the inputs by their name attribute and console.log them.
let fNameInput = document.getElementsByName('firstname')[0];
let lNameInput = document.getElementsByName('lastname')[0];
console.log(fNameInput);
console.log(lNameInput);
// When the user submits the form (ie. submit event listener) use event.preventDefault(), why ?
// get the values of the input tags, make sure that they are not empty, create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.
let userAnswer = document.createElement('ul');
userAnswer.classList.add('userAnswer');

form.addEventListener('submit', function(e) {
    e.preventDefault()

    if (fNameInput.value === '' || lNameInput.value === '') {
        alert('please, fill in both first and last name')
        return
    }
    let userAnswer = document.createElement('ul');
    userAnswer.classList.add('userAnswer')
    
    let inputValues = [fNameInput.value, lNameInput.value];

    for (let value of inputValues) {
        let listItem = document.createElement('li');
        listItem.textContent = value;
        userAnswer.appendChild(listItem);
    }

    const namesList = document.querySelector('.userAnswer');
    form.insertAdjacentElement('afterend', userAnswer);

    fNameInput.value = '';
    lNameInput.value ='';
})
//somehow appends to the list from the beginning (top of the list), not from the end (bottom)


//The output should be :
// <ul class="usersAnswer">
//     <li>first name of the user</li>
//     <li>last name of the user</li>
// </ul>