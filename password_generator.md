# Password Generator Program

## Overview
This Python script generates a secure, random password based on a specified length, incorporating letters, numbers, and symbols for enhanced security. Users can create passwords by specifying a length, and the program will ensure that input is valid before generating the password.

## Features
- Prompts users to input their desired password length.
- Generates a password using a mix of uppercase and lowercase letters, numbers, and symbols.
- Provides error handling to ensure valid input.

## Usage
1. Run the program.
2. Enter the desired password length when prompted.
3. The program will generate and display a random password.

## Code

```python
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
```

## How It Works

1. **Importing Modules:** The programm imports `random` and `string` modules.
     - `random.choice()` is used to select random characters.
     - `string` provides sets of characters (`ascii_letters`,`digits`,`punctuation`), for easy character selection.
2. **Defining `generate_password(length)`:** The function creates a password by randomly picking characters from a combined pool of letters, numbers, and symbols.
     - `string.ascii_letters` gives both uppercase and lowercase letters.
     - `string.digits`provides numerical characters.
     - `password` is built by iterating `length` times to randomly select characters from `all_characters`.
3. **User Input:** The program prompts the user for password length and validates it.
     - If the input isn't a valid integer, the program asks again until a valid number is entered.
     - If the input number is less than 1, the program requests a length of at least 1.
4. **Generating and Displaying the Password:** After receiving valid input, the function `generate_password` is called, and the resulting password is printed.

## Example Output

```csharp
Welcome to the Password Generator!
You can create a secure password by specifying the length of the password.

Enter the desired length for your password: 12

Here is your generated password:
a8#Tz!9Pf&wD

Keep your password safe and secure!
```
## Notes

- The program does not save the password. The users should store it securely after generation.
- Password length should be chosen based on security needs, with longer passwords being generally more secure.
