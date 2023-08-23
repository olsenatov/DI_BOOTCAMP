//2.1
const containerDiv = document.getElementById('container');
console.log(containerDiv)
//2.2
let peteName = document.getElementById('peteName')
peteName.textContent = 'Richard'
console.log(peteName)
//2.3
const secondUl = document.getElementById('secondUl')
const deleteSarah = document.getElementById('sarahName')
deleteSarah.remove()
console.log(secondUl)

//2.4
const allLists = document.querySelectorAll('.list');
allLists.forEach((list) => {
    const firstLi = list.querySelector('li:first-child');
    firstLi.textContent = 'Ola';
        });
console.log(allLists)
//3.1
allLists.forEach((list) => {
    list.classList.add('student_list');
});
console.log(allLists)
//3.2
const firstUL = document.querySelector('.list')
firstUL.classList.add('university', 'attendance');
console.log(firstUL)
//4.1
containerDiv.style.backgroundColor = 'lightblue'
containerDiv.style.padding = '20px'
//4.2
const danLiElement = secondUl.querySelector('li:nth-child(2)')
danLiElement.style.display = 'none' 
////i give up, i got stuck on this for far too long, gives me an error: Cannot read properties of null (reading 'querySelector')
// i actually checked, and because i've deleted sarah earlier, it's now not the 3rd element, but the 2nd! 
//is it made intentionally or should i comment out each task ?
//4.3
peteName.style.border = '1px solid black'
//4.4
document.body.style.fontSize = '25px'