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
        print("\nINVALID NUMBER! Please enter numbers only.")

    except ZeroDivisionError:
        print("ERROR! You cannot divide by zero.")

    else:
        print("\nResult:", result)

    finally:
        print("\nDivision operation finished.")

# Function 2: Open and search file
def open_file():
    try:
        filename = input("Enter filename to open: ").strip()

        search_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        found_path = None

        for root, dirs, files in os.walk(search_folder):
            if filename in files:
                found_path = os.path.join(root, filename)
                break

        if found_path is None:
            raise FileNotFoundError

        with open(found_path, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("\nERROR! File not found.")

    except PermissionError:
        print("ERROR! You do not have permission to open this file.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(content)
        print("\nFile location:", found_path)

    finally:
        print("File operation finished.")

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
            print("\nTHANKYOU!")
            break

        else:
            print("\nINVALID SELECTION! Please choose 1-3.")

main()