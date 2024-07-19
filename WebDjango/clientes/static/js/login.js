document.addEventListener('DOMContentLoaded', () => {
    const showRegister = document.getElementById('show-register');
    const showLogin = document.getElementById('show-login');
    const loginContainer = document.getElementById('login-container');
    const registerContainer = document.getElementById('register-container');

    if (showRegister) {
        showRegister.addEventListener('click', (e) => {
            e.preventDefault();
            loginContainer.style.display = 'none';
            registerContainer.style.display = 'block';
        });
    }

    if (showLogin) {
        showLogin.addEventListener('click', (e) => {
            e.preventDefault();
            registerContainer.style.display = 'none';
            loginContainer.style.display = 'block';
        });
    }

    // Validate Login Form
    document.getElementById('login-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const username = document.getElementById('login-username').value.trim();
        const password = document.getElementById('login-password').value.trim();

        if (username === '' || password === '') {
            alert('Please fill in both fields.');
            return;
        }

        e.target.submit(); // Submit the form if validation passes
    });

    // Validate Registration Form
    document.getElementById('register-form').addEventListener('submit', (e) => {
        e.preventDefault();
        const username = document.getElementById('register-username').value.trim();
        const email = document.getElementById('register-email').value.trim();
        const password = document.getElementById('register-password').value.trim();
        const confirmPassword = document.getElementById('register-confirm-password').value.trim();

        if (username === '' || email === '' || password === '' || confirmPassword === '') {
            alert('Please fill in all fields.');
            return;
        }

        // Simple email validation
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        // Password length validation
        if (password.length < 8) {
            alert('Password must be at least 8 characters long.');
            return;
        }

        // Password match validation
        if (password !== confirmPassword) {
            alert('Passwords do not match.');
            return;
        }

        e.target.submit(); // Submit the form if validation passes
    });
});
