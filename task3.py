import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_length():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Enter a valid integer")

def main():
    length = get_length()
    
    
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
