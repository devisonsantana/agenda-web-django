const body = document.body;
const btn = document.getElementById('theme-toggle');
const icon = document.getElementById('theme-icon');

if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark-mode');
    icon.className = 'bi bi-sun';
}

btn.addEventListener('click', () => {
    const isDark = body.classList.toggle('dark-mode');
    icon.className = isDark ? 'bi bi-sun' : 'bi bi-moon';
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
});