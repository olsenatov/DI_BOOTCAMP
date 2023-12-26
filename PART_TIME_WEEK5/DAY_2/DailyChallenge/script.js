// Instructions
// In todays exercise we will be creating a Mad Libs game.
// If you’ve never played this game, a mad lib is a game where you fill in a bunch of blank inputs with different word types (ie : noun, adjective, verb), and then a story is generated based on the words you chose, and sometimes the story is surprisingly funny.

// In this exercise you work with the HTML code presented below.

// Follow these steps :

// Get the value of each of the inputs in the HTML file when the form is submitted. Remember the event.preventDefault()
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should change the story currently displayed (but keep the values entered by the user). The user could click the button at least three times and get a new story. Display the stories randomly.

const form = document.getElementById('libform');
const noun = document.getElementById('noun');
const adjective = document.getElementById('adjective');
const person = document.getElementById('person');
const verb = document.getElementById('verb');
const place = document.getElementById('place');
const story = document.getElementById('story');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    getAllInputsValues()
})

function getAllInputsValues() {
    if(!validateValueInput(noun.value) ||
    !validateValueInput(adjective.value) ||
    !validateValueInput(person.value) ||
    !validateValueInput(verb.value) ||
    !validateValueInput(place.value)) {
        return;
    };
    const mystory = `Far far away in a ${adjective.value} ${place.value}, there lived
    a ${person.value} and he had a magic ${noun.value}. Once he ${verb.value} far away from ${place.value}, 
    and he was rather scared to see himself ${adjective.value}`;

    story.innerText = mystory;
}

function validateValueInput(value) {
    if (value.trim().length === 0) {
        alert("Please enter a value");
        return false;
    }
    return true;
}

