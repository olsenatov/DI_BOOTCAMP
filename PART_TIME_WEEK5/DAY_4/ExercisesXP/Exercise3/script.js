// Exercise 3 : Change The Navbar
// Instructions
// <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>
// Add the code above, to your HTML file

// Using Javascript, in the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.
let navBar = document.getElementById('navBar');
navBar.setAttribute('id', 'socialNetworkNavigation')
console.log(navBar)
// We are going to add a new <li> to the <ul>.

// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (<li>).
// Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.
let listTagLogout = document.createElement('li');
let logoutTextNode = document.createTextNode('Logout');
listTagLogout.appendChild(logoutTextNode);
console.log(listTagLogout);
ulMenu = document.querySelector('ul');
ulMenu.appendChild(listTagLogout);

// Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). 
//Display the text of each link. (Hint: use the textContent property).

let firstLi = ulMenu.firstElementChild;
let lastLi = ulMenu.lastElementChild;

console.log(`first link text: ${firstLi.textContent}`);
console.log(`last link text: ${lastLi.textContent}`)