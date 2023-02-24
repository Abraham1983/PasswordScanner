import hashlib
import requests
import re

# Define the password to check
password = "password123"

# Check if the password is strong (at least 8 characters long and contains at least one uppercase letter, one lowercase letter, one digit, and one special character)
if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
    print("This password is not strong.")
else:
    print("This password is strong.")

# Hash the password using SHA-1
hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()

# Send a request to the haveibeenpwned.com API to check if the password has been leaked
response = requests.get(f"https://api.pwnedpasswords.com/range/{hashed_password[:5]}")

# Parse the response to check if the password has been leaked
if response.status_code == 200:
    for line in response.content.decode().splitlines():
        if hashed_password[5:] in line.split(":")[0]:
            print("This password has been leaked in a data breach.")
            break
    else:
        print("This password has not been leaked in a data breach.")
else:
    print("Error: Could not check if the password has been leaked.")

# Check if the password has been reused (appears in a list of previous passwords)
previous_passwords = ["password123", "123456789", "qwertyuiop"]
if password in previous_passwords:
    print("This password has been reused.")
else:
    print("This password has not been reused.")
