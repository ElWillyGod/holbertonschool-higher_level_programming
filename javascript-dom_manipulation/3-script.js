const header = document.querySelector('header');

document.querySelector('#toggle_header').addEventListener('click', () => {
    if (header.classList.contains('red')) {
        header.classList.replace('red', 'green');
    } else {
        header.classList.replace('green', 'red');
    }
});