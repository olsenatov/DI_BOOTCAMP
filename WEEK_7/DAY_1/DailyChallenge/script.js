let planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];

let solarSystem = document.querySelector('.listPlanets')

let colors = {
    'Mercury' : 'grey',
    'Venus' : 'yellow',
    'Earth': 'lightblue',
    'Mars' : 'red',
    'Jupiter' : 'orange',
    'Saturn': 'brown',
    'Uranus' : 'green',
    'Neptune' : 'blue'
}

//bonus
let moons = {
    'Mercury': [],
    'Venus': [],
    'Earth': ['Moon'],
    'Mars': ['Phobos', 'Deimos'],
    'Jupiter': ['Io', 'Europa', 'Ganymede', 'Callisto'],
    'Saturn': ['Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan', 'Iapetus'],
    'Uranus': ['Miranda', 'Ariel', 'Umbriel', 'Titania', 'Oberon'],
    'Neptune': ['Triton']
};

planets.forEach(planetName => {
    let planetDiv = document.createElement('div')
    planetDiv.className = 'planet'
    planetDiv.textContent = planetName
    planetDiv.style.backgroundColor = colors[planetName]
    planetDiv.style.margin = '15px'

    if (moons[planetName]) {
        moons[planetName].forEach(moonName => {
            let moonDiv = document.createElement('div');
            moonDiv.className = 'moon';
            moonDiv.textContent = moonName;

            planetDiv.appendChild(moonDiv);
        });
    } //// couldn't understand how to make moons display outside, and also to be separate from each other
    //// like in case of Saturns' moons - it's too many for one planet =/ but did what i could

    solarSystem.appendChild(planetDiv);
});





