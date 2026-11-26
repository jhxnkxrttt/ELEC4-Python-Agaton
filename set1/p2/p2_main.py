
# Agaton, Jhon Kurt V. IV-BSIT B
# P2: Custom Module
# November 22, 2026

import student_utils
from student_utils import get_high_grade, get_low_grade
import datetime


# Function 1: Enter grades
def enter_grades():
    grades = []

    while True:
        try:
            grade = float(input("Enter Your Grade (0-100): "))

            if 0 <= grade <= 100:
                grades.append(grade)
                print("Grade added successfully!")
            else:
                print("Invalid Grade! Grade must be 0-100.")

        except ValueError:
            print("Invalid Input! Please enter a number.")
    
        another = input("Enter another grade? (y/n): ").lower()

        if another != "y":
          break

    return grades

# Function 2: View results
def view_results(grades):

    if len(grades) == 0:
        print("You must enter grades first!")
        return

    average = student_utils.compute_average(grades)
    status = student_utils.grade_status(grades)
    highest = get_high_grade(grades)
    lowest = get_low_grade(grades)

    print("\n===== STUDENT RESULTS =====")
    print("Grades:", grades)
    print("Average:", round(average, 2))
    print("Highest Grade:", highest)
    print("Lowest Grade:", lowest)
    print("Status:", status)

    # Built-in module: datetime
    current_time = datetime.datetime.now()
    print("Report generated:", current_time.strftime("%Y-%m-%d %H:%M:%S"))


# Function 3: Main menu
def main():
    grades = []

    while True:
        print("\n===== P2 STUDENT GRADE CALCULATOR =====")
        print("1. Enter grades")
        print("2. View results")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            grades = enter_grades()

        elif choice == "2":
            view_results(grades)

        elif choice == "3":
            print("Thank you! Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-3.")


main()

# The first import style is import module, which imports the entire module. 
# When using this style, we need to use the module name followed by the function name 
# to access its functions. The second import style is from module import name,
# which allows us to import specific functions from a module
# and use them directly without typing the module name.
# In my program, I used both styles to demonstrate how Python
# imports reusable functions from my custom module student_utils.