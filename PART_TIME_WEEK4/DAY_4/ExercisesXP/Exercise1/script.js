// Exercise 1 : Users
// Instructions
// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>
// Add the code above, to your HTML file

// // Using Javascript:
// // Retrieve the div and console.log it

// const containerDiv = document.getElementById('container');
// console.log(containerDiv)

// // Change the name “Pete” to “Richard”.
// let peteName = document.querySelector('ul.list li:nth-child(2)');
// peteName.textContent = 'Richard'
// console.log(peteName)

// Delete the <li> that contains the text node “Sarah”. (It’s the second <li> of the second <ul>)
// const listItems = document.querySelectorAll('li');
// listItems.forEach(item => {
//     if(item.textContent.includes('Sarah')) {
//         item.remove()
//     }
// })
// console.log(listItems)

// Change each first name of the two <ul>'s to your name. (Hint : use a loop)
// const allLists = document.querySelectorAll('.list');
// allLists.forEach((list) =>{
//     const firstLi = list.querySelector('li:first-child');
//     firstLi.textContent = 'Ola';
// })
// console.log(allLists)

// // Bonus - Using Javascript:
// // Add a class called student_list to both of the <ul>'s.

// // const allUl = document.querySelectorAll('ul.list')
// allUl.forEach(ul => {
//     ul.classList.add('student_list');
// });

// // Add the classes university and attendance to the first <ul>.

// const firstUl = document.querySelector('ul.list:first-of-type');
// firstUl.classList.add('university', 'attendance');

