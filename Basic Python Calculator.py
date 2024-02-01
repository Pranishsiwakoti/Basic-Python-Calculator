print("Basic Python Calculator")

import math

def basic_calculator():
    # These are the prompts where the user adds their numbers to apply Operations on them. You can add more numbers if you want to add more than 2 times.
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # These are the mathematical Operations. If you have any more Operations you can add them.
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter choice (1/2/3/4): ")
s
    # These Program select Operations and display the result. These code is very Inmportant.
    if choice == '1':
        result = num1 + num2
        print("Result:", result)
    elif choice == '2':
        result = num1 - num2
        print("Result:", result)
    elif choice == '3':
        result = num1 * num2
        print("Result:", result)
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero!")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    basic_calculator()

# This is the Program which works during exiting time.
import subprocess

def main():
    while True:
        user_input = input("Enter a command (type 'bye' to exit): ")
        if user_input.lower() == 'bye':
            break
        elif user_input.lower() == 'execute':
            subprocess.call(["python", "script1.py"])  
        else:
            print("Type bye to exit. Try again!")

if __name__ == "__main__":
    main()