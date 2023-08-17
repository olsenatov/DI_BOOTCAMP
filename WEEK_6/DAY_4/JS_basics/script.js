
// // CONSOLE LOG
// console.log("Hello World")
// console.log('lorem ipsum')

// // VARIABLES
// let x = 3; // declaring with let/const
// console.log(3);
// let my_name = 'Ola' //start with letters
// let My_name = 'ola' // key sensitive

// // CAMEL CASE
// let thisIsMyName = 'Ola' //first letter is low, everynew word in variable is from capital

// // UNDEFINED
// log a;
// console.log(a);


// // DATA TYPES
// // strings
// let exampleString = 'Hello';
// let exampleString2 = 'World';

// console.log(exampleString + ' ' + exampleString2); //defined inside log is not saved anywhere

// console.log('2') //inside quotes anything is a string
// console.log(2) // not the same thing

// let longString = 'lorem ipsum \ to take you down one line \ and maybe one more'
// console.log(longString)

// // // STRING PROPERTIES and METHODS
// let myName = 'Ola is a student';
// // console.log(myName.length); // . -acssess property of the string

// // // INDEX OF
// console.log(myName.indexOf('Ola')); // () - (method) // to see index of the string
// console.log(myName.indexOf('a')); // index of the letter in the string

// // // SUBSTRING
// console.log(myName.substring(0,3)) // making a substring in the range of

// // toLOWERCASE
// let myString = 'AbCdEfG'
// console.log(myString.toLowerCase())

//!!!!! EXERCISE
// let addressNumber = 'London, 10';
// let addressStreet = 'Downing street';
// let country = 'UK';

// let globalAddress = addressNumber + ' ' + addressStreet + 'in' + ' ' + country;
// console.log('I live in' + globalAddress)


// // NUMBERS
// console.log(10/2);
// console.log(10-2);
// console.log(10*2);
// //isNaN
// let op='me';
// console.log(isNaN(op));//is not a number? boolean true or false

// let ten=10;
// console.log(ten);
// console.log(ten.toString());

// //COMPARISON
// let x = 2 ;// = defines the variable
// console.log(x == '2');//== checks value regardless of type

// console.log(1===1); // === comparing 
// console.log(x != 2); // != not equal
// console.log(x >= 2); // > greater than or equal
// console.log(x > 2); // greater than
// console.log(x>1 && x<3); // check for 2 conditions simultaneously
// console.log (x>5 || x===2) // check for one ||OR|| another

// // // Working with numbers
// x=4//redefines the variable 
// x++ //now x=x+1
// console.log(x)

// // USER INTERFACE FUNCTIONS

// console.log('Before Alert');
// alert('Welcome to my website'); . // ALERT
// console.log("After Alert");

// let userAnswer = prompt('What is your name', 'Guest'); // PROMT, variable stores and can pass the answer of the user, 
//                                                       //"2nd text is a default value"
// console.log("Welcome to the website " + userAnswer); 

// let isBoss = confirm('Are you the boss?'); //if the user presses in the popup okay - True, cancel - False
// console.log(isBoss); 

// // ARRAYS
// // multiple variables in a single value [list]

// let users = ['Daniel', 'Alex', 'Ola', 'Lea'];
// let x = 1
// console.log(typeof x) . // TYPEOF
// console.log(typeof users) //RETURNS object, but it's actually an array
// console.log(users[1]) //user at [POSITION] in THE ARRAY/LIST


// let sampleArray = [
//     [1, 2, 5],
//     [7, 6, 10, 11, 12],
//     [3]
// ]
// console.log(sampleArray[0][1]) // get element at POSITION in the 1st list of the array in the 2D list, of the 2nd element 

// let colors = ['pink', 'blue', 'green'];
// console.log(colors);
// colors[1] = 'yellow'; // REDEFINE ELEMENT of ARRAY AT SPECIFIC POSITION
// console.log(colors); 

// console.log(colors.length); // LENGTH - 3
// let arrayLength = colors.length // STORES THE VALUE

// ARRAY METHODS
// let colors = ['pink', 'blue', 'green'];
// colors.push('yellow'); // ADDS NEW ELEMENT IN THE END of the ARRAY
// colors.push('purple');
// console.log(colors);

// colors.pop() // REMOVES THE LAST ELEMENT of the ARRAY - always edits the origin
// console.log(colors);

// let colors = ['pink', 'blue', 'green'];
// console.log(colors);

// colors.splice(1, 2, 'ORANGE', 'red' ) //REMOVE FROM POSITION 1, 2 ELEMENTS, INSTEAD PUT the NEW ELEMENT(s)
// console.log(colors);

// let colors = ['pink', 'blue', 'green'];

// let slicedArray = colors.slice(1,3) // does not affect origin array, gives NEW ARRAY with ELEMENTS in range from the origin
// console.log(colors);
// console.log(slicedArray);

// let pets = ['cat','dog','fish','rabbit','cow'];
// console.log(pets[1])
// pets.splice(3,1, 'horse')
// console.log(pets)
// let petsLen = pets.length
// console.log(petsLen)



// // OBJECTS
//kind of dictionaries to store multiple lines of data

// let person = { //defines the OBJECT with key-value pairs
//     firstName : 'John',
//     // key : value
//     lastName : 'Smith',
//     age : 25,
//     eyeColor : 'blue'
// };
// console.log(person.firstName) // acsess value of the key in object
// console.log(person.age)
// console.log(person.eyeColor)

// // // ADD CHANGE VALUES
// person.country = 'Israel'  // CREATE and ADD
// console.log(person)

// person.age = 27  // CHANGE
// console.log(person)

// delete person.age   // REMOVE key with value from OBJECT
// console.log(person)


// // IF _ CONDITIONALS if (){} else{}    if(){} else if(){}else

// let x = 20;

// if (x >= 21) {
// console.log("You can drink in US");
// }

// let x = 22;

// if (x >= 21) {
// console.log("You can drink in the US");
// } else { //the other option
//     console.log('You are too young to drink in the US')
// }

// let x = 17;

// if (x >= 21) {
// console.log("You can drink in the US");
// } else if (x >=18) {
//     console.log("you can drink outside US")
// } else if (x >=16 && x <18) {
//         console.log("you can drink in Germany")
// } else { 
//     console.log('You are too young to drink')
// }

//!!!!! EXERCISE

// let userAnswer = prompt('What is your age?');
// if (userAnswer < 18){ 
//  alert('Sorry, you are too young to drive this car. Powering off')

// }  else if (userAnswer == 18){ 
//     // == because of string type that answer recieves there and compares it to number type
//     alert('Congratulations on your first year of driving. Enjoy the ride!')
// }
// else  { 
//     alert('Powering On. Enjoy the ride!')
// }


// // SWITCH CASE
// let fruit = 'Papayas'

// switch(fruit) { // (fruit) - checking it
//     case "Oranges": //if it's equal to oranges, then:
//         console.log("oranges are $1 per kilo");
//         break; // if condition is executed, stop the checking
    
//     case Mangoes:
//     case Papayas: // can be multiple case per each answer
//         console.log('Mangoes and papayas are $2 per kilo');
//         break;

//     default:
//         console.log("Sorry we are out of " + fruit);
//         // if there's nothing suitable for condition - default (like else)

// }


// // LOOPS
// for loop

// for(let i = 0; i < 5; i++) {
// // with what loop starts - 
// //(how many itterations i; 
// // as long as i has not become...; 
// // what happens to i each time loop goes)
// console.log('the current number is' +i)

// }

// LOOP through ARRAY
// let colors = ['red', 'blue', 'green', 'purple', 'pink']

// for (let i = 0; i < colors.length; i++){ // length - to make it dynamic
//     console.log(colors[i]); //utilizing [index] to acsess position of the array's element
//     console.log('the ' + (i + 1) + ' color is ' + colors[i]); // to add the count
// }

// FOR IN (object)
// let person = {
//     firstName : "Ola",
//     age : '30',
//     country : 'Israel',

// }
// for (let key in person) { // the only way to LOOP THROUGH OBJECT
//         // key can be i, name, whatever
//         console.log(key);
//         console.log("Key is " + key + "// Value is " + person[key]); 
// }

// LOOPS FOR/OF (array)
// let colors = ['red', 'blue', 'green', 'purple', 'pink']
// let x = 0
// for (let i of colors) {
//     console.log('the color at position ' + x + i);
//     x++;
// }

// // WHILE LOOP
// let n = 0;
// while (n<3){ //while condition is true keep doing:
//     console.log(n);
//     n++;
// }

// let answer = promt('What is the secret password?')
// while (answer != '1234'){
//       answer = promt('What is the secret password?');
// }
// alert('Welcome Admin');

// // DO WHILE

// let i = 0

// do{ // DO something WHILE the condition is TRUE (it will run at least 1 time no matter what)
//     console.log('the namber is ' + i);
//     i++;
// } while(i < 10);

// // // BREAK Statement
// for (let i = 0; i < 10; i++) {
//     if (i===3) {
//         break; //break the loop when the condition is satisfied
//     }
//     console.log(i);
// }

// for (let i = 0; i < 10; i++) {
//     if(i===3){
//         continue; // skip loop for this condition
//     }
//     console.log(i);
// }

// // CONST
const yourName = 'Ola'; // unchangeble constant variable
console.log(yourName);
yourName = 'Alex' // Error
// The best practice to protect variable