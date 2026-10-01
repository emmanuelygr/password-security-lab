# Password Security Lab

**Author**: emmanuelygr

## Overview
Password Security Lab is an interactive command-line application built in Python that demonstrates core concepts of modern password security. The tool provides a hands-on learning environment for understanding how passwords are safely processed, evaluated, and stored using industry-standard hashing techniques.

## Why Built
This project was developed to provide a practical understanding of cybersecurity fundamentals, specifically focusing on authentication and password management. Many data breaches occur due to poor password storage practices (like storing passwords in plain text or using weak hashing algorithms without salts). Building this tool demonstrates how to implement secure password handling and evaluate password strength properly.

## Learning Objectives
- **Hashing**: Understand how to convert a plain-text password into a secure hash.
- **Salting**: Learn the importance of adding random data to passwords before hashing to defend against rainbow table attacks.
- **Verification**: Grasp how to verify user input against a stored hash without ever knowing the actual password.
- **Authentication**: Build a basic user registration and login flow.
- **Password Strength Evaluation**: Analyze passwords for length, complexity, and character variety.

## Features
- **Account Creation**: Register new users with strong password recommendations.
- **Authentication**: Secure login system comparing input against stored hashes.
- **Password Strength Checker**: Evaluate password complexity with actionable feedback.
- **Secure Storage**: Passwords are never saved in plain text; they are hashed and salted using bcrypt.

## Technologies
- **Python 3.x**: Core programming language.
- **bcrypt**: Industry-standard library for secure password hashing.
- **JSON**: Lightweight data interchange format for simulating a database (`users.json`).
- **re (Regular Expressions)**: For evaluating password complexity.

## Cybersecurity Concepts

### Plaintext vs Hash
A **plaintext** password is the exact string a user types (e.g., `Password123!`). Storing this is highly insecure. A **hash** is a cryptographic function that transforms the plaintext into a fixed-length, unpredictable string. Unlike encryption, hashing is a one-way process; you cannot reverse a hash back to the plaintext.

### Salting
A **salt** is random data added to a password before hashing. If two users have the same password, they will have the same hash without salting. This makes them vulnerable to pre-computed attacks (Rainbow Tables). A salt ensures that even identical passwords produce entirely different hashes.

### Verification and Authentication
**Authentication** is the process of proving a user's identity. During login, the system takes the provided password, applies the same salt and hash function used during registration, and compares the resulting hash with the stored hash. If they match, the user is authenticated.

### Password Strength
A strong password is computationally harder to crack through brute force or dictionary attacks. Evaluating password strength involves checking:
- **Length**: Longer passwords exponentially increase the time needed to crack.
- **Complexity**: Utilizing a mix of uppercase, lowercase, numbers, and special characters expands the possible character set.

## How It Works
1. **Registration**: User enters a username and password. The system evaluates the password strength and provides feedback. It then generates a salt, hashes the password using `bcrypt`, and stores the username and the resulting hash in `users.json`.
2. **Login**: User enters credentials. The system retrieves the hash for the username, extracts the salt, hashes the entered password, and compares the results.
3. **Strength Check**: Uses regex to determine if the password meets security criteria (uppercase, lowercase, digits, special characters, length >= 8).

## Project Structure
```text
password-security-lab/
│
├── password_lab.py      # Main application logic
├── requirements.txt     # Python dependencies
├── users.json           # Local JSON database (created after first user)
├── .gitignore           # Git ignore configuration
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

## Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone <repository_url>
   cd password-security-lab
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```bash
python password_lab.py
```

Follow the on-screen menu:
```text
=== Password Security Lab ===
1. Create Account
2. Authenticate
3. Check Password Strength
4. Exit
Choose an option:
```

## Examples & Expected Output

### Account Creation
```text
--- Create Account ---
Enter a new username: alice
Enter a password: password
Password Strength: Weak
- Add uppercase letters.
- Add numbers.
- Add special characters (!@#$%).
Warning: We strongly recommend using a stronger password.
Hashing password securely...
Account created successfully!
```

### Authentication
```text
--- Authenticate ---
Username: alice
Password: password
Authentication successful! Welcome, alice
```

### Password Strength Checker
```text
Enter a password to test: SuperS3cr3t!
Password Strength: Strong
```

## Security Considerations
- **Local Storage**: This project uses a local `users.json` file to store credentials for educational purposes. In a production environment, you would use a secure, scalable database.
- **bcrypt Work Factor**: The `bcrypt` library uses a default work factor (rounds) to ensure hashing is slow enough to thwart brute-force attacks. This can be adjusted based on hardware capabilities.

## Ethical/Legal Use
This tool is for **educational purposes only**. It is designed to teach defensive security concepts. Do not use this tool or its concepts to attempt unauthorized access to systems, intercept communications, or process real user data in production without proper security reviews. 

## Limitations
- **In-Memory/File Storage**: `users.json` is not a secure database and is prone to file corruption or unauthorized local access.
- **No Rate Limiting**: The current implementation does not limit login attempts, leaving it vulnerable to automated brute-force attacks.
- **No Password Recovery**: There is no mechanism to reset a forgotten password.

## Troubleshooting / FAQ

**Q: I get a `ModuleNotFoundError: No module named 'bcrypt'` error.**
A: Ensure you have installed the requirements using `pip install -r requirements.txt`. If you are using a virtual environment, make sure it is activated.

**Q: Where are the passwords stored?**
A: They are stored as bcrypt hashes inside `users.json` in the same directory. The file is created automatically when the first user registers.

## What I Learned
- Implementing secure password hashing in Python using `bcrypt`.
- The practical difference between encryption and hashing.
- Designing a rudimentary authentication flow.
- Using regular expressions to validate and evaluate string patterns.

## Future Improvements
1. **Implement Rate Limiting**: Add a delay or lockout mechanism after multiple failed login attempts to prevent brute-force attacks.
2. **Database Integration**: Migrate from `users.json` to a robust database like SQLite or PostgreSQL.
3. **Password Policies**: Enforce strict password policies during registration rather than just providing warnings.
4. **Multi-Factor Authentication (MFA)**: Introduce a secondary authentication step (e.g., OTP via email or authenticator app).
5. **Session Management**: Implement a secure session token system to keep users logged in across actions.
6. **GUI Integration**: Build a graphical user interface using Tkinter or a web framework like Flask/Django.
