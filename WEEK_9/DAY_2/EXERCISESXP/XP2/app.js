import people from './data.js'

function calculateAverageAge(peopleArray) {
    const totalAge = peopleArray.reduce((sum, person) => sum + person.age, 0);
    const averageAge = totalAge / peopleArray.length;
    return averageAge;
  }

  console.log(calculateAverageAge(people));

  

