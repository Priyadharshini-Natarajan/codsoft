# simple calculator with basic arithmetic operations

# importing necessary modules
import math
import sys

print("\t\tSIMPLE CALCULATOR\n")
print("*" * 96)
c = 'y'
while c == 'y':

    # Displaying the options and getting users choice
    print("\n1.Addition - ( + ) \n2.Subtraction - ( - )\n3.Multiplication - ( * ) \n4.Division - ( / ) \n5.Power - ( ^ )");
    print("*" * 96)

    # getting input from the users
    choice = input("\nEnter your choice number (for example: 1): ")
    num1 = int(input("\nEnter the first number: "))
    num2 = int(input("\nEnter the second number: "))

    # performing arithmetic operations
    if choice == '1':
        result = num1 + num2
        print("\nThe first number is : ", num1)
        print("\nThe second number is : ", num2)
        print("Result after performing Addition operation: ", result)

    elif choice == '2':
        result = num1 - num2
        print("\nThe first number is : ", num1)
        print("\nThe second number is : ", num2)
        print("Result after performing Subtraction operation: ", result)

    elif choice == '3':
        result = num1 * num2
        print("\nThe first number is : ", num1)
        print("\nThe second number is : ", num2)
        print("Result after performing Multiplication operation: ", result)

    elif choice == '4':
        # Exception for division by zero
        if num2 == 0:
            print("\nError: Division by zero is not allowed!")
        else:
            result = num1 / num2
            print("\nThe first number is : ", num1)
            print("\nThe second number is : ", num2)
            print("Result after performing Division operation: ", result)

    elif choice == '5':
        # Exception for the second number being a decimal in power operation
        if num2 != int(num2):
            print("\nError: Power operation requires an integer exponent!")
        else:
            result = math.pow(num1, num2)
            print("\nThe first number is : ", num1)
            print("\nThe second number is : ", num2)
            print("Result after performing Power operation: ", result)

    else:
        print("\nPlease Enter a valid choice")
    c = input("Would you like to perform more operations (y/n)? ")
