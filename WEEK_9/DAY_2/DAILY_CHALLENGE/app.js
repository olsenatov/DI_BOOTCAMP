import greet from './greeting.js';
import displayColor from './colorful_message.js';

import readAndDisplay from './read_file.js';

const name = 'Mike';

console.log(greet(name));

const word1 = 'Look';
const word2 = ' what I ';
const word3 = 'can do!';

displayColor(word1, word2, word3);

readAndDisplay();

// didn't quite understand the need of challenge.js file 
// if i have aggregated all the functions inside this file