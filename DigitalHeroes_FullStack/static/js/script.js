document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (toggle && navLinks) {
        toggle.addEventListener('click', () => {
            navLinks.classList.toggle('open');
        });
    }

    const form = document.getElementById('leadForm');
    if (!form) return;

    form.addEventListener('submit', (event) => {
        const name = form.querySelector('input[name="name"]');
        const email = form.querySelector('input[name="email"]');
        const message = form.querySelector('textarea[name="message"]');
        const budget = form.querySelector('select[name="budget"]');

        const errors = [];

        if (!name || name.value.trim().length < 2) {
            errors.push('Please enter your full name.');
        }

        if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())) {
            errors.push('Please enter a valid email address.');
        }

        if (!budget || !budget.value) {
            errors.push('Please select a budget range.');
        }

        if (!message || message.value.trim().length < 10) {
            errors.push('Please share a message with at least 10 characters.');
        }

        if (errors.length) {
            event.preventDefault();
            const errorBox = form.querySelector('.form-error-global');
            if (errorBox) {
                errorBox.remove();
            }
            const container = document.createElement('div');
            container.className = 'form-error form-error-global';
            container.innerText = errors.join(' ');
            form.prepend(container);
        }
    });
});
