document.querySelector('#add_item').addEventListener('click', () => {
    const ul = document.querySelector('.my_list');
    const li = document.createElement('li');
    li.textContent = 'Item';
    ul.appendChild(li);
});