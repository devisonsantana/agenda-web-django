function confirmDelete(eventId, eventTitle) {
    if (confirm(`Deseja realmente excluir o evento "${eventTitle}"?`)) {
        window.location.href = `/agenda/delete/${eventId}`;
    }
}
