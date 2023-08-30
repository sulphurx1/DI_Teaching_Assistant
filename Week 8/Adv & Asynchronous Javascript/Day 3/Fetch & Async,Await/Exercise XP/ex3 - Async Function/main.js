async function fetchStarship() {
    try {
        const response = await fetch("https://www.swapi.tech/api/starships/9/");

        if (!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const objectStar = await response.json();
        console.log(objectStar.result);
    }
    catch(error) {
        console.error("An error occurred:", error);
    }
}

fetchStarship();