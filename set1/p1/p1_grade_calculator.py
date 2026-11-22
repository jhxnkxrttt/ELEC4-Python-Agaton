#Agaton, Jhon Kurt V. IV-BSIT B 
#Grade Calculator
#November 22, 2026


grades = []

def enter_grades():
    global grades

    grades.clear()

    while True:

        try: 
            grade = float(input("Enter Your Grades: "))

            if 0 <= grades <= 100:
                grades.append(grade)
                print("Grade added Successfully")
            else:
                print("Invalid Grade! Grade must be 0-100!")

        except ValueError:
            print("Invalid Input! Please enter number.")

        another = input("Enter grade again?(y/n)").lower()

        if another != "y":
            break

print(enter_grades)

