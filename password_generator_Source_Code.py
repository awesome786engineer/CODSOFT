import random
import string

def generate_password(length):
    letters = string.ascii_letters       
    numbers = string.digits              
    symbols = string.punctuation         
    all_characters = letters + numbers + symbols
    password = ''

    for _ in range(length):
        password += random.choice(all_characters)  

    return password
    
print("Welcome to the Password Generator!")
print("You can create a secure password by specifying the length of the password.\n")

while True:
    try:
        length = int(input("Enter the desired length for your password: "))
        if length < 1:
            print("Password length should be at least 1. Please try again.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

generated_password = generate_password(length)

print("\nHere is your generated password:")
print(generated_password)
print("\nKeep your password safe and secure!")
