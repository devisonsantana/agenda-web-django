document.addEventListener('DOMContentLoaded', () => {
    const eventForm = document.getElementById('event-form');
    if (eventForm) {
        eventForm.addEventListener('submit', (e) => {
            let valid = true;

            // Título
            const titleInput = document.getElementById('title');
            if (!titleInput.value.trim()) {
                titleInput.classList.add('is-invalid');
                valid = false;
            } else {
                titleInput.classList.remove('is-invalid');
            }

            // Data
            const dateInput = document.getElementById('event-date');
            if (!dateInput.value.trim()) {
                dateInput.classList.add('is-invalid');
                valid = false;
            } else {
                dateInput.classList.remove('is-invalid');
            }

            if (!valid) {
                e.preventDefault(); // impede o submit
            }
        });
    }
});
