"""
Challenge: Offline Credential Manager

Create a CLI tool to manage login credentials (website, username, password) in an encoded local file (`vault.txt`).

Your program should:
1. Add new credentials (website, username, password)
2. Automatically rate password strength (weak/medium/strong)
3. Encode the saved content using Base64 for simple offline obfuscation
4. View all saved credentials (decoding them)
5. Update password for any existing website entry (assignment)

Bonus:
- Support searching for a website entry
- Mask password when showing in the list
"""

import base64
import os
import string 

VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(ch in string.punctuation for ch in password)
    
    score = sum([length >= 8 , has_digit , has_upper , has_special , has_lower])

    return ["invalid" , "weak" , "medium" , "strong" , "very strong"][min(score , 4)]

def add_credentials():
    website = input("Enter the website url: ").strip()
    username = input("Enter the username: ").strip()
    password = input("Enter the password: ").strip()

    strength = password_strength(password)

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE , "a" , encoding="utf-8") as f:
        f.write(encoded_line+'\n')

    print("\nCredential Saved !!")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File Not Found !!")
        return 
    
    with open(VAULT_FILE , "r" , encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website , username , password = decoded.split("||")
            print(f"{website} | {username} | {password}")

def main():
    while True:
        print("\n🔒 Credential Manager")
        print("1. Add credential")
        print("2. View credentials")
        print("3. Update password")
        print("4. Exit")
    
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1": add_credentials()
            case "2": view_credentials()
            case "3": pass 
            case "4": break
            case _:
                print("Invalid choice !!")
                break

if __name__ == "__main__":
    main()
