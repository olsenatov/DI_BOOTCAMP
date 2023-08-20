// Functions
// console.log('Testing....')

// function greet(){
//     console.log('Welcome');
// }

// greet();

// function greet(username, age){
//     // console.log('Welcome ' + username + age);
//     console.log(`Welcome ${username} your age is ${age}`) // better to use this
// }

// greet('Olga123', 20);

// function calculate(x, y, z) {
//     console.log('a' + x + y + z);
//     console.log( x + y + z + 'a');

// }

// calculate (2, 3, 1)


// // FUNCTION DEFAULT VALUE
// function greet(username, age = 20){ // looks at it, when no value is defined

//     console.log(`Welcome ${username} your age is ${age}`) 
// }

// greet ('Ola') 

// // GLOBAL/LOCAL SCOPES VARIABLES

// function userMoreInfo (userName, userAge) {
//     let eyeColor = "blue"; //local variable, can't acsess it outside
//     console.log("My name is " + userName + ", my age is "  + userAge + ", I have " + eyeColor + " eyes");
// }

// userMoreInfo("Sarah", 22);

// function familyAge(x) {
//     console.log(`my age is ${x}, my mom's age is ${x*2} and my Dad's is ${(x*2)*1.2}`)
// }

// familyAge(30)

// // RETURN STATEMENT
// function calculate (x, y) {
//     let mySum = x + y;
//     // console.log(mySum);
//     return mySum // the moment return is stated - function exits
// }

// const sum = calculate(1,2);
// console.log(sum); 

// TRY/EXCEPTIONS/CATCH

// function exeptions() {
//     try {
//         console.log(greeting)
    
//     }
//     catch(e) { // catching an error
//         console.log(e.name);
//         console.log(e.message);
//         console.log(e.stack);
//     } finally {
//         console.log('Hello') // will run in any case
//     }
// }

// THROW NEW ERROR
// function calc(x, y) {
//     const sum = x+y;
//     try {

//     if (sum > 10) {
//         throw new Error ('Your Number was bigger than allowed (10)')
//         }
//     else {
//         console.log(sum);
//         }
//     }
//     catch (e) {
//         console.log(e);
//     }
// }
// calc(8, 2)



// OBJECT


// const person = {
//     fname: 'Olga',
//     lname : 'Senatov',
//     eat: function () {
//         console.log(`I love spinach and my name is ${this.fname}`); 
//         // /this\ gives acsess to the key value
//     }
// };
// console.log(person.fname);
// console.log(person.lname);
// person.eat()



