# password_strength_checker.py
import re
import math
import requests
import hashlib

def password_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32
    return len(password) * math.log2(charset) if charset > 0 else 0

def strength_label(entropy):
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Reasonable"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"

def check_pwned(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def main():
    print("🔐 Password Strength Checker")

    try:
        password = input("Enter a password to evaluate: ")
    except Exception as e:
        print(f"Input error: {e}\nUsing default test password.")
        password = "Password!1234"  # fallback

    print(f"Evaluating password: {password}")

    entropy = password_entropy(password)
    strength = strength_label(entropy)
    print(f"\nEntropy Score: {entropy:.2f}")
    print(f"Strength: {strength}")

    try:
        count = check_pwned(password)
        if count:
            print(f"⚠️ Warning: This password has been seen {count} times in data breaches!")
        else:
            print("✅ This password has not been seen in known breaches.")
    except Exception as e:
        print(f"(Optional breach check failed: {e})")

if __name__ == "__main__":
    main()
