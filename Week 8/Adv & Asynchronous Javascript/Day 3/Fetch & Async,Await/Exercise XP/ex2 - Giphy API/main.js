const API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const SEARCH_ITEM = 'sun';
const LIMIT = 10;
const OFFSET = 2;

url = `https://api.giphy.com/v1/gifs/search?q=${SEARCH_ITEM}&api_key=${API_KEY}&limit=${LIMIT}&offset=${OFFSET}`;

fetch(url).then(response => {
    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json()
})
.then(data => {
    console.log(data);
})
.catch(erro => {
    console.error(`Fetch error: `, error);
});