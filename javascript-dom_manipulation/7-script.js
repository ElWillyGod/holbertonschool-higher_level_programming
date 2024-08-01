fetch('https://swapi-api.hbtn.io/api/films/?format=json').then(
    (res) => {
        return res.json();
    })
    .then((lista) => {

        lista.results.forEach((element) => {
            let li = document.createElement('li');
            li.textContent = element.title;
            document.querySelector('#list_movies').appendChild(li);
    });
});