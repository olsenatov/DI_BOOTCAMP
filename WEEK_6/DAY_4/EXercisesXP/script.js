// const people = ["Greg", "Mary", "Devon", "James"];

// Exercise 1

//part1
// .1
// people.splice(0,1);
// console.log(people);
// // .2
// people.splice(2,1, 'Jason');
// console.log(people);
// // .3
// people.push('Ola');
// console.log(people);
// // .4
// console.log(people.indexOf('Mary'))
// // .5
// let slicedPeople = people.slice(1, 3)
// console.log(slicedPeople)
// //.6
// console.log(people.indexOf('Foo')) // -1 because it doesn't exist
// // .7
// let last = people[people.length - 1]
// console.log(last)

//part2
// const people = ["Greg", "Mary", "Devon", "James"];
// //.1
// for (let i = 0; i < people.length; i++ ){
//     console.log(people[i])
// }
// //.2
// for (let i = 0; i < people.length; i++ ){
//     console.log(people[i]);
//         if (i == 2) {
//             break;
//     }
    
// }


// Exercise 2
// // .1.2
// const colors = ['red', 'blue', 'green', 'yellow', 'white']

// for (let i = 0; 1< colors.length; i++ ){
//     console.log('My #' + [i] + " choice is " + colors[i])
//     if (i == colors.length - 1) {
//         break;
//     }
// }


// Exercise 3
// let answer = prompt('Input number');

// while (answer < 10){
//     answer = prompt('Input number');
// }
// alert('The number is correct')


// Exercise 4
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }
// console.log(building.numberOfFloors)
// console.log(`floor 1 has ${building.numberOfAptByFloor.firstFloor} apartments, floor 3 has ${building.numberOfAptByFloor.thirdFloor} apartments`)
// console.log(`Name of the second tenant is ${building.nameOfTenants[1]} and he has ${building.numberOfRoomsAndRent.dan[[0]]} rooms`)

// const sarahRent = building.numberOfRoomsAndRent.sarah[1]
// const danRent = building.numberOfRoomsAndRent.dan[1]
// const davidRent = building.numberOfRoomsAndRent.david[1]

// if (sarahRent + davidRent > danRent) {
//     building.numberOfRoomsAndRent.dan[1] = 1200
//     console.log('Dans rent inscreased to 1200')
// } else {
//     console.log('no change is needed')
// }
// console.log(building.numberOfRoomsAndRent)


// Exercise 5
// const family = {
//     father: 'Max', 
//     mother: "Ola",
//     elderSon: "David",
//     littleSon: "Sam"
// };

// console.log("Keys of the family:");
// for (const key in family) {
//     console.log(key);
// }

// console.log("Values of the family:");
// for (const key in family) {
//     console.log(family[key]);
// }


// Exercise 6
// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
//   };

// sentence = ''
// for (const key in details) {
//     sentence += `${key}  ${details[key]} `; 
    
// }
// console.log(sentence)


// Exercise 7
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// secret = ' '
// for (index in names) {
//     for (letter in index) {
//         let takeLetter = names[index][0]
//         secret += takeLetter
//     }    
// }
// let secretName = secret.split('').sort().join('')
// console.log(secretName)