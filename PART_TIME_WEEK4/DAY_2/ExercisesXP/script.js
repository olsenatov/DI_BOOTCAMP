// // Exercise 1 : Information
// // Instructions
// // Part I : function with no parameters

// // Create a function called infoAboutMe() that takes no parameter.
// // The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
// // Call the function.

// function infoAboutMe() {
//     console.log("My name is Ola, I'm 30, and I love photography and psychology");
// }
// infoAboutMe()

// // Part II : function with three parameters

// // Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
// // The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// // Call the function twice with the following arguments:
// // infoAboutPerson("David", 45, "blue")
// // infoAboutPerson("Josh", 12, "yellow")

// function infoAboutPerson(personName, personAge, personFavoriteColor) {
//     console.log(`Your name is ${personName}, your are ${personAge} years old, your favorite color is ${personFavoriteColor}`);
// }
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")


// // Exercise 2 : Tips
// // Instructions
// // John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

// // Create a function named calculateTip() that takes no parameter.

// // Inside the function, use prompt to ask John for the amount of the bill.

// // Here are the rules
// // If the bill is less than $50, tip 20%.
// // If the bill is between $50 and $200, tip 15%.
// // If the bill is more than $200, tip 10%.

// // Console.log the tip amount and the final bill (bill + tip).

// // Call the calculateTip() function.

// function calculateTip() {
//     let bill = prompt("How much $ is the bill?");

//     if (bill < 50) {
//         console.log(`The tip is $${bill * 0.2} , and the bill is $${bill}`);
//     } else if ( bill > 50 && bill < 200) {
//         console.log(`The tip is $${bill * 0.15} , and the bill is $${bill}`); 
//     } else {
//         console.log(`The tip is $${bill * 0.1} , and the bill is $${bill}`) 
//     }

//     }
// calculateTip()


// // Exercise 3 : Find The Numbers Divisible By 23
// // Instructions
// // Create a function call isDivisible() that takes no parameter.
// // In the function, loop through numbers 0 to 500.
// // Console.log all the numbers divisible by 23.
// // At the end, console.log the sum of all numbers that are divisible by 23.
// // Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// // 391 414 437 460 483
// // Sum : 5313

// function isDivisible() {
//     let sum = 0;
//     for (let n = 0; n <= 500; n++ ){
//             if (n % 23 === 0) {
//                 console.log(n);
//                 sum += n
//             }
//     }
//     console.log(`Sum: ${sum}`);
// }
// isDivisible()


// // Bonus: Add a parameter divisor to the function.
// // isDivisible(divisor)
// // Example:
// // isDivisible(3) : Console.log all the numbers divisible by 3, and their sum
// // isDivisible(45) : Console.log all the numbers divisible by 45, and their sum

// function isDivisible(divisor) {
//     let sum = 0;
//     for (let n=0; n <= 500; n++) {
//         if (n % divisor === 0) {
//             console.log(n);
//             sum += n;
//         }
//     }
//     console.log(`Sum: ${sum}`);
// }
// isDivisible(3);
// isDivisible(45)


// // Exercise 4 : Shopping List
// // Instructions
// // Add the stock and prices objects to your js file.

// // Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

// // Create a function called myBill() that takes no parameters.

// // The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// // The item must be in stock. (Hint : check out if .. in)
// // If the item is in stock find out the price in the prices object.

// // Call the myBill() function.
// // Bonus: If the item is in stock, decrease the item’s stock by 1

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// let shoppingList = ['banana', 'orange', 'apple'];

// function myBill() {
//     let total = 0;
//     for(let item of shoppingList) {
//         if(item in stock && stock[item] > 0) {
//             total += prices[item];
//             stock[item] -= 1 //bonus 
        
//         };
       
//     }
//     return total
// };

// console.log(`Here is my shopping list: ${shoppingList} , and I think only in Switzerland they pay that much per item in total: ${myBill(shoppingList)}`);
// console.log(stock)


// // Exercise 5 : What’s In My Wallet ?
// // Instructions
// // Note: Read the illustration (point 4), while reading the instructions

// // Create a function named changeEnough(itemPrice, amountOfChange) that receives two arguments :
// // an item price
// // and an array representing the amount of change in your pocket.

// // In the function, determine whether or not you can afford the item.
// // If the sum of the change is bigger or equal than the item’s price (ie. it means that you can afford the item), the function should return true
// // If the sum of the change is smaller than the item’s price (ie. it means that you cannot afford the item) the function should return false

// // Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// // A quarters is 0.25
// // A dimes is 0.10
// // A nickel is 0.05
// // A penny is 0.01

// // To illustrate:
// // After you created the function, invoke it like this:
// // changeEnough(4.25, [25, 20, 5, 0])
// // The value 4.25 represents the item’s price
// // The array [25, 20, 5, 0] represents 25 quarters, 20 dimes, 5 nickels and 0 pennies.
// // The function should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)

// function changeEnough(itemPrice, amountOfChange) {
//     const changeValues = [0.25 , 0.10, 0.05, 0.01];
//     let total = 0;
//     for (let i = 0; i < amountOfChange.length; i++) {
//         total += amountOfChange[i] * changeValues[i];
//     }
//     return total >=itemPrice;
// }
// console.log(changeEnough(4.25, [25, 20, 5, 0]));
// console.log(changeEnough(14.11, [2,100,0,0]));
// console.log(changeEnough(0.75, [0,0,20,5]))



// // Exercise 6 : Vacations Costs
// // Instructions
// // Let’s create functions that calculate your vacation’s costs:
// // Define a function called hotelCost().
// // It should ask the user for the number of nights they would like to stay in the hotel.
// // If the user doesn’t answer or if the answer is not a number, ask again.
// // The hotel costs $140 per night. The function should return the total price of the hotel.

// function hotelCost() {
//     while(true) {
//         let nNights = prompt('How many nights would you like to stay?')
//         if (nNights < 1) {
//             alert("Not a valid number")
//             continue;
//         }

//         if (!isNaN(nNights)) {
//             const cost = nNights * 140;
//             return cost;
//         }
//         else {
//             alert('please enter a valid number');
//         }
//         nNights = parseInt(nNights);
//     }
// }
// let cost = hotelCost();
// console.log(`The total cost of your stay is $${cost}`);


// // Define a function called planeRideCost().
// // It should ask the user for their destination.
// // If the user doesn’t answer or if the answer is not a string, ask again.
// // The function should return a different price depending on the location.
// // “London”: 183$
// // “Paris” : 220$
// // All other destination : 300$

// function planeRideCost(){
//     let destination;
//     do {
//       destination = prompt("Please enter your destination (London, Paris or elsewhere):");
//     } while (!destination || typeof destination !== "string");
  
//     switch (destination.toLowerCase()) {
//       case "london":
//         return 183;
//       case "paris":
//         return 220;
//       default:
//         return 300;
//     }
//   }

  // could not solve, how to continue asking user, if he/she enters a number instead of the name
// let ticketCost = planeRideCost();
// console.log(`the plane ticket will cost $${ticketCost}`)


// // Define a function called rentalCarCost().
// // It should ask the user for the number of days they would like to rent the car.
// // If the user doesn’t answer or if the answer is not a number, ask again.
// // Calculate the cost to rent the car. The car costs $40 everyday.
// // If the user rents a car for more than 10 days, they get a 5% discount.
// // The function should return the total price of the car rental.

// function rentalCarCost() {
//     while(true) {
//         let nDays = prompt("For how many days would you like to rent a car?");
//         if (nDays === null) {
//             continue;
//         }
//         nDays = parseInt(nDays)
//         if(!isNaN(nDays)) {
//             const carCost = nDays * 40;
//             let totalCost = carCost;

//             if(nDays >= 10) {
//                 const discount = carCost * 0.05;
//                 totalCost = carCost - discount
//             }
//             return totalCost
//         } else {
//             alert('please enter a valid number')
//         }
//     }
// }
// const rentalCarPrice = rentalCarCost();
// console.log(`the car rent will cost $${rentalCarPrice}`)


// // Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// // Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// // Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().
// // Call the function totalVacationCost()
// function totalVacationCost(){
//     const hotelTotal = hotelCost();
//     const flightTotal = planeRideCost();
//     const rentalTotal = rentalCarCost();

//     const totalVacationCost = hotelTotal + flightTotal + rentalTotal;
//     return totalVacationCost;
// }

// const vacationCost = totalVacationCost();
// console.log(`The total vacation cost is ${vacationCost}`)
// // Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function. You need to change the 3 first functions, accordingly.
