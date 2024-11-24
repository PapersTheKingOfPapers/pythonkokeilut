async function chuckNorr(){
    try{
        const responce = await fetch("https://api.chucknorris.io/jokes/random");
        const chuck = await responce.json();
        console.log(chuck["value"]);
    } catch (error) {
        console.log(error.message)
    }
}

chuckNorr();