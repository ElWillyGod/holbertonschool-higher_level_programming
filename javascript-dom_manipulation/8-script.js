fetch('https://hellosalut.stefanbohacek.dev/?lang=fr').then(
    (res) => {
        return res.json();
    })
    .then((data) => {
        const obj = document.getElementById('hello');
        obj.textContent = data.hello;
    });