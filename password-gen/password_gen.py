import secrets
import string

def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def check_strength(password):
    length = len(password)
    if length >= 16:
        return "Strong"
    elif length >= 12:
        return "Medium"
    else:
        return "Weak"

if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    length = int(input("Password ki length daalein : "))
    
    pwd = generate_password(length)
    strength = check_strength(pwd)
    
    print(f"\nGenerated Password: {pwd}")
    print(f"Password Strength: {strength}")
