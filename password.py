#Building a password generator
#importing necessary module

import random

#defining function based on user requirements

def password_generator(length, use_uppercase, use_lowercase, use_digits, use_special_chars):

      #declaring necessary char/symbols for passwords
      upper1      =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      lower1      =   upper1.lower()
      digit         =   '1234567890'
      symbols   =    '!@#$%^&*?/  |`~'
      characters = ' '

      if use_uppercase:
            characters += upper1
      if use_lowercase:
            characters += lower1
      if use_digits:
            characters += digit
      if use_special_chars:
            characters += symbols
    
      if not characters:
            print("Select at least one character type.")
            return None

      #making random choices in user specified characters
      password = ''.join(random.choice(characters) for i in range(length))
      return password

def main():

      #exception block for catching password length <0
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a valid length greater than zero.")
            return

        #getting input from user for their specifications
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

        #passing user interest as function parameters
        password = password_generator(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input.Enter a valid integer for the password length.")

if __name__ == "__main__":
    main()
