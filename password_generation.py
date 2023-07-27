import random
import string

def generate_password(length=8):
    characters = string.ascii_lowercase
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 8  # You can change this to your desired password length
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
