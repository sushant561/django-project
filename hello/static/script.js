document.addEventListener('DOMContentLoaded', function() {
    const message = document.getElementById('success-message');
    if (message) {
        message.style.display = 'block';
        setTimeout(() => {
            message.style.display = 'none';
        }, 5000); // hide after 5 seconds
    }
});
