document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');

    if (localStorage.getItem('theme') === 'dark-mode') {
        document.body.classList.add('dark-mode');
        themeIcon.className = 'bi bi-sun';
    }

    toggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        const isDark = document.body.classList.contains('dark-mode');
        themeIcon.className = isDark ? 'bi bi-sun' : 'bi bi-moon';
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
});
