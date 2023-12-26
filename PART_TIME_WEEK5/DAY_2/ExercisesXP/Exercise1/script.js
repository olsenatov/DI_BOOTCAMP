// Using a DOM property, retrieve the h1 and console.log it.
const headingOne = document.querySelector('h1');
console.log(headingOne);

// Using DOM methods, remove the last paragraph in the <article> tag.
const article = document.querySelector('article');
let lastP = article.lastElementChild;
article.removeChild(lastP);

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
let headingTwo = document.querySelector('h2');
headingTwo.addEventListener('click', () => {
    headingTwo.style.backgroundColor = 'red'
})
// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).
let headingThree = document.querySelector('h3');
headingThree.addEventListener('click', () => {
    headingThree.style.display = 'none'
});
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
let boldButton = document.getElementById('boldButton')

let allP = document.querySelectorAll('p')
boldButton.addEventListener('click', () => {
    allP.forEach(eachP => {
        eachP.style.fontWeight = 'bold'
    })
})
// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
headingOne.addEventListener( "mouseover", () => {
    let randomFontSize = Math.floor(Math.random() * 101)
    headingOne.style.fontSize = `${randomFontSize}px`
})
// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

const secondP = document.querySelector('article p:nth-of-type(2)');
secondP.addEventListener('mouseenter', () => { 
    secondP.style.opacity = '0';

} )
secondP.addEventListener('mouseleave', () => { 
    secondP.style.opacity = '';

} )