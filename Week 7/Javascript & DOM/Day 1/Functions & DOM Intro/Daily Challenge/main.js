const solarSystem = [
    { name: "Mercury", color: "gray", moons: 0 },
    { name: "Venus", color: "orange", moons: 0 },
    { name: "Earth", color: "blue", moons: 1 },
    { name: "Mars", color: "red", moons: 2 },
    { name: "Jupiter", color: "orange", moons: 79 },
    { name: "Saturn", color: "goldenrod", moons: 83 },
    { name: "Uranus", color: "lightblue", moons: 27 },
    { name: "Neptune", color: "darkblue", moons: 14 }
];

let listPlanets = document.querySelector(".listPlanets");


solarSystem.forEach(planet => {
    let planetDiv = document.createElement("div");
    planetDiv.className = "planet " + planet.name.toLowerCase();
    planetDiv.style.backgroundColor = planet.color;
    planetDiv.innerText = planet.name;

    if (planet.moons > 0) {
        for (let i = 0; i < planet.moons; i++) {
            let moonDiv = document.createElement("div");
            moonDiv.className = "moon";
            moonDiv.style.left = Math.random() * 100 + "%";
            moonDiv.style.top = Math.random() * 100 + "%";
            planetDiv.appendChild(moonDiv);

        }
    }

    listPlanets.appendChild(planetDiv)
})

