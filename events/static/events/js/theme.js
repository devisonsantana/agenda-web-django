document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');

    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark');
        themeIcon.className = 'bi bi-sun';
    }

    toggleBtn.addEventListener('click', () => {
        document.body.classList.toggle('dark');
        const isDark = document.body.classList.contains('dark');
        themeIcon.className = isDark ? 'bi bi-sun' : 'bi bi-moon';
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
});
