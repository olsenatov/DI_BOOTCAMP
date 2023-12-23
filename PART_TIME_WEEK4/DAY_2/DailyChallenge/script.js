
// Prompt the user for several words (separated by commas).
// Put the words into an array.
// Console.log the words one per line, in a rectangular frame as seen below.
// Check out the Hints and Requirements below.
// For example, if the user gives you:
// Hello, World, in, a, frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
// that will get displayed as:

// Hint
// The number of stars that wraps the sentence, must depend on the length of the longest word.
const userInput = prompt('Enter words separated by commas');
function printInFrame(words) {
    const wordsArray = words.split(',').map(word => word.trim());
    const maxLength = Math.max(...wordsArray.map(word => word.length));
    
    const horizontalLine = '*'.repeat(maxLength +4)
    console.log(horizontalLine);

    wordsArray.forEach((word) => {
        const spaces = " ".repeat(maxLength - word.length);
        console.log(`* ${word}${spaces} *`);
        })
    console.log(horizontalLine)
}

// is this solution too much for this level? i did it because i know a bit more, but maybe there's a simplier way?
printInFrame(userInput)




  



  
