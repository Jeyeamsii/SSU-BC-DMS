const validUsername = "admin";
const validPassword = "password123";

function validateAndRedirect() {
    // Get values from input fields
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Validate the username and password
    if (username === validUsername && password === validPassword) {
        // If correct, redirect to home page
        window.location.href = ""; // Replace "home.html" with your home page URL
    } else {
        // If incorrect, show an error message
        alert("Invalid username or password. Please try again.");
    }
}