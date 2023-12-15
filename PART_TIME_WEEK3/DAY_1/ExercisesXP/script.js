// // Exercise 1: Your Favorite Food
// // Instructions
// // Store your favorite food into a variable.

// // Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)

// // Console.log I eat <favorite food> at every <favorite meal>

// // For example

// // If your favorite food is "chocolate", 
// // and your favorite meal of the day is "dinner", 
// // you will console.log 
// // I eat chocolate at every dinner


// let myFavFood = "pancakes";
// let myFavMeal = "breakfast";
// console.log(`I eat ${ myFavFood } at every ${myFavMeal}`);


// // Exercise 2 : Series
// // Instructions
// // Part I
// // Using this array : const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

// // Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.

// // Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
// // For example : black mirror, money heist, and the big bang theory

// // Console.log a sentence using both of the variables created above
// // For example : I watched 3 series : black mirror, money heist, and the big bang theory


// const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

// let myWatchedSeriesLength = myWatchedSeries.length;
// console.log(myWatchedSeriesLength);

// let myWatchedSeriesSentence = myWatchedSeries.join(", ")
// console.log(myWatchedSeriesSentence);

// console.log(`I watched ${myWatchedSeriesLength} series: ${myWatchedSeriesSentence}`)

// // Part II
// // Change the series “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.
// // Add, at the end of the array, the name of another series you watched.
// // Add, at the beginning of the array, the name of your favorite series.
// // Delete the series “black mirror”.
// // Console.log the third letter of the series “money heist”.
// // Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.

// myWatchedSeries[2] = "friends";
// myWatchedSeries.push("how i met your mother");
// myWatchedSeries.unshift("gameof thrones");
// console.log(myWatchedSeries);

// myWatchedSeries.splice[1];

// console.log(`The third letter is: ${myWatchedSeries[myWatchedSeries.indexOf('money heist')][2]}`)
// console.log(myWatchedSeries);


// // Exercise 3 : The Temperature Converter
// // Instructions
// // Store a celsius temperature into a variable.

// // Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
// // Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// // Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32

// const celsiusT = prompt("How much is C temperature");
// alert(`Temperature ${celsiusT}C is ${celsiusT/5*9 + 32}F`);


// // Exercise 4 : Guess The Answers #1
// // Instructions
// // For each expression, predict what you think the output will be in a comment (//) without first running the command.
// // Of course, explain each prediction.
// // Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

// let c;
// let a = 34;
// let b = 21;

// // console.log(a+b) //first expression
// // Prediction: 55
// // Actual: 55

// a = 2;

// console.log(a+b) //second expression
// // Prediction: 23 (the value of a is rewritten)
// // Actual: 23

// // What is the value of c? 
// console.log(c)
// //undefined

// // Analyse the code below, what will be the outcome?
// console.log(3 + 4 + '5');
// // Prediction: 75 (combines together)
// // Actual: 75


// // Exercise 5 : Guess The Answers #2
// // Instructions
// // For each expression, predict what you think the output will be in a comment (//) without first running the command.
// // Of course, explain each prediction.
// // Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

// console.log(typeof(15))
// // Prediction: Number
// // Actual: Number

// console.log(typeof(5.5))
// // Prediction: Float
// // Actual: Number

// console.log(typeof(NaN))
// // Prediction: Number
// // Actual: Number

// console.log(typeof("hello"))
// // Prediction: String
// // ActualString:

// console.log(typeof(true))
// // Prediction: Boolean
// // Actual: Boolean

// console.log(typeof(1 != 2))
// // Prediction: Boolean
// // Actual: Boolean

// console.log("hamburger" + "s")
// // Prediction: hamburgers
// // Actual:

// console.log("hamburgers" - "s")
// // Prediction: hamburger
// // Actual: NaN

// console.log("1" + "3")
// // Prediction: 13
// // Actual: 13

// console.log("1" - "3")
// // Prediction: -2
// // Actual: -2

// console.log("johnny" + 5)
// // Prediction: johnny5
// // Actual:  johnny5

// console.log("johnny" - 5)
// // Prediction: NaN
// // Actual: NaN

// console.log(99 * "hello")
// // Prediction: hello written 99 times
// // Actual: NaN

// console.log(1 != 1)
// // Prediction: False
// // Actual: False

// console.log(1 == "1")
// // Prediction: True
// // Actual: True

// console.log(1 === "1")
// // Prediction: False
// // Actual: False


// Exercise 6 : Guess The Answers #3
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

console.log(5 + "34")
// Prediction: 534
// Actual: 534

console.log(5 - "4")
// Prediction: 1
// Actual: 1

console.log(10 % 5)
// Prediction: 0
// Actual: 0

console.log(5 % 10)
// Prediction: 5
// Actual: 5

console.log("Java" + "Script")
// Prediction: Javascript
// Actual: Javascript

console.log(" " + " ")
// Prediction: 2 spaces
// Actual: 2 spaces

console.log(" " + 0)
// Prediction: space 0
// Actual: space 0

console.log(true + true)
// Prediction: true
// Actual: 2

console.log(true + false)
// Prediction: true
// Actual: 1

console.log(false + true)
// Prediction: false
// Actual: 1

console.log(false - true)
// Prediction: NaN
// Actual: -1

console.log(!true)
// Prediction: false
// Actual: false

console.log(3 - 4)
// Prediction: -1
// Actual: -1

console.log("Bob" - "bill")
// Prediction: NaN
// Actual: NaN
