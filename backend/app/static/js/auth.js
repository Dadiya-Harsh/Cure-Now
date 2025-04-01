document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, email, password })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (response.ok) {
            // Redirect to login or home page
            window.location.href = '/';
        }
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('resetPasswordForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const email = document.getElementById('email').value;
    const new_password = document.getElementById('new_password').value;

    fetch('/reset_password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, new_password })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (response.ok) {
            // Redirect to login or home page
            window.location.href = '/';
        }
    })
    .catch(error => console.error('Error:', error));
});
