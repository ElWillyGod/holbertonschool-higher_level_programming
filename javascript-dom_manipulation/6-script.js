fetch("https://swapi-api.hbtn.io/api/people/5/?format=json").then((res) => {
  return res.json();
})
.then((data) => {
    document.querySelector('#character').textContent = data.name;
});
