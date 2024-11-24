const tvsearchform = document.querySelector('#tv-search-form')
const results = document.querySelector('#results')
tvsearchform.addEventListener('submit', async function(evt) {
    // ... prevent the default action.
    evt.preventDefault();
    // get value of input element
    const query = document.querySelector('input[name=q]').value;
    results.innerHTML = '';
    try {                                               // error handling: try/catch/finally
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=:${query}`);    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        for(let i = 0; i<jsonData.length;i++){
            const article = document.createElement("article");
            const h2 = document.createElement("h2");
            h2.innerHTML = jsonData[i]["show"]["name"];
            const a = document.createElement("a");
            a.innerHTML = jsonData[i]["show"]["url"];
            a.target = "_blank";
            const img = document.createElement("img");
            img.src = jsonData[i].show.image?.medium;
            img.alt = jsonData[i]["show"]["name"];
            const div = document.createElement("div");
            div.innerHTML = jsonData[i]["show"]["summary"];
            article.appendChild(h2);
            article.appendChild(a);
            article.appendChild(img);
            article.appendChild(div);
            results.appendChild(article);

        }
    } catch (error) {
        console.log(error.message);
    }
});