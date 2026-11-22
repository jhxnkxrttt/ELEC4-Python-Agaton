#Agaton, Jhon Kurt V. IV-BSIT B 
#Grade Calculator
#November 22, 2026

#Function #1 "Input Grade"
grades = []

def enter_grades():
    global grades

    grades.clear()

    while True:

        try: 
            grade = float(input("Enter Your Grade: "))

            if 0 <= grade <= 100:
                grades.append(grade)
                print("Grade added Successfully")
            else:
                print("Invalid Grade! Grade must be 0-100!")

        except ValueError:
            print("Invalid Input! Please enter number.")

        another = input("Enter grade again?(y/n)").lower()

        if another != "y":
            break

#Function 2: computing the average of grades
def compute_average(grades):
    return sum(grades) / len(grades)

#Function 3:get the highest grade
def get_high_grade(grades):
    return max(grades)

#Function 4: get the lowest grade
def get_low_grade(grades):
    return min(grades)

#Function 5: Determine wheter PASS or FAIL
def grade_status(grades):
    average = compute_average(grades)

    if average >= 75:
        return "PASSED"
    else:   
        return "FAILED"

#Function 6: View the results
def view_grades(grades):
    if len(grades) == 0:
        print("You must enter GRADE first!")
        return

    average = compute_average(grades)
    highest = get_high_grade(grades)
    lowest = get_low_grade(grades)
    status = grade_status(grades)

    print("\n===== STUDENT RESULTS =====")
    print("Grades:", grades)
    print("Average:", round(average, 2))
    print("Highest Grade:", highest)
    print("Lowest Grade:", lowest)
    print("Status:", status)

#Function 7: MAIN MENU
def main():
    while True:
        print("\n===STUDENT GRADE LIST/CALCULATOR===")
        print("1. Grade Calculator")
        print("2. View grade")
        print("3. Exit")

        choice = input("Enter Number 1-3: ")

        if choice == "1":
            enter_grades()
        elif choice == "2":
            view_grades(grades)
        elif choice == "3":
            print("Thankyou student!")
            break
        else:
            print("you must select from 1-3!")

main()


