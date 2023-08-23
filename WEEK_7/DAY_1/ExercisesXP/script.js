// ////Exercise 1
// function displayNumbersDivisible() {
//     let sum = 0;
//     for (let n = 0; n<=500; n++){
//         if (n % 23 === 0) {
//             console.log(n);
//             sum+= n;
//         }
//     }
//     console.log(`Sum: ${sum}`)
// }
// displayNumbersDivisible()

// ////bonus
// function displayNumbersDivisible(divisor) {
//     let sum = 0;
//     for (let n = 0; n<=500; n++){
//         if (n % divisor === 0) {
//             console.log(n);
//             sum+= n;
//         }
//     }
//     console.log(`Sum: ${sum}`)
// }
// displayNumbersDivisible(10)


////Exercise 2

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
//             total +=prices[item];
//             stock[item] -=1 //bonus
//         }
//     }
//     return total
// }
// console.log(myBill(shoppingList))
// console.log(`Here is my shoping list: ${shoppingList}, and I will pay in total: ${myBill(shoppingList)}`)
// console.log(stock)


////Exercise 3
// function changeEnough(itemPrice, amountOfChange) {
//     const changeValues = [0.25, 0.10, 0.05, 0.01];
//     let total = 0;
//     for (let i = 0; i < amountOfChange.length; i++) {
//         total += amountOfChange[i] * changeValues[i];
    
//     }
//     return total >=itemPrice;
// }
// console.log(changeEnough(4.25, [25, 20, 5, 0]))
// console.log(changeEnough(14.11, [2,100,0,0]))


////Exercise 4
// //#1
// function hotelCost() {
//     while(true) {
//         let nNights = prompt('How many nights would you like to stay?');
//         if (nNights === null) {
//             continue;
//         }
//         nNights =parseInt(nNights);

//         if (!isNaN(nNights)) {
//             const cost = nNights * 140;
//             return cost;
//         }
//         else {
//             alert ('please enter a valid number of nights')
//         }
//     }
// }
// let cost = hotelCost()
// console.log(`The total for your stay is ${cost}`)
// //#2
// function planeRideCost(){
//     while(true) {
//         let destination = prompt('What is the destination?')
//         if (destination === null) {
//             continue;
//         }
//         if (typeof destination === 'string') {
//             if (destination === 'London') {
//                 return 183;
//             }
//             else if (destination === 'Paris') {
//                 return 220
//             }
//             else {
//                 return 300
//             }
//             }
//             else {
//                 alert('please enter valid name of destination');
//             }

//         }
//     }
    
// let ticketCost = planeRideCost()
// console.log(`the plane ticket will cost ${ticketCost} $`)

// //#3
// function rentalCarCost(){
//     while(true) {
//         let nDays = prompt('For how many days would you like to rent a car?')
//         if (nDays === null) {
//             continue;
//         }
//         nDays = parseInt(nDays)
//         if (!isNaN(nDays)) {
//             const carCost = nDays *40;
//             let totalCost = carCost;

//             if (nDays >= 10) {
//                 const discount = carCost * 0.05;
//                 totalCost -= discount;
//             }
//             return totalCost
//         } else {
//             alert("Please enter a valid number")
        
//     } 

//     }
// }

// const rentalCarPrice = rentalCarCost()
// console.log(`the car rent will cost ${rentalCarPrice} $`)

// //#4
// function totalVacationCost() {
//     const hotelTotal = hotelCost();
//     const planeTotal= planeRideCost();
//     const rentalTotal= rentalCarCost();
    
//     const totalVacationCost = hotelTotal+ planeTotal+ rentalTotal;
//     return totalVacationCost;
// }

// const vacationCost = totalVacationCost();
// console.log(`The total vacation cost is ${vacationCost} $`);

////Exercise 5, 6, 7

////made separate folders for those