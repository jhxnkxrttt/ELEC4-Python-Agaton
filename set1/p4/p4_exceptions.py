# Agaton, Jhon Kurt V. IV-BSIT B
# P3: Student Record Manager
# November 23, 2026
import os
# Function 1: Division
def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Error! You cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")

# Function 3: Main menu
def main():
    while True:
        print("\n SAFE MENU PROGRAM ")
        print("1. Division")
        print("2. Open file")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Thank you! Goodbye!")
            break

        else:
            print("Invalid selection! Please choose 1-3.")

main()