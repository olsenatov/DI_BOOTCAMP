// // Exercise 2
// // Instructions
// // <div>Users:</div>
// // <ul>
// //     <li>John</li>
// //     <li>Pete</li>
// // </ul>
// // Add the code above, to your HTML file

// // Using Javascript:
// // Add a “light blue” background color and some padding to the <div>.
// let containerDiv = document.querySelector('div')
// containerDiv.style.backgroundColor = 'lightblue';
// containerDiv.style.padding = '20px'

// // Do not display the <li> that contains the text node “John”. (the first <li> of the <ul>)
// const noLiElement = document.querySelector('li:nth-child(1)')
// noLiElement.style.display = 'none'
// // Add a border to the <li> that contains the text node “Pete”. (the second <li> of the <ul>)
// const borderLiElement = document.querySelector('li:nth-child(2)')
// borderLiElement.style.border = '1px solid black'
// // Change the font size of the whole body.
// const fontBody = document.querySelector('body')
// fontBody.style.fontSize = '30px'
// // Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).
// const listItems = document.querySelectorAll('ul.list li');
// const names = Array.from(listItems).map(li => li.textContent.trim());

// if (containerDiv.style.backgroundColor = 'lightblue') {
   
//     const [name1, name2] = names;
//     alert(`Hello ${name1} and ${name2}`);
// }

//doesn't work, could not understand, what is a solution here - I get 'Hello undefined and undefined'