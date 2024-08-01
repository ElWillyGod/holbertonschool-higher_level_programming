fetch('https://swapi-api.hbtn.io/api/films/?format=json').then(
    (res) => {
        return res.json();
    })
    .then((lista) => {

        for (let element of lista.results) {
            let li = document.createElement('li');
            li.textContent = element.title;
            document.querySelector('#list_movies').appendChild(li);
        }
    });

