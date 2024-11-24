const results = document.querySelector('#results')
const chuckSearchForm = document.querySelector('#chuck-search-form')
chuckSearchForm.addEventListener('submit', async function(evt){
    evt.preventDefault();
    const value_from_input = document.querySelector('input[name=q]').value;
    results.innerHTML = '';
    try{
        const responce = await fetch(`https://api.chucknorris.io/jokes/search?query=${value_from_input}`);
        const chuck = await responce.json();
        console.log(chuck);
        for (let i = 0; i < chuck["result"].length; i++) {
            const article = document.createElement("article");
            const p = document.createElement("p");
            p.innerHTML = chuck["result"][i]["value"];
            article.appendChild(p);
            results.appendChild(article);
        }
    } catch (error) {
        console.log(error.message);
    }
});