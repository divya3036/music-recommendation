const form = document.querySelector('form');
const loader = document.getElementById('loader');
const results = document.getElementById('results');

form.addEventListener('submit', function() {
    loader.style.display = 'block';
    results.style.display = 'none';

    setTimeout(() => {
        loader.style.display = 'none';
        results.style.display = 'block';
    }, 2500); // 2.5 seconds loading effect
});
