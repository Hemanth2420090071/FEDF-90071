<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Form Validation Example</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 40px;
    }
    .form-group {
      margin-bottom: 15px;
    }
    .error {
      color: red;
      font-size: 14px;
      display: none;
    }
    input.invalid {
      border: 2px solid red;
    }
    input.valid {
      border: 2px solid green;
    }
    button {
      padding: 10px 15px;
      border: none;
      background: #007bff;
      color: white;
      cursor: pointer;
      border-radius: 5px;
    }
    button:disabled {
      background: #999;
    }
  </style>
</head>
<body>
  <h2>Signup Form</h2>
  <form id="signupForm">
    <div class="form-group">
      <label>Username:</label><br>
      <input type="text" id="username" required>
      <div class="error" id="usernameError">Username is required (min 3 characters)</div>
    </div>

    <div class="form-group">
      <label>Email:</label><br>
      <input type="email" id="email" required>
      <div class="error" id="emailError">Enter a valid email address</div>
    </div>

    <div class="form-group">
      <label>Password:</label><br>
      <input type="password" id="password" required>
      <div class="error" id="passwordError">Password must be at least 6 characters</div>
    </div>

    <button type="submit" id="submitBtn">Register</button>
  </form>

  <script>
    // DOM Elements
    const form = document.getElementById("signupForm");
    const username = document.getElementById("username");
    const email = document.getElementById("email");
    const password = document.getElementById("password");

    const usernameError = document.getElementById("usernameError");
    const emailError = document.getElementById("emailError");
    const passwordError = document.getElementById("passwordError");

    // Validation Functions
    function validateUsername() {
      if (username.value.trim().length < 3) {
        username.classList.add("invalid");
        username.classList.remove("valid");
        usernameError.style.display = "block";
        return false;
      }
      username.classList.remove("invalid");
      username.classList.add("valid");
      usernameError.style.display = "none";
      return true;
    }

    function validateEmail() {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!regex.test(email.value.trim())) {
        email.classList.add("invalid");
        email.classList.remove("valid");
        emailError.style.display = "block";
        return false;
      }
      email.classList.remove("invalid");
      email.classList.add("valid");
      emailError.style.display = "none";
      return true;
    }

    function validatePassword() {
      if (password.value.length < 6) {
        password.classList.add("invalid");
        password.classList.remove("valid");
        passwordError.style.display = "block";
        return false;
      }
      password.classList.remove("invalid");
      password.classList.add("valid");
      passwordError.style.display = "none";
      return true;
    }

    // Event Handling
    username.addEventListener("input", validateUsername);
    email.addEventListener("input", validateEmail);
    password.addEventListener("input", validatePassword);

    form.addEventListener("submit", function (e) {
      e.preventDefault(); // prevent form submission

      const isValidUsername = validateUsername();
      const isValidEmail = validateEmail();
      const isValidPassword = validatePassword();

      if (isValidUsername && isValidEmail && isValidPassword) {
        alert("Form submitted successfully!");
        form.reset();

        // remove styles after reset
        username.classList.remove("valid", "invalid");
        email.classList.remove("valid", "invalid");
        password.classList.remove("valid", "invalid");
      } else {
        alert("Please fix the errors before submitting.");
      }
    });
  </script>
</body>
</html>
