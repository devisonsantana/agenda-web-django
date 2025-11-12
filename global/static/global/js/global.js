document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const toggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');

    const storedTheme = localStorage.getItem('theme');
    if (storedTheme === 'dark') {
        body.classList.add('dark-mode');
        themeIcon.className = 'bi bi-sun-fill';
    }

    toggleBtn?.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        const isDark = body.classList.contains('dark-mode');
        themeIcon.className = isDark ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
});
