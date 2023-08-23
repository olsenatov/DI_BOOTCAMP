//2
let navBar = document.getElementById('navBar')
navBar.setAttribute('id', 'socialNetworkNavigation')
console.log(navBar)
//3.1
let listTagLogout = document.createElement('li')
//3.2
let logoutTextNode = document.createTextNode('Logout')
//3.3
listTagLogout.appendChild(logoutTextNode)
console.log(listTagLogout)
//3.4
ulMenu =document.querySelector('ul') 
ulMenu.appendChild(listTagLogout)
//4
let firstLi = ulMenu.firstElementChild
let lastLi = ulMenu.lastElementChild

console.log(`fist link text: ${firstLi.textContent}`)
console.log(`last link text: ${lastLi.textContent}`)
