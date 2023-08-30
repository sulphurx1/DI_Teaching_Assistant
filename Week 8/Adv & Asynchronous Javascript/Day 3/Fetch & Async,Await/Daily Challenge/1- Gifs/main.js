const API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
const gifContainer = document.getElementById("gif-container");
const deleteAllButton = document.getElementById("delete-all");

searchForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const searchQuery = searchInput.value.trim();
    if(searchQuery !== "") {
        const gifData = await fetchGif(searchQuery);
        if (gifData) {
            appendGif(gifData);
        }
    }
});

deleteAllButton.addEventListener("click", () => {
    gifContainer.innerHTML = "";
});

async function fetchGif(category) {
    const apiUrl = `https://api.giphy.com/v1/gifs/random?api_key=${API_KEY}&tag=${category}`;
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();
        if(data.data && data.data.images) {
            return data.data;
        }
        else {
            console.error("Invalid response from Giphy API");
            return null;
        }
    }
    catch (error) {
        console.error("Error fetching data from Giphy API", error);
        return null;
    }
}

function appendGif(gifData) {
    const gifUrl = gifData.images.downsized.url;

    const gifElement = document.createElement("div");
    gifElement.className = "gif-item";

    const img = document.createElement("img");
    img.src = gifUrl;

    const deleteButton = document.createElement("button");
    deleteButton.innerText = "Delete";
    deleteButton.addEventListener("click", () => {
        gifElement.remove();
    });

    gifElement.appendChild(img);
    gifElement.appendChild(deleteButton);

    gifContainer.appendChild(gifElement);
}