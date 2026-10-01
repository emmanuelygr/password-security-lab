import bcrypt
import json
import os
import re

DB_FILE = 'users.json'

def load_db():
    """Loads the user database from a JSON file."""
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(db):
    """Saves the user database to a JSON file."""
    with open(DB_FILE, 'w') as f:
        json.dump(db, f, indent=4)

def check_password_strength(password):
    """
    Evaluates password strength based on length, uppercase, lowercase, numbers, and special characters.
    Returns a score and feedback.
    """
    score = 0
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters).")
    else:
        score += 1
        
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
        
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
        
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")
        
    if re.search(r"[\W_]", password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%).")

    strength = "Weak"
    if score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"

    return strength, feedback

def create_account():
    print("\n--- Create Account ---")
    username = input("Enter a new username: ")
    db = load_db()
    
    if username in db:
        print("Username already exists. Please choose another.")
        return

    password = input("Enter a password: ")
    strength, feedback = check_password_strength(password)
    
    print(f"Password Strength: {strength}")
    for item in feedback:
        print(f"- {item}")
        
    if strength == "Weak":
        print("Warning: We strongly recommend using a stronger password.")
        
    # Generate a salt and hash the password
    # bcrypt generates a secure salt automatically and includes it in the resulting hash string
    print("Hashing password securely...")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Store the hashed password (decode to store as string in JSON)
    db[username] = {
        'password_hash': hashed.decode('utf-8')
    }
    save_db(db)
    print("Account created successfully!")

def authenticate():
    print("\n--- Authenticate ---")
    username = input("Username: ")
    password = input("Password: ")
    
    db = load_db()
    
    if username not in db:
        print("Authentication failed: User not found.")
        return
        
    stored_hash = db[username]['password_hash'].encode('utf-8')
    
    # bcrypt.checkpw automatically extracts the salt from the stored hash and hashes the provided password to compare
    if bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        print("Authentication successful! Welcome, " + username)
    else:
        print("Authentication failed: Incorrect password.")

def main():
    while True:
        print("\n=== Password Security Lab ===")
        print("1. Create Account")
        print("2. Authenticate")
        print("3. Check Password Strength")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            authenticate()
        elif choice == '3':
            password = input("Enter a password to test: ")
            strength, feedback = check_password_strength(password)
            print(f"Password Strength: {strength}")
            for item in feedback:
                print(f"- {item}")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
